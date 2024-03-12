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


@cocotb.test()
async def tb_RV32I_ALU_CONTROLLER_case_1(dut: "RV32I_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("111")
    dut.function_7.value = BinaryValue("0000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0000")

    await Timer(Decimal(1), units="ns")

@cocotb.test()
async def tb_RV32I_ALU_CONTROLLER_case_2(dut: "RV32I_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("110")
    dut.function_7.value = BinaryValue("0000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0001")

    await Timer(Decimal(1), units="ns")

@cocotb.test()
async def tb_RV32I_ALU_CONTROLLER_case_3(dut: "RV32I_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0100000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0110")

    await Timer(Decimal(1), units="ns")

@cocotb.test()
async def tb_RV32I_ALU_CONTROLLER_case_4(dut: "RV32I_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0010")

    await Timer(Decimal(1), units="ns")


def test_RV32I_ALU_CONTROLLER_synthesis():
    RV32I_ALU_CONTROLLER.build_vhd()
    #RV32I_ALU_CONTROLLER.build_netlistsvg()


def test_RV32I_ALU_CONTROLLER_case_1():
    RV32I_ALU_CONTROLLER.test_with(tb_RV32I_ALU_CONTROLLER_case_1)

def test_RV32I_ALU_CONTROLLER_case_2():
    RV32I_ALU_CONTROLLER.test_with(tb_RV32I_ALU_CONTROLLER_case_2)

def test_RV32I_ALU_CONTROLLER_case_3():
    RV32I_ALU_CONTROLLER.test_with(tb_RV32I_ALU_CONTROLLER_case_3)

def test_RV32I_ALU_CONTROLLER_case_4():
    RV32I_ALU_CONTROLLER.test_with(tb_RV32I_ALU_CONTROLLER_case_4)


if __name__ == "__main__":
    pytest.main(["-k", f"test_RV32I_ALU_CONTROLLER"])
