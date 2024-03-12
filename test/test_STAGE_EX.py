from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_ALU import MODULE_ALU
from test_MODULE_ALU_CONTROLLER import MODULE_ALU_CONTROLLER


class STAGE_EX(utils.DUT):
    CHILDREN = [MODULE_ALU, MODULE_ALU_CONTROLLER]


def test_STAGE_EX_synthesis():
    STAGE_EX.build_vhd()
    #STAGE_EX.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_STAGE_EX"])
