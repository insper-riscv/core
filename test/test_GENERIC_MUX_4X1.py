from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class GENERIC_MUX_4X1(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1]

    source_1: utils.DUT.Input_pin
    source_2: utils.DUT.Input_pin
    source_3: utils.DUT.Input_pin
    source_4: utils.DUT.Input_pin
    selector: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_MUX_4X1(dut: GENERIC_MUX_4X1):
    values_source_1 = [
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
    ]
    values_source_2 = [
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
    ]
    values_source_3 = [
        "00000000111111111111111100000000",
        "00000000111111111111111100000000",
        "00000000111111111111111100000000",
        "00000000111111111111111100000000",
    ]
    values_source_4 = [
        "11111111000000000000000011111111",
        "11111111000000000000000011111111",
        "11111111000000000000000011111111",
        "11111111000000000000000011111111",
    ]
    values_selector = ["00", "01", "10", "11"]
    values_destination = [
        "00001111000011110000111100001111",
        "11110000111100001111000011110000",
        "00000000111111111111111100000000",
        "11111111000000000000000011111111",
    ]

    for index, (source_1, source_2, source_3, source_4, selector, destination) in enumerate(zip(values_source_1, values_source_2, values_source_3, values_source_4, values_selector, values_destination)):
        dut.source_1.value = BinaryValue(source_1)
        dut.source_2.value = BinaryValue(source_2)
        dut.source_3.value = BinaryValue(source_3)
        dut.source_4.value = BinaryValue(source_4)
        dut.selector.value = BinaryValue(selector)

        await Timer(Decimal(1), units="ns")

        condition = dut.destination.value.binstr == destination

        if not condition:
            dut._log.error(f"Expected value: {destination} Obtained value: {dut.destination.value.binstr}")

        assert condition, f"Error in test {index}: source_1={source_1} source_2={source_2} source_3={source_3} source_4={source_4} selector={selector}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_MUX_4X1():
    GENERIC_MUX_4X1.build_vhd()
    GENERIC_MUX_4X1.test_with(tb_GENERIC_MUX_4X1)


if __name__ == "__main__":
    test_GENERIC_MUX_4X1()
