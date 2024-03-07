from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils


class GENERIC_RAM(utils.DUT):
    clock: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    enable_read: utils.DUT.Input_pin
    enable_write: utils.DUT.Input_pin
    address: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_RAM(dut: GENERIC_RAM):
    values_enable = [
        "0",
        "1",
        "1",
        "1",
        "1",
    ]
    values_enable_read = [
        "1",
        "0",
        "1",
        "0",
        "1",
    ]
    values_enable_write = [
        "1",
        "1",
        "0",
        "1",
        "0",
    ]
    values_address = [
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000010000000000000001",
        "00000000000000010000000000000001",
    ]
    values_source = [
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00000000000000000000000000000000",
        "11110000111100001111000011110000",
        "00000000000000000000000000000000",
    ]
    values_destination = [
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "00001111000011110000111100001111",
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "11110000111100001111000011110000",

    ]
    clock = Clock(dut.clock, 20000, units="ns")

    for index, (enable, enable_read, enable_write, address,
        source, destination) in enumerate(
        zip(values_enable, values_enable_read, values_enable_write, values_address, values_source, values_destination)
    ):
        dut.enable.value = BinaryValue(enable)
        dut.enable_read.value = BinaryValue(enable_read)
        dut.enable_write.value = BinaryValue(enable_write)
        dut.address.value = BinaryValue(address)
        dut.source.value = BinaryValue(source)
        cocotb.start_soon(clock.start(start_high=False))

        await RisingEdge(dut.clock)

        await Timer(Decimal(20000), units="ns")

        condition = dut.destination.value.binstr == destination

        if not condition:
            dut._log.error(
                f"Expected value: {destination} Obtained value: {dut.destination.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test {index}: enable={enable} enable_read={enable_read} enable_write={enable_write} address={address} source={source}"
        await Timer(Decimal(20000), units="ns")


def test_GENERIC_RAM():
    GENERIC_RAM.test_with(tb_GENERIC_RAM)


if __name__ == "__main__":
    test_GENERIC_RAM()
