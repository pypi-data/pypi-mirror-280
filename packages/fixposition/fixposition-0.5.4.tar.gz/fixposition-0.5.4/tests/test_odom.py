import pytest
from fixposition import parser
from fixposition.messages import odometry
from fixposition.checksum import check_checksum

TEST_MSG = "$FP,ODOMETRY,2,2231,227610.750000,4279243.1641,635824.2171,4671589.8683,-0.412792,0.290804,-0.123898,0.854216,-17.1078,-0.0526,-0.3252,0.02245,0.00275,0.10369,-1.0385,-1.3707,9.8249,4,1,8,8,1,0.01761,0.02274,0.01713,-0.00818,0.00235,0.00129,0.00013,0.00015,0.00014,-0.00001,0.00001,0.00002,0.03482,0.06244,0.05480,0.00096,0.00509,0.00054,fp_release_vr2_2.54.0_160*4F\r\n"


def test_checksum() -> None:
    check_checksum(TEST_MSG)

    # removed checksum
    with pytest.raises(ValueError):
        check_checksum(TEST_MSG[:-5])

    # change a character in the message
    with pytest.raises(ValueError):
        check_checksum(TEST_MSG.replace("F", "G"))


def test_odometry_message() -> None:
    msg = parser.parse(TEST_MSG)

    assert isinstance(msg, odometry.Data)
    assert msg.msg_type == "ODOMETRY"
    assert msg.msg_version == 2
    assert msg.gps_week == 2231
    assert msg.gps_tow == 227610.750000
    assert msg.pos_x == 4279243.1641
    assert msg.pos_y == 635824.2171
    assert msg.pos_z == 4671589.8683
    assert msg.orientation_w == -0.412792
    assert msg.orientation_x == 0.290804
    assert msg.orientation_y == -0.123898
    assert msg.orientation_z == 0.854216
    assert msg.vel_x == -17.1078
    assert msg.vel_y == -0.0526
    assert msg.vel_z == -0.3252
    assert msg.rot_x == 0.02245
    assert msg.rot_y == 0.00275
    assert msg.rot_z == 0.10369
    assert msg.acc_x == -1.0385
    assert msg.acc_y == -1.3707
    assert msg.acc_z == 9.8249
    assert msg.fusion_status == 4
    assert msg.imu_bias_status == 1
    assert msg.gnss1_fix == 8
    assert msg.gnss2_fix == 8
    assert msg.wheelspeed_status == 1
    assert msg.pos_cov_xx == 0.01761
    assert msg.pos_cov_yy == 0.02274
    assert msg.pos_cov_zz == 0.01713
    assert msg.pos_cov_xy == -0.00818
    assert msg.pos_cov_yz == 0.00235
    assert msg.pos_cov_xz == 0.00129
    assert msg.orientation_cov_xx == 0.00013
    assert msg.orientation_cov_yy == 0.00015
    assert msg.orientation_cov_zz == 0.00014
    assert msg.orientation_cov_xy == -0.00001
    assert msg.orientation_cov_yz == 0.00001
    assert msg.orientation_cov_xz == 0.00002
    assert msg.vel_cov_xx == 0.03482
    assert msg.vel_cov_yy == 0.06244
    assert msg.vel_cov_zz == 0.05480
    assert msg.vel_cov_xy == 0.00096
    assert msg.vel_cov_yz == 0.00509
    assert msg.vel_cov_xz == 0.00054
    assert msg.sw_version == "fp_release_vr2_2.54.0_160"
