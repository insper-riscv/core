from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

import utils


class GENERIC_REGISTER_FILE(utils.DUT):
    clock: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    address_destination: utils.DUT.Input_pin
    address_source_1: utils.DUT.Input_pin
    address_source_2: utils.DUT.Input_pin
    data_destination: utils.DUT.Input_pin
    data_source_1: utils.DUT.Output_pin
    data_source_2: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_REGISTER_FILE(dut: GENERIC_REGISTER_FILE):
    clock = Clock(dut.clock, 20000, units="ns")
    values_enable = ["1", "1", "1", "1", "1"]
    values_address_destination = [
        "00001", "00011", "00111", "01111","11111",
    ]
    values_address_source_1 = [
        "00000", "00001", "00011", "00111","01111",
    ]
    values_address_source_2 = [
        "00001", "00011", "00111", "01111","11111",
    ]
    values_data_destination = [
        "11111111111111110000000000000000",
        "00000000000000001111111111111111",
        "11111111000000000000000011111111",
        "00000000111111111111111100000000",
        "01111111111111111111111111111110",
    ]
    values_data_source_1 = [
        "00000000000000000000000000000000",
        "11111111111111110000000000000000",
        "00000000000000001111111111111111",
        "11111111000000000000000011111111",
        "00000000111111111111111100000000",
    ]
    values_data_source_2 = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    for index, (enable, address_destination, address_source_1, address_source_2,
            data_destination, data_source_1, data_source_2) in enumerate(
        zip(values_enable, values_address_destination, values_address_source_1, values_address_source_2,
            values_data_destination, values_data_source_1, values_data_source_2)
    ):
        dut.enable.value = BinaryValue(enable)
        dut.address_destination.value = BinaryValue(address_destination)
        dut.address_source_1.value = BinaryValue(address_source_1)
        dut.address_source_2.value = BinaryValue(address_source_2)
        dut.data_destination.value = BinaryValue(data_destination)
        cocotb.start_soon(clock.start(start_high=False))

        await RisingEdge(dut.clock)

        await Timer(Decimal(20000), units="ns")

        condition = dut.data_source_1.value.binstr == data_source_1
        condition2 = dut.data_source_2.value.binstr == data_source_2

        if not condition:
            dut._log.error(
                f"Expected value condition: {data_source_1} Obtained value: {dut.data_source_1.value.binstr}"
            )

        if not condition2:
            dut._log.error(
                f"Expected value condition2: {data_source_2} Obtained value: {dut.data_source_2.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test {index}: enable={enable} clock={clock}"

        assert (
            condition2
        ), f"Error in test {index}: enable={enable} clock={clock}"


def test_GENERIC_REGISTER_FILE():
    GENERIC_REGISTER_FILE.test_with(tb_GENERIC_REGISTER_FILE)


if __name__ == "__main__":
    test_GENERIC_REGISTER_FILE()
