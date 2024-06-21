#!/usr/bin/env python3
"""
 Gps interface node.

 This node receives gps messages from socket. It is similar to `gps_node` from `roxbot`,
 but eliminates the the need for a separate container and mqtt messages.

 **Note**: this node still publishes the gps message to mqtt topic.

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""
import asyncio
import time

from fixposition.messages import GgaData, HdtData
from fixposition.parser import parse
from fixposition.receiver import receive
from pydantic_settings import BaseSettings, SettingsConfigDict
from roxbot import Node
from roxbot.config import MqttConfig
from roxbot.exceptions import FixException, FixProblem
from roxbot.interfaces import Pose, GpsLatlon, GpsHeading


class FPX_Config(BaseSettings):
    """Fixposition related settings"""

    model_config = SettingsConfigDict(env_prefix="fpx_")

    host: str = "localhost"
    port: int = 21000

    # mocked data config
    mock_data_freq: float = 5.0  # frequency of mock data in Hz


class FpxNode(Node):
    """interface to gps data, works in latitude and longitude."""

    def __init__(self, mock: bool = False) -> None:
        """Initialize the node. When `mock` is True, the node will generate mock data from self.latlon and self.heading."""
        super().__init__()

        self._is_mock = mock

        self.latlon = (0.0, 0.0)
        self.heading = 0.0
        self.gps_qual = 0
        self.last_update = time.time()

        self._msg_q: asyncio.Queue[bytes] = asyncio.Queue()

        if not self._is_mock:
            self._coros.append(self._receive)
        else:
            self._log.warning("Mocking gps data")
            self.latlon = (51.36595, 6.172037)
            self._coros.append(self._send_mock_data)

    def get_pose(self, max_age: float = 1.0) -> Pose:
        """returns pose or raises FixException if data is too old"""
        if time.time() - self.last_update > max_age:
            raise FixException(FixProblem.OLD_FIX)

        return Pose.from_gps(self.latlon[0], self.latlon[1], self.heading)

    async def _send_mock_data(self) -> None:
        """broadcast mock data to mqtt"""
        fpx_cfg = FPX_Config()
        mqtt_cfg = MqttConfig()

        delay = 1 / fpx_cfg.mock_data_freq

        self._log.info(f"Sending mock data at {fpx_cfg.mock_data_freq} Hz")

        while True:
            await self.mqtt.publish(
                mqtt_cfg.gps_position_topic,
                GpsLatlon(
                    lat=self.latlon[0], lon=self.latlon[1], gps_qual=self.gps_qual
                )._asdict(),
            )

            await self.mqtt.publish(
                mqtt_cfg.gps_direction_topic,
                GpsHeading(heading=self.heading)._asdict(),
            )

            await asyncio.sleep(delay)

    async def _receive(self) -> None:
        """receive gps messages"""

        fpx_cfg = FPX_Config()
        mqtt_cfg = MqttConfig()

        # receiver task will put messages into self._msg_q
        _ = asyncio.create_task(receive(fpx_cfg.host, fpx_cfg.port, self._msg_q))

        while True:

            msg = await self._msg_q.get()

            # parse message
            try:
                parsed = parse(msg.decode(), ignore=["ODOM"])
                if parsed is None:
                    continue

                self.last_update = time.time()
                self._log.debug(f"parsed: {parsed}")

                # handle parsed message
                if isinstance(parsed, GgaData):
                    self.latlon = (parsed.lat, parsed.lon)
                    self.gps_qual = parsed.quality

                    await self.mqtt.publish(
                        mqtt_cfg.gps_position_topic,
                        GpsLatlon(
                            lat=parsed.lat, lon=parsed.lon, gps_qual=parsed.quality
                        )._asdict(),
                    )
                elif isinstance(parsed, HdtData):
                    self.heading = parsed.heading

                    await self.mqtt.publish(
                        mqtt_cfg.gps_direction_topic,
                        GpsHeading(heading=parsed.heading)._asdict(),
                    )

            except ValueError as e:
                self._log.warning(f"Failed to parse message: {e}")
                self.nr_warnings += 1
            except NotImplementedError as e:
                self._log.warning(f"Failed to publish to mqtt: {e}")
                self.nr_errors += 1
