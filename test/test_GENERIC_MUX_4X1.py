import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class GENERIC_MUX_4X1(utils.DUT):
    source_1 = utils.DUT.Input_pin
    source_2 = utils.DUT.Input_pin
    source_3 = utils.DUT.Input_pin
    source_4 = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    mux_1 = GENERIC_MUX_2X1
    mux_2 = GENERIC_MUX_2X1


@cocotb.test()
async def tb_GENERIC_MUX_4X1_case_1(dut: GENERIC_MUX_4X1):
    dut.source_1.value = BinaryValue("00001111000011110000111100001111")
    dut.source_2.value = BinaryValue("11110000111100001111000011110000")
    dut.source_3.value = BinaryValue("00000000111111111111111100000000")
    dut.source_4.value = BinaryValue("11111111000000000000000011111111")
    dut.selector.value = BinaryValue("00")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00001111000011110000111100001111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_MUX_4X1_case_2(dut: GENERIC_MUX_4X1):
    dut.source_1.value = BinaryValue("00001111000011110000111100001111")
    dut.source_2.value = BinaryValue("11110000111100001111000011110000")
    dut.source_3.value = BinaryValue("00000000111111111111111100000000")
    dut.source_4.value = BinaryValue("11111111000000000000000011111111")
    dut.selector.value = BinaryValue("01")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11110000111100001111000011110000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_MUX_4X1_case_3(dut: GENERIC_MUX_4X1):
    dut.source_1.value = BinaryValue("00001111000011110000111100001111")
    dut.source_2.value = BinaryValue("11110000111100001111000011110000")
    dut.source_3.value = BinaryValue("00000000111111111111111100000000")
    dut.source_4.value = BinaryValue("11111111000000000000000011111111")
    dut.selector.value = BinaryValue("10")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000111111111111111100000000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_GENERIC_MUX_4X1_case_4(dut: GENERIC_MUX_4X1):
    dut.source_1.value = BinaryValue("00001111000011110000111100001111")
    dut.source_2.value = BinaryValue("11110000111100001111000011110000")
    dut.source_3.value = BinaryValue("00000000111111111111111100000000")
    dut.source_4.value = BinaryValue("11111111000000000000000011111111")
    dut.selector.value = BinaryValue("11")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111000000000000000011111111")
    await Timer(Decimal(1), units="ns")


def test_GENERIC_MUX_4X1_synthesis():
    GENERIC_MUX_4X1.build_vhd()
    # GENERIC_MUX_4X1.build_netlistsvg()


def test_GENERIC_MUX_4X1_testcases():
    GENERIC_MUX_4X1.test_with(
        [
            tb_GENERIC_MUX_4X1_case_1,
            tb_GENERIC_MUX_4X1_case_2,
            tb_GENERIC_MUX_4X1_case_3,
            tb_GENERIC_MUX_4X1_case_4,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
