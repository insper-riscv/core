from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1
from test_RV32I_ALU_CONTROLLER import RV32I_ALU_CONTROLLER
from test_RV32I_ALU import RV32I_ALU


class MODULE_ALU(utils.DUT):
    CHILDREN = [GENERIC_MUX_4X1, GENERIC_MUX_4X1, RV32I_ALU, RV32I_ALU_CONTROLLER]


def test_MODULE_ALU_syntesis():
    MODULE_ALU.build_vhd()
    MODULE_ALU.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_ALU"])
