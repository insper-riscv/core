from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_MUX_2X1(utils.DUT):
    source_1: utils.DUT.Input_pin
    source_2: utils.DUT.Input_pin
    selector: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_MUX_2X1_case_1(dut: GENERIC_MUX_2X1):
    dut.source_1.value = BinaryValue("00001111000011110000111100001111")
    dut.source_2.value = BinaryValue("11110000111100001111000011110000")
    dut.selector.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00001111000011110000111100001111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_MUX_2X1_case_2(dut: GENERIC_MUX_2X1):
    dut.source_1.value = BinaryValue("00001111000011110000111100001111")
    dut.source_2.value = BinaryValue("11110000111100001111000011110000")
    dut.selector.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11110000111100001111000011110000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_MUX_2X1_case_3(dut: GENERIC_MUX_2X1):
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")
    dut.selector.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000000000000000000000000000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_MUX_2X1_case_4(dut: GENERIC_MUX_2X1):
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("11111111111111111111111111111111")
    dut.selector.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111111111111111111111111111")
    await Timer(Decimal(1), units="ns")


def test_GENERIC_MUX_2X1_syntesis():
    GENERIC_MUX_2X1.build_vhd()
    #GENERIC_MUX_2X1.build_netlistsvg()


def test_GENERIC_MUX_2X1_case_1():
    GENERIC_MUX_2X1.test_with(tb_GENERIC_MUX_2X1_case_1)


def test_GENERIC_MUX_2X1_case_2():
    GENERIC_MUX_2X1.test_with(tb_GENERIC_MUX_2X1_case_2)


def test_GENERIC_MUX_2X1_case_3():
    GENERIC_MUX_2X1.test_with(tb_GENERIC_MUX_2X1_case_3)


def test_GENERIC_MUX_2X1_case_4():
    GENERIC_MUX_2X1.test_with(tb_GENERIC_MUX_2X1_case_4)


if __name__ == "__main__":
    pytest.main(["-k", f"test_GENERIC_MUX_2X1"])
