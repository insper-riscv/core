import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_ALU_BIT import RV32I_ALU_BIT


class RV32I_ALU(utils.DUT):
    CHILDREN = [RV32I_ALU_BIT]
    invert_source_1: utils.DUT.Input_pin
    invert_source_2: utils.DUT.Input_pin
    select_function: utils.DUT.Input_pin
    source_1: utils.DUT.Input_pin
    source_2: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_RV32I_ALU_case_1(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("00")
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000000000000000000000000000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_2(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("01")
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111111111111111111111111111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_3(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("10")
    dut.source_1.value = BinaryValue("11111111111111110000000000000000")
    dut.source_2.value = BinaryValue("00000000000000001111111111111111")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111111111111111111111111111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_4(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("11")
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000000000000000000000000001")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_5(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("00")
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111111111111111111111111111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_6(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("1")
    dut.select_function.value = BinaryValue("01")
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111111111111111111111111111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_7(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("10")
    dut.source_1.value = BinaryValue("11111111111111110000000000000000")
    dut.source_2.value = BinaryValue("11111111111111110000000000000000")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000000000000000000000000000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_case_8(dut: RV32I_ALU):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("1")
    dut.select_function.value = BinaryValue("11")
    dut.source_1.value = BinaryValue("11111111111111111111111111111111")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000000000000000000000000001")
    await Timer(Decimal(1), units="ns")


def test_RV32I_ALU_synthesis():
    RV32I_ALU.build_vhd()
    # RV32I_ALU.build_netlistsvg()


def test_RV32I_ALU_testcases():
    RV32I_ALU.test_with(
        [
            tb_RV32I_ALU_case_1,
            tb_RV32I_ALU_case_2,
            tb_RV32I_ALU_case_3,
            tb_RV32I_ALU_case_4,
            tb_RV32I_ALU_case_5,
            tb_RV32I_ALU_case_6,
            tb_RV32I_ALU_case_7,
            tb_RV32I_ALU_case_8,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
