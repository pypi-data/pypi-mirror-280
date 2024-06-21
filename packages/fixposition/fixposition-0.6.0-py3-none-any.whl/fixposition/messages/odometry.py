"""parse FPA_A-ODOMETRY"""

from typing import NamedTuple
from fixposition.checksum import validate_checksum


class Data(NamedTuple):
    msg_type: str
    msg_version: int
    gps_week: int
    gps_tow: float
    pos_x: float
    pos_y: float
    pos_z: float
    orientation_w: float
    orientation_x: float
    orientation_y: float
    orientation_z: float
    vel_x: float
    vel_y: float
    vel_z: float
    rot_x: float
    rot_y: float
    rot_z: float
    acc_x: float
    acc_y: float
    acc_z: float
    fusion_status: int
    imu_bias_status: int
    gnss1_fix: int
    gnss2_fix: int
    wheelspeed_status: int
    pos_cov_xx: float
    pos_cov_yy: float
    pos_cov_zz: float
    pos_cov_xy: float
    pos_cov_yz: float
    pos_cov_xz: float
    orientation_cov_xx: float
    orientation_cov_yy: float
    orientation_cov_zz: float
    orientation_cov_xy: float
    orientation_cov_yz: float
    orientation_cov_xz: float
    vel_cov_xx: float
    vel_cov_yy: float
    vel_cov_zz: float
    vel_cov_xy: float
    vel_cov_yz: float
    vel_cov_xz: float
    sw_version: str


@validate_checksum
def parse(message: str) -> Data:
    data_part, _ = message.split("*")
    fields = data_part[1:].split(",")

    return Data(
        msg_type=fields[1],
        msg_version=int(fields[2]),
        gps_week=int(fields[3]),
        gps_tow=float(fields[4]),
        pos_x=float(fields[5]),
        pos_y=float(fields[6]),
        pos_z=float(fields[7]),
        orientation_w=float(fields[8]),
        orientation_x=float(fields[9]),
        orientation_y=float(fields[10]),
        orientation_z=float(fields[11]),
        vel_x=float(fields[12]),
        vel_y=float(fields[13]),
        vel_z=float(fields[14]),
        rot_x=float(fields[15]),
        rot_y=float(fields[16]),
        rot_z=float(fields[17]),
        acc_x=float(fields[18]),
        acc_y=float(fields[19]),
        acc_z=float(fields[20]),
        fusion_status=int(fields[21]),
        imu_bias_status=int(fields[22]),
        gnss1_fix=int(fields[23]),
        gnss2_fix=int(fields[24]),
        wheelspeed_status=int(fields[25]),
        pos_cov_xx=float(fields[26]),
        pos_cov_yy=float(fields[27]),
        pos_cov_zz=float(fields[28]),
        pos_cov_xy=float(fields[29]),
        pos_cov_yz=float(fields[30]),
        pos_cov_xz=float(fields[31]),
        orientation_cov_xx=float(fields[32]),
        orientation_cov_yy=float(fields[33]),
        orientation_cov_zz=float(fields[34]),
        orientation_cov_xy=float(fields[35]),
        orientation_cov_yz=float(fields[36]),
        orientation_cov_xz=float(fields[37]),
        vel_cov_xx=float(fields[38]),
        vel_cov_yy=float(fields[39]),
        vel_cov_zz=float(fields[40]),
        vel_cov_xy=float(fields[41]),
        vel_cov_yz=float(fields[42]),
        vel_cov_xz=float(fields[43]),
        sw_version=fields[44],
    )
