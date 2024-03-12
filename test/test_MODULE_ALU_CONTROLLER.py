from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_ALU_CONTROLLER import RV32I_ALU_CONTROLLER


class MODULE_ALU_CONTROLLER(utils.DUT):
    CHILDREN = [RV32I_ALU_CONTROLLER]
    opcode     : utils.DUT.Input_pin
    function_3 : utils.DUT.Input_pin
    function_7 : utils.DUT.Input_pin
    destination: utils.DUT.Output_pin

@cocotb.test()
async def tb_MODULE_ALU_CONTROLLER_case_1(dut: "MODULE_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("111")
    dut.function_7.value = BinaryValue("0000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0000")

    await Timer(Decimal(1), units="ns")

@cocotb.test()
async def tb_MODULE_ALU_CONTROLLER_case_2(dut: "MODULE_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0010")

    await Timer(Decimal(1), units="ns")

@cocotb.test()
async def tb_MODULE_ALU_CONTROLLER_case_3(dut: "MODULE_ALU_CONTROLLER"):
    dut.opcode.value = BinaryValue("01100")
    dut.function_3.value = BinaryValue("000")
    dut.function_7.value = BinaryValue("0100000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "0110")

    await Timer(Decimal(1), units="ns")

def test_MODULE_ALU_CONTROLLER_syntesis():
    MODULE_ALU_CONTROLLER.build_vhd()
    #MODULE_ALU_CONTROLLER.build_netlistsvg()

def test_MODULE_ALU_CONTROLLER_case_1():
    MODULE_ALU_CONTROLLER.test_with(tb_MODULE_ALU_CONTROLLER_case_1)

def test_MODULE_ALU_CONTROLLER_case_2():
    MODULE_ALU_CONTROLLER.test_with(tb_MODULE_ALU_CONTROLLER_case_2)

def test_MODULE_ALU_CONTROLLER_case_3():
    MODULE_ALU_CONTROLLER.test_with(tb_MODULE_ALU_CONTROLLER_case_3)

if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_ALU_CONTROLLER"])
