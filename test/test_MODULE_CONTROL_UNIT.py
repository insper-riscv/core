import os
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
    instruction: utils.DUT.Input_pin
    pc_out: utils.DUT.Input_pin
    data_source_1: utils.DUT.Input_pin
    immediate_source: utils.DUT.Output_pin
    control_if: utils.DUT.Output_pin
    control_ex: utils.DUT.Output_pin
    control_mem: utils.DUT.Output_pin
    control_wb: utils.DUT.Output_pin


@cocotb.test()
async def tb_MODULE_CONTROL_UNIT_case_1(dut: "MODULE_CONTROL_UNIT"):
    dut.instruction.value = BinaryValue("00000000000000000001010000110111")
    dut.pc_out.value = BinaryValue("00000000000000000000000000000000")
    dut.data_source_1.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.immediate_source, "00000000000000000001000000000000")

    await Timer(Decimal(1), units="ns")


def test_MODULE_CONTROL_UNIT_synthesis():
    MODULE_CONTROL_UNIT.build_vhd()
    # MODULE_CONTROL_UNIT.build_netlistsvg()


def test_MODULE_CONTROL_UNIT_testcases():
    MODULE_CONTROL_UNIT.test_with(
        [
            tb_MODULE_CONTROL_UNIT_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
