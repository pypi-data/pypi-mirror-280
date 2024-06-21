import pytest
from fixposition import parser


def test_unknown_msg() -> None:

    res = parser.parse("$FP,UNKNOWN,*4F\r\n")
    assert res is None
