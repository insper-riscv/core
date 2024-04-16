import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_RV32I_package import RV32I


class RV32I_ALU_CONTROLLER(utils.DUT):
    _package = RV32I

    opcode = utils.DUT.Input_pin
    funct3 = utils.DUT.Input_pin
    funct7 = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@RV32I_ALU_CONTROLLER.testcase
async def tb_RV32I_ALU_CONTROLLER_case_1(dut: "RV32I_ALU_CONTROLLER", trace: utils.Trace):
    dut.opcode.value = BinaryValue("01100")
    dut.funct3.value = BinaryValue("111")
    dut.funct7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000")

    dut.funct3.value = BinaryValue("110")

    await trace.cycle()
    yield trace.check(dut.destination, "00001")

    dut.funct3.value = BinaryValue("000")
    dut.funct7.value = BinaryValue("0100000")

    await trace.cycle()
    yield trace.check(dut.destination, "01011")

    dut.funct7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00011")


@pytest.mark.synthesis
def test_RV32I_ALU_CONTROLLER_synthesis():
    RV32I_ALU_CONTROLLER.build_vhd()
    # RV32I_ALU_CONTROLLER.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_CONTROLLER_testcases():
    RV32I_ALU_CONTROLLER.test_with(
        [
            tb_RV32I_ALU_CONTROLLER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
