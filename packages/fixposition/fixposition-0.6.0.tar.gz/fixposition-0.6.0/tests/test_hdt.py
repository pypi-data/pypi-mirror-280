""" " nmea hdt message"""

from fixposition import parser
from fixposition.messages import hdt

TEST_MSG = "$GPHDT,61.7,T*05\r\n"


def test_parsing() -> None:
    expected = hdt.Data(heading=61.7, true_ind="T")
    msg = parser.parse(TEST_MSG)
    assert isinstance(msg, hdt.Data)
    assert msg == expected
