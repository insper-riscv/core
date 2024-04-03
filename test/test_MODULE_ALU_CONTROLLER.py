import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_RV32I_ALU_CONTROLLER import RV32I_ALU_CONTROLLER


class MODULE_ALU_CONTROLLER(utils.DUT):
    opcode = utils.DUT.Input_pin
    function_3 = utils.DUT.Input_pin
    function_7 = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    alu_controller = RV32I_ALU_CONTROLLER


@MODULE_ALU_CONTROLLER.testcase
async def tb_MODULE_ALU_CONTROLLER_case_1(dut: "MODULE_ALU_CONTROLLER", trace: utils.Trace):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("111")
    dut.function_7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")

    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "0010")

    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0100000")

    await trace.cycle()
    yield trace.check(dut.destination, "0110")


def test_MODULE_ALU_CONTROLLER_synthesis():
    MODULE_ALU_CONTROLLER.build_vhd()
    # MODULE_ALU_CONTROLLER.build_netlistsvg()


def test_MODULE_ALU_CONTROLLER_testcases():
    MODULE_ALU_CONTROLLER.test_with(
        [
            tb_MODULE_ALU_CONTROLLER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
