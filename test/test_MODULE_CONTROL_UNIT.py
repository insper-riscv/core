from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_INSTRUCTION_DECODER import RV32I_INSTRUCTION_DECODER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_CONTROL_UNIT(utils.DUT):
    CHILDREN = [RV32I_INSTRUCTION_DECODER, GENERIC_ADDER, GENERIC_MUX_2X1]


def test_MODULE_CONTROL_UNIT_syntesis():
    MODULE_CONTROL_UNIT.build_vhd()
    MODULE_CONTROL_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_CONTROL_UNIT"])
