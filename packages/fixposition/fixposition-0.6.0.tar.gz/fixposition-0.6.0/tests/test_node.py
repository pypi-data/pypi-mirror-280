import pytest
import time

from roxbot.interfaces import Pose
from roxbot.gps import converters
from roxbot.exceptions import FixException
from fixposition.gps_node import FpxNode

# make sure gps refecence is set
converters.set_gps_ref(52.0, 4.0)


@pytest.fixture
def fpx_node() -> FpxNode:
    return FpxNode()


def test_get_pose(fpx_node: FpxNode) -> None:
    fpx_node.latlon = (52.0, 4.0)
    fpx_node.heading = 90.0
    fpx_node.last_update = time.time()
    fpx_node.gps_qual = 1

    pose = fpx_node.get_pose()

    assert isinstance(pose, Pose)


def test_get_pose_old_fix(fpx_node: FpxNode) -> None:
    fpx_node.last_update = time.time() - 10  # Simulate old data
    with pytest.raises(FixException):
        fpx_node.get_pose(max_age=1.0)
