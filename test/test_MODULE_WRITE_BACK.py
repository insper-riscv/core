import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_WRITE_BACK(utils.DUT):
    source_memory = utils.DUT.Input_pin
    source_ex = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    mux = GENERIC_MUX_2X1


@cocotb.test()
async def tb_MODULE_WRITE_BACK_case_1(dut: MODULE_WRITE_BACK):
    dut.source_memory.value = BinaryValue("00001111000011110000111100001111")
    dut.source_ex.value = BinaryValue("11110000111100001111000011110000")
    dut.selector.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00001111000011110000111100001111")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_MODULE_WRITE_BACK_case_2(dut: MODULE_WRITE_BACK):
    dut.source_memory.value = BinaryValue("00001111000011110000111100001111")
    dut.source_ex.value = BinaryValue("11110000111100001111000011110000")
    dut.selector.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11110000111100001111000011110000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_MODULE_WRITE_BACK_case_3(dut: MODULE_WRITE_BACK):
    dut.source_memory.value = BinaryValue("00000000000000000000000000000000")
    dut.source_ex.value = BinaryValue("11111111111111111111111111111111")
    dut.selector.value = BinaryValue("0")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "00000000000000000000000000000000")
    await Timer(Decimal(1), units="ns")


@cocotb.test()
async def tb_MODULE_WRITE_BACK_case_4(dut: MODULE_WRITE_BACK):
    dut.source_memory.value = BinaryValue("00000000000000000000000000000000")
    dut.source_ex.value = BinaryValue("11111111111111111111111111111111")
    dut.selector.value = BinaryValue("1")

    await Timer(Decimal(1), units="ns")
    utils.assert_output(dut.destination, "11111111111111111111111111111111")
    await Timer(Decimal(1), units="ns")


def test_MODULE_WRITE_BACK_synthesis():
    MODULE_WRITE_BACK.build_vhd()
    # MODULE_WRITE_BACK.build_netlistsvg()


def test_MODULE_WRITE_BACK_testcases():
    MODULE_WRITE_BACK.test_with(
        [
            tb_MODULE_WRITE_BACK_case_1,
            tb_MODULE_WRITE_BACK_case_2,
            tb_MODULE_WRITE_BACK_case_3,
            tb_MODULE_WRITE_BACK_case_4,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
