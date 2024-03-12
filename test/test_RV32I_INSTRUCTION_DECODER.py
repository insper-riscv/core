from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_INSTRUCTION_DECODER(utils.DUT):
    instruction: utils.DUT.Input_pin
    control_if: utils.DUT.Output_pin
    control_id: utils.DUT.Output_pin
    control_ex: utils.DUT.Output_pin
    control_mem: utils.DUT.Output_pin
    control_wb: utils.DUT.Output_pin
    immediate: utils.DUT.Output_pin


def test_RV32I_INSTRUCTION_DECODER_synthesis():
    RV32I_INSTRUCTION_DECODER.build_vhd()
    RV32I_INSTRUCTION_DECODER.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_RV32I_INSTRUCTION_DECODER"])
