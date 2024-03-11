from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_WRITE_BACK(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1]


def test_MODULE_WRITE_BACK_syntesis():
    MODULE_WRITE_BACK.build_vhd()
    MODULE_WRITE_BACK.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_WRITE_BACK"])
