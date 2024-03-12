from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_ROM import GENERIC_ROM


class MODULE_ROM(utils.DUT):
    CHILDREN = [GENERIC_ROM]


def test_MODULE_ROM_synthesis():
    MODULE_ROM.build_vhd()
    #MODULE_ROM.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_ROM"])
