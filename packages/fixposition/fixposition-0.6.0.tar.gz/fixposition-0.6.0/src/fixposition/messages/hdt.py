"""nmea hdt message
https://docs.fixposition.com/fd/nmea-gp-hdt
"""

from fixposition.checksum import validate_checksum
from typing import NamedTuple

from roxbot.config import PrecisionConfig

PREC_CFG = PrecisionConfig()


class Data(NamedTuple):
    heading: float
    true_ind: str


@validate_checksum
def parse(message: str) -> Data:
    # Split the message to exclude the start '$', checksum, and end characters
    data_part = message[1 : message.index("*")]

    # Split the message fields
    fields = data_part.split(",")

    return Data(heading=round(float(fields[1]), PREC_CFG.angle), true_ind=fields[2])
