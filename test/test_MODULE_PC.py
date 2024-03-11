from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_PC(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1, GENERIC_REGISTER, GENERIC_ADDER]


def test_MODULE_PC_syntesis():
    MODULE_PC.build_vhd()
    MODULE_PC.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_PC"])
