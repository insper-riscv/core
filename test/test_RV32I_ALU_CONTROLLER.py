from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_ALU_CONTROLLER(utils.DUT):
    opcode: utils.DUT.Input_pin
    function_3: utils.DUT.Input_pin
    function_7: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


def test_RV32I_ALU_CONTROLLER_syntesis():
    RV32I_ALU_CONTROLLER.build_vhd()
    RV32I_ALU_CONTROLLER.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_RV32I_ALU_CONTROLLER"])
