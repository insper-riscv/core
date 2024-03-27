import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1
from test_RV32I_ALU import RV32I_ALU


class MODULE_ALU(utils.DUT):
    select_source_1 = utils.DUT.Input_pin
    select_source_2 = utils.DUT.Input_pin
    address_program = utils.DUT.Input_pin
    data_source_1 = utils.DUT.Input_pin
    data_source_2 = utils.DUT.Input_pin
    data_immediate = utils.DUT.Input_pin
    select_function = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    mux_register_alu_1 = GENERIC_MUX_4X1
    mux_register_alu_2 = GENERIC_MUX_4X1
    alu = RV32I_ALU


@MODULE_ALU.testcase
async def tb_MODULE_ALU_case_1(dut: "MODULE_ALU", trace: utils.Trace):
    dut.select_source_1.value = BinaryValue("10")
    dut.select_source_2.value = BinaryValue("01")
    dut.address_program.value = BinaryValue("11111111111111111111111111111111")
    dut.data_source_1.value = BinaryValue("10101010101010101010101010101010")
    dut.data_source_2.value = BinaryValue("01010101010101010101010101010101")
    dut.data_immediate.value = BinaryValue("00000000000000000001000000000000")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000001000000000000")

    dut.select_source_1.value = BinaryValue("01")
    dut.select_source_2.value = BinaryValue("10")
    dut.address_program.value = BinaryValue("00000000000000000000000000000000")
    dut.data_source_1.value = BinaryValue("10101010101010101010101010101010")
    dut.data_source_2.value = BinaryValue("01010101010101010101010101010101")
    dut.data_immediate.value = BinaryValue("00000000000000000001000000000000")
    dut.select_function.value = BinaryValue("0001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000100")


def test_MODULE_ALU_synthesis():
    MODULE_ALU.build_vhd()
    # MODULE_ALU.build_netlistsvg()


def test_MODULE_ALU_testcases():
    MODULE_ALU.test_with(
        [
            tb_MODULE_ALU_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
