from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils


class GENERIC_EDGE_DETECTOR(utils.DUT):
    clock: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    pulse: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_EDGE_DETECTOR(dut: GENERIC_EDGE_DETECTOR):
    values_source_rise = ["0", "1", "0", "0",]
    values_pulse_rise = ["0", "0", "0", "1"]
    values_source_fall = ["0", "1", "0", "0",]
    values_pulse_fall = ["0", "0", "0", "1"]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))
    for index, (source_rise, pulse) in enumerate(
        zip(values_source_rise, values_pulse_rise)
    ):
        dut.source.value = BinaryValue(source_rise)

        await RisingEdge(dut.clock)

        condition = dut.pulse.value.binstr == pulse

        if not condition:
            dut._log.error(
                f"Expected value: {pulse} Obtained value: {dut.pulse.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test rise {index}: clock={clock} source_rise={source_rise}"
        await FallingEdge(dut.clock)

    cocotb.start_soon(clock.start(start_high=True))
    for index, (source_fall, pulse) in enumerate(
        zip(values_source_fall, values_pulse_fall)
    ):
        dut.source.value = BinaryValue(source_fall)

        await FallingEdge(dut.clock)

        condition = dut.pulse.value.binstr == pulse

        if not condition:
            dut._log.error(
                f"Expected value: {pulse} Obtained value: {dut.pulse.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test fall {index}: clock={clock} source_fall={source_fall}"
        await RisingEdge(dut.clock)


def test_GENERIC_EDGE_DETECTOR():
    GENERIC_EDGE_DETECTOR.test_with(tb_GENERIC_EDGE_DETECTOR)


if __name__ == "__main__":
    test_GENERIC_EDGE_DETECTOR()
