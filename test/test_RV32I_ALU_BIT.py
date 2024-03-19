import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_ALU_BIT(utils.DUT):
    invert_source_1 = utils.DUT.Input_pin
    invert_source_2 = utils.DUT.Input_pin
    select_function = utils.DUT.Input_pin
    carry_in = utils.DUT.Input_pin
    slt = utils.DUT.Input_pin
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin
    carry_out = utils.DUT.Output_pin
    overflow = utils.DUT.Output_pin


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_1(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("00")
    dut.carry_in.value = BinaryValue("0")
    dut.slt.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "0")
    utils.assert_output(dut.carry_out, "0")
    utils.assert_output(dut.overflow, "1")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_2(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("01")
    dut.carry_in.value = BinaryValue("0")
    dut.slt.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "1")
    utils.assert_output(dut.carry_out, "0")
    utils.assert_output(dut.overflow, "1")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_3(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("10")
    dut.carry_in.value = BinaryValue("1")
    dut.slt.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "0")
    utils.assert_output(dut.carry_out, "1")
    utils.assert_output(dut.overflow, "0")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_4(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("0")
    dut.invert_source_2.value = BinaryValue("0")
    dut.select_function.value = BinaryValue("11")
    dut.carry_in.value = BinaryValue("1")
    dut.slt.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "1")
    utils.assert_output(dut.carry_out, "1")
    utils.assert_output(dut.overflow, "0")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_5(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("1")
    dut.select_function.value = BinaryValue("00")
    dut.carry_in.value = BinaryValue("0")
    dut.slt.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "0")
    utils.assert_output(dut.carry_out, "0")
    utils.assert_output(dut.overflow, "1")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_6(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("1")
    dut.select_function.value = BinaryValue("01")
    dut.carry_in.value = BinaryValue("0")
    dut.slt.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "1")
    utils.assert_output(dut.carry_out, "0")
    utils.assert_output(dut.overflow, "1")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_7(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("1")
    dut.select_function.value = BinaryValue("10")
    dut.carry_in.value = BinaryValue("1")
    dut.slt.value = BinaryValue("0")
    dut.source_1.value = BinaryValue("0")
    dut.source_2.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "0")
    utils.assert_output(dut.carry_out, "1")
    utils.assert_output(dut.overflow, "0")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_RV32I_ALU_BIT_case_8(dut: RV32I_ALU_BIT):
    dut.invert_source_1.value = BinaryValue("1")
    dut.invert_source_2.value = BinaryValue("1")
    dut.select_function.value = BinaryValue("11")
    dut.carry_in.value = BinaryValue("1")
    dut.slt.value = BinaryValue("1")
    dut.source_1.value = BinaryValue("1")
    dut.source_2.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "1")
    utils.assert_output(dut.carry_out, "1")
    utils.assert_output(dut.overflow, "0")
    await Timer(Decimal(1), units="ns")


def test_RV32I_ALU_BIT_synthesis():
    RV32I_ALU_BIT.build_vhd()
    # RV32I_ALU_BIT.build_netlistsvg()


def test_RV32I_ALU_BIT_testcases():
    RV32I_ALU_BIT.test_with(
        [
            tb_RV32I_ALU_BIT_case_1,
            tb_RV32I_ALU_BIT_case_2,
            tb_RV32I_ALU_BIT_case_3,
            tb_RV32I_ALU_BIT_case_4,
            tb_RV32I_ALU_BIT_case_5,
            tb_RV32I_ALU_BIT_case_6,
            tb_RV32I_ALU_BIT_case_7,
            tb_RV32I_ALU_BIT_case_8,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
