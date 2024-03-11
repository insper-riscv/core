from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_DEBOUNCE(utils.DUT):
    CHILDREN = [GENERIC_EDGE_DETECTOR, GENERIC_FLIP_FLOP]


def test_GENERIC_DEBOUNCE_syntesis():
    GENERIC_DEBOUNCE.build_vhd()
    GENERIC_DEBOUNCE.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_GENERIC_DEBOUNCE"])
