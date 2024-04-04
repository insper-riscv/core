import os

import pytest

import utils
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_DEBOUNCE(utils.DUT):
    edge_detector = GENERIC_EDGE_DETECTOR
    state_register = GENERIC_FLIP_FLOP


def test_GENERIC_DEBOUNCE_synthesis():
    GENERIC_DEBOUNCE.build_vhd()
    # GENERIC_DEBOUNCE.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
