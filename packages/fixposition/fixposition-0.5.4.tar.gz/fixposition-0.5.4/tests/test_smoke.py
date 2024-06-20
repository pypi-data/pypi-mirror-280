# type: ignore
# pylint:n disable=unused-import
""" basic smoke tests for the package """


def test_imports():

    from fixposition import cli
    from fixposition import receiver
    from fixposition import replay
    from fixposition import recorder
    from fixposition import test_data
    from fixposition.gps_node import FpxNode

    FpxNode()
