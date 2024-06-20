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
from roxbot.interfaces import Pose


class FPX_Config(BaseSettings):
    """Fixposition related settings"""

    model_config = SettingsConfigDict(env_prefix="fpx_")

    host: str = "localhost"
    port: int = 21000


class FpxNode(Node):
    """interface to gps data, works in latitude and longitude."""

    def __init__(self) -> None:
        super().__init__()

        self.latlon = (0.0, 0.0)
        self.heading = 0.0
        self.gps_qual = 0
        self.last_update = time.time()

        self._msg_q: asyncio.Queue[bytes] = asyncio.Queue()

        self._coros.append(self._receive)

    def get_pose(self, max_age: float = 1.0) -> Pose:
        """returns pose or raises FixException if data is too old"""
        if time.time() - self.last_update > max_age:
            raise FixException(FixProblem.OLD_FIX)

        # if self.gps_qual != 4:
        #     raise FixException(FixProblem.NO_RTK_FIX)

        return Pose.from_gps(self.latlon[0], self.latlon[1], self.heading)

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
                        mqtt_cfg.gps_position_topic, parsed.to_mqtt()
                    )
                elif isinstance(parsed, HdtData):
                    self.heading = parsed.heading
                    await self.mqtt.publish(
                        mqtt_cfg.gps_direction_topic, parsed.to_mqtt()
                    )

            except ValueError as e:
                self._log.warning(f"Failed to parse message: {e}")
                self.nr_warnings += 1
            except NotImplementedError as e:
                self._log.warning(f"Failed to publish to mqtt: {e}")
                self.nr_errors += 1


# ----------------demo code


async def demo() -> None:

    async def show_pose(gps: FpxNode) -> None:
        """show current pose"""
        while True:
            pose = gps.get_pose()
            print(f"pose: {pose}")
            await asyncio.sleep(1)

    gps = FpxNode()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(gps.main())
        tg.create_task(show_pose(gps))


if __name__ == "__main__":
    # simple standalone demo code
    from roxbot.utils import run_main_async

    run_main_async(demo())
