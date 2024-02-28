from decimal import Decimal

import pytest
import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils


class GENERIC_COUNTER(utils.DUT):
    clock: utils.DUT.Input_pin
    clear: utils.DUT.Input_pin
    update: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    state: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_COUNTER(dut: GENERIC_COUNTER):
    clock = Clock(dut.clock, 20000, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    dut.clear.value = BinaryValue('1')
    await RisingEdge(dut.clock)
    await FallingEdge(dut.clock)

    condition = dut.state.value.binstr == '0'

    if not condition:
        dut._log.error(f"Expected value: {'0'} Obtained value: {dut.state.value.binstr}")

    assert (condition), f"Error in clear test 1"

    dut.source.value = BinaryValue("00010")
    dut.update.value = BinaryValue('1')
    dut.clear.value = BinaryValue('0')
    await FallingEdge(dut.clock)
    await FallingEdge(dut.clock)
    await FallingEdge(dut.clock)

    condition = dut.state.value.binstr == '1'

    if not condition:
        dut._log.error(f"Expected value: {'1'} Obtained value: {dut.state.value.binstr}")

    assert (condition), f"Error in count test"

    dut.clear.value = BinaryValue('1')
    await RisingEdge(dut.clock)
    await FallingEdge(dut.clock)

    condition = dut.state.value.binstr == '0'

    if not condition:
        dut._log.error(f"Expected value: {'0'} Obtained value: {dut.state.value.binstr}")

    assert (condition), f"Error in clear test 2"


def test_GENERIC_COUNTER():
    GENERIC_COUNTER.test_with(tb_GENERIC_COUNTER)


if __name__ == "__main__":
    test_GENERIC_COUNTER()
