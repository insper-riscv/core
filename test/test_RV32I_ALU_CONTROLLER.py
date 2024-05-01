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
    dut.opcode.value = BinaryValue("00100")
    dut.funct3.value = BinaryValue("000")
    dut.funct7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")

    dut.funct3.value = BinaryValue("001")

    await trace.cycle()
    yield trace.check(dut.destination, "0001")

    dut.funct3.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "0100")

    dut.funct3.value = BinaryValue("000")
    dut.funct7.value = BinaryValue("0100000")

    await trace.cycle()
    yield trace.check(dut.destination, "1000")

    dut.funct3.value = BinaryValue("001")

    await trace.cycle()
    yield trace.check(dut.destination, "1001")

    dut.funct3.value = BinaryValue("010")

    await trace.cycle()
    yield trace.check(dut.destination, "1010")

    dut.funct3.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "1100")

    dut.opcode.value = BinaryValue("01100")
    dut.funct3.value = BinaryValue("000")
    dut.funct7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")

    dut.funct3.value = BinaryValue("001")

    await trace.cycle()
    yield trace.check(dut.destination, "0001")

    dut.funct3.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "0100")

    dut.funct3.value = BinaryValue("000")
    dut.funct7.value = BinaryValue("0100000")

    await trace.cycle()
    yield trace.check(dut.destination, "1000")

    dut.funct3.value = BinaryValue("001")

    await trace.cycle()
    yield trace.check(dut.destination, "1001")

    dut.funct3.value = BinaryValue("010")

    await trace.cycle()
    yield trace.check(dut.destination, "1010")

    dut.funct3.value = BinaryValue("100")

    await trace.cycle()
    yield trace.check(dut.destination, "1100")

    dut.opcode.value = BinaryValue("00000")
    dut.funct3.value = BinaryValue("XXX")
    dut.funct7.value = BinaryValue("XXXXXXX")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")

    dut.opcode.value = BinaryValue("01000")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")

    dut.opcode.value = BinaryValue("XXXXX")

    await trace.cycle()
    yield trace.check(dut.destination, "0110")

    dut.opcode.value = BinaryValue("11100")

    await trace.cycle()
    yield trace.check(dut.destination, "0000")


@pytest.mark.synthesis
def test_RV32I_ALU_CONTROLLER_synthesis():
    RV32I_ALU_CONTROLLER.build_vhd()
    RV32I_ALU_CONTROLLER.build_netlistsvg()


@pytest.mark.testcases
def test_RV32I_ALU_CONTROLLER_testcases():
    RV32I_ALU_CONTROLLER.test_with(
        [
            tb_RV32I_ALU_CONTROLLER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
