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
async def tb_GENERIC_MUX_2X1(dut: GENERIC_MUX_2X1):
    values_source_1 = [
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]
    values_source_2 = [
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
    ]
    values_selector = ["0", "1", "0", "1"]
    values_destination = [
        "00001111000011110000111100001111",
        "11110000111100001111000011110000",
        "00000000000000000000000000000000",
        "11111111111111111111111111111111",
    ]

    for index, (source_1, source_2, selector, destination) in enumerate(
        zip(values_source_1, values_source_2, values_selector, values_destination)
    ):
        dut.source_1.value = BinaryValue(source_1)
        dut.source_2.value = BinaryValue(source_2)
        dut.selector.value = BinaryValue(selector)

        await Timer(Decimal(1), units="ns")

        condition = dut.destination.value.binstr == destination

        if not condition:
            dut._log.error(
                f"Expected value: {destination} Obtained value: {dut.destination.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test {index}: source_1={source_1} source_2={source_2} selector={selector}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_MUX_2X1():
    GENERIC_MUX_2X1.test_with(tb_GENERIC_MUX_2X1)


if __name__ == "__main__":
    test_GENERIC_MUX_2X1()
