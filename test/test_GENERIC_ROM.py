from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_EDGE_DETECTOR import GENERIC_EDGE_DETECTOR
from test_GENERIC_FLIP_FLOP import GENERIC_FLIP_FLOP


class GENERIC_ROM(utils.DUT):
    address: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


def test_GENERIC_ROM_syntesis():
    GENERIC_ROM.build_vhd()
    GENERIC_ROM.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_GENERIC_ROM"])
