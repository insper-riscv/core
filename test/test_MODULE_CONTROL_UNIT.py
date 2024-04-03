import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_RV32I_INSTRUCTION_DECODER import RV32I_INSTRUCTION_DECODER
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_CONTROL_UNIT(utils.DUT):
    instruction = utils.DUT.Input_pin
    address_program = utils.DUT.Input_pin
    data_source_1 = utils.DUT.Input_pin
    jump_address = utils.DUT.Output_pin
    immediate_source = utils.DUT.Output_pin
    control_if = utils.DUT.Output_pin
    control_ex = utils.DUT.Output_pin
    control_mem = utils.DUT.Output_pin
    control_wb = utils.DUT.Output_pin

    control_unit =  RV32I_INSTRUCTION_DECODER
    adder_1 = GENERIC_ADDER
    adder_2 = GENERIC_ADDER
    mux = GENERIC_MUX_2X1


@MODULE_CONTROL_UNIT.testcase
async def tb_MODULE_CONTROL_UNIT_case_1(dut: "MODULE_CONTROL_UNIT", trace: utils.Trace):
    dut.instruction.value = BinaryValue("00000000000000000001010000110111")
    dut.address_program.value = BinaryValue("00000000000000000000000000000000")
    dut.data_source_1.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.immediate_source, "00000000000000000001000000000000")


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
