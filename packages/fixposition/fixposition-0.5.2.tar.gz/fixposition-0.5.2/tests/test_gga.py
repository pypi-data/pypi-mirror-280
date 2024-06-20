import pytest
from pytest import approx
import pynmea2
from fixposition import parser
from fixposition.checksum import check_checksum
from fixposition.messages.gga import Data


TEST_MSG = "$GPGGA,090411.2001,4724.0179046,N,00827.0219436,E,4,30,99.99,459.4117,M,,,0.4,0000*28\r\n"

NMEA = pynmea2.parse(TEST_MSG.strip())

REF_DATA = Data(
    time="090411.2001",
    lat=NMEA.latitude,
    lat_ns="N",
    lon=NMEA.longitude,
    lon_ew="E",
    quality=4,
    num_sv=30,
    hdop=99.99,
    alt=459.4117,
    alt_unit="M",
    sep="",  # Assuming null values are represented as empty strings
    sep_unit="",
    diff_age=0.4,  # Assuming a default value of 0.0 for null, but the message has 0.4
    diff_sta="0000",
)


def test_checksum() -> None:
    check_checksum(TEST_MSG)

    # removed checksum
    with pytest.raises(ValueError):
        check_checksum(TEST_MSG[:-5])

    # change a character in the message
    with pytest.raises(ValueError):
        check_checksum(TEST_MSG.replace("E", "X"))


def test_parse_gga() -> None:

    msg = parser.parse(TEST_MSG)
    assert isinstance(msg, Data)

    for field in ["lat", "lon", "alt"]:
        assert getattr(msg, field) == approx(getattr(REF_DATA, field))
