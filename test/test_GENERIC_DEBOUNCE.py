import pytest

import lib
from test_GENERICS_package import GENERICS
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_DEBOUNCE(lib.Device):
    _package = GENERICS

    edge_detector = GENERIC_EDGE_DETECTOR
    state_register = GENERIC_FLIP_FLOP


@pytest.mark.synthesis
def test_GENERIC_DEBOUNCE_synthesis():
    GENERIC_DEBOUNCE.build_vhd()
    # GENERIC_DEBOUNCE.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
