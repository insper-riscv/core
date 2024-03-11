from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_ALU_CONTROLLER import RV32I_ALU_CONTROLLER


class MODULE_ALU_CONTROLLER(utils.DUT):
    CHILDREN = [RV32I_ALU_CONTROLLER]


def test_MODULE_ALU_CONTROLLER_syntesis():
    MODULE_ALU_CONTROLLER.build_vhd()
    MODULE_ALU_CONTROLLER.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_ALU_CONTROLLER"])
