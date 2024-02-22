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
async def tb_GENERIC_ADDER(dut: "GENERIC_ADDER"):
    values_source_1 = [
        "00000000000000000000000000000000",
        "10101010101010101010101010101010",
        "00101010101010101010101010101010",
        "11111111111111111111111111111110",
    ]
    values_source_2 = [
        "00000000000000000000000000000000",
        "01010101010101010101010101010101",
        "00101010101010101010101010101010",
        "00000000000000000000000000000001",
    ]
    values_destination = [
        "00000000000000000000000000000000",
        "11111111111111111111111111111111",
        "01010101010101010101010101010100",
        "11111111111111111111111111111111",
    ]

    for index, (source_1, source_2, destination) in enumerate(
        zip(values_source_1, values_source_2, values_destination)
    ):
        dut.source_1.value = BinaryValue(source_1)
        dut.source_2.value = BinaryValue(source_2)

        await Timer(Decimal(1), units="ns")

        condition = dut.destination.value.binstr == destination

        if not condition:
            dut._log.error(
                f"Expected value: {destination} Obtained value: {dut.destination.value.binstr}"
            )

        assert condition, f"Error in test {index}: inA={source_1} inB={source_2}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_ADDER():
    GENERIC_ADDER.test_with(tb_GENERIC_ADDER)


if __name__ == "__main__":
    test_GENERIC_ADDER()
