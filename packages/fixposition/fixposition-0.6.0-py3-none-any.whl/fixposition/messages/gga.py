"""nmea gga message
https://docs.fixposition.com/fd/nmea-gp-gga
"""

from typing import NamedTuple
from roxbot.gps.converters import parse_nmea_lat, parse_nmea_lon
from roxbot.config import PrecisionConfig

from fixposition.utils import timestamp
from fixposition.checksum import validate_checksum

PREC_CFG = PrecisionConfig()


class Data(NamedTuple):
    time: str
    lat: float
    lat_ns: str
    lon: float
    lon_ew: str
    quality: int
    num_sv: int
    hdop: float
    alt: float
    alt_unit: str
    sep: str  # Always null as per your notes, so it could be Optional[str] or just str with a note it's unused.
    sep_unit: str  # Same note as 'sep'
    diff_age: float
    diff_sta: str


@validate_checksum
def parse(message: str) -> Data:
    # Split the message to exclude the start '$', checksum, and end characters
    data_part = message[1 : message.index("*")]

    # Split the message fields
    fields = data_part.split(",")

    return Data(
        time=fields[1],
        lat=round(parse_nmea_lat(fields[2]), PREC_CFG.latlon),
        lat_ns=fields[3],
        lon=round(parse_nmea_lon(fields[4]), PREC_CFG.latlon),
        lon_ew=fields[5],
        quality=int(fields[6]),
        num_sv=int(fields[7]),
        hdop=float(fields[8]),
        alt=float(fields[9]),
        alt_unit=fields[10],
        sep=fields[11],  # Always null, kept for completeness
        sep_unit=fields[12],  # Always null, kept for completeness
        diff_age=(
            float(fields[13]) if fields[13] else 0.0
        ),  # Handling possible null values
        diff_sta=fields[14],
    )
