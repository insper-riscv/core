from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

import utils


class GENERIC_STACK(utils.DUT):
    clock: utils.DUT.Input_pin
    enable_read: utils.DUT.Input_pin
    enable_write: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin
    overflow: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_STACK(dut: GENERIC_STACK):
    clock = Clock(dut.clock, 20000, units="ns")
    values_enable_read = [
        "0",
        "1",
        "0",
        "0",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
    ]
    values_enable_write = [
        "1",
        "0",
        "1",
        "1",
        "0",
        "0",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ]
    values_source = [
        "00000000000000001111111111111111",
        "00000000000000000000000000000000",
        "00000000000000001111111111111111",
        "00000000111111111111111111111111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
    ]
    values_destination = [
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
        "00000000000000001111111111111111",
        "00000000000000001111111111111111",
        "00000000111111111111111111111111",
        "00000000111111111111111111111111",
        "00000000000000001111111111111111",
        "00000000000000001111111111111111",
        "00000000000000001111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
    ]
    values_overflow = [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
    ]

    for index, (enable_read, enable_write, source, destination, overflow) in enumerate(
        zip(
            values_enable_read,
            values_enable_write,
            values_source,
            values_destination,
            values_overflow,
        )
    ):
        dut.enable_read.value = BinaryValue(enable_read)
        dut.enable_write.value = BinaryValue(enable_write)
        dut.source.value = BinaryValue(source)
        cocotb.start_soon(clock.start(start_high=False))

        await RisingEdge(dut.clock)

        await Timer(Decimal(20000), units="ns")

        condition = dut.destination.value.binstr == destination

        if not condition:
            dut._log.error(
                f"Expected destination value: {destination} Obtained destination value: {dut.destination.value.binstr}, Expected overflow value: {overflow} Obtained overflow value: {dut.overflow.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test {index}: enable_read={enable_read}, enable_write={enable_write} source={source} clock={clock}"
        await Timer(Decimal(20000), units="ns")


def test_GENERIC_STACK():
    GENERIC_STACK.test_with(tb_GENERIC_STACK)


if __name__ == "__main__":
    test_GENERIC_STACK()
