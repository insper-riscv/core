from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_ADDER(utils.DUT):
    source_1: utils.DUT.Input_pin
    source_2: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_ADDER_case_1(dut: "GENERIC_ADDER"):
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "00000000000000000000000000000000")

    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_ADDER_case_2(dut: "GENERIC_ADDER"):
    dut.source_1.value = BinaryValue("10101010101010101010101010101010")
    dut.source_2.value = BinaryValue("01010101010101010101010101010101")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "11111111111111111111111111111111")

    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_ADDER_case_3(dut: "GENERIC_ADDER"):
    dut.source_1.value = BinaryValue("00101010101010101010101010101010")
    dut.source_2.value = BinaryValue("00101010101010101010101010101010")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "01010101010101010101010101010100")

    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_ADDER_case_4(dut: "GENERIC_ADDER"):
    dut.source_1.value = BinaryValue("11111111111111111111111111111110")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")

    await Timer(Decimal(1), units="ns")

    utils.assert_output(dut.destination, "11111111111111111111111111111111")

    await Timer(Decimal(1), units="ns")


def test_GENERIC_ADDER_syntesis():
    GENERIC_ADDER.build_vhd()
    GENERIC_ADDER.build_netlistsvg()


def test_GENERIC_ADDER_case_1():
    GENERIC_ADDER.test_with(tb_GENERIC_ADDER_case_1)


def test_GENERIC_ADDER_case_2():
    GENERIC_ADDER.test_with(tb_GENERIC_ADDER_case_2)


def test_GENERIC_ADDER_case_3():
    GENERIC_ADDER.test_with(tb_GENERIC_ADDER_case_3)


def test_GENERIC_ADDER_case_4():
    GENERIC_ADDER.test_with(tb_GENERIC_ADDER_case_4)


if __name__ == "__main__":
    pytest.main(["-k", f"test_GENERIC_ADDER"])
