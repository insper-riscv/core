import os

import pytest
from cocotb.binary import BinaryValue

import utils


class RV32I_ALU_CONTROLLER(utils.DUT):
    opcode = utils.DUT.Input_pin
    function_3 = utils.DUT.Input_pin
    function_7 = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@RV32I_ALU_CONTROLLER.testcase
async def tb_RV32I_ALU_CONTROLLER_case_1(dut: "RV32I_ALU_CONTROLLER", trace: utils.Trace):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("111")
    dut.function_7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")

    dut.function_3.value = BinaryValue("110")

    await trace.cycle()
    yield trace.check(dut.destination, "0001")

    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0100000")

    await trace.cycle()
    yield trace.check(dut.destination, "0110")

    dut.function_7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "0010")


def test_RV32I_ALU_CONTROLLER_synthesis():
    RV32I_ALU_CONTROLLER.build_vhd()
    # RV32I_ALU_CONTROLLER.build_netlistsvg()


def test_RV32I_ALU_CONTROLLER_testcases():
    RV32I_ALU_CONTROLLER.test_with(
        [
            tb_RV32I_ALU_CONTROLLER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
