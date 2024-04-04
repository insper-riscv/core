import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils


class GENERIC_EDGE_DETECTOR(utils.DUT):
    clock = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    pulse = utils.DUT.Output_pin


@GENERIC_EDGE_DETECTOR.testcase
async def tb_GENERIC_EDGE_DETECTOR_case_1(dut: GENERIC_EDGE_DETECTOR, trace: utils.Trace):
    values_source = ["0", "1", "0", "0"]
    values_pulse = ["0", "0", "0", "1"]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    for index, (source_rise, pulse) in enumerate(zip(values_source, values_pulse)):
        dut.source.value = BinaryValue(source_rise)

        await RisingEdge(dut.clock)
        yield trace.check(dut.pulse, pulse, f"At clock {index}.")
        await FallingEdge(dut.clock)


@GENERIC_EDGE_DETECTOR.testcase
async def tb_GENERIC_EDGE_DETECTOR_case_2(dut: GENERIC_EDGE_DETECTOR, trace: utils.Trace):
    values_source = ["0", "1", "0", "0"]
    values_pulse = ["0", "0", "0", "1"]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=True))

    for index, (source_fall, pulse) in enumerate(zip(values_source, values_pulse)):
        dut.source.value = BinaryValue(source_fall)

        await FallingEdge(dut.clock)
        yield trace.check(dut.pulse, pulse, f"At clock {index}.")
        await RisingEdge(dut.clock)


def test_GENERIC_EDGE_DETECTOR_synthesis():
    GENERIC_EDGE_DETECTOR.build_vhd()
    # GENERIC_EDGE_DETECTOR.build_netlistsvg()


def test_GENERIC_EDGE_DETECTOR_testcases():
    GENERIC_EDGE_DETECTOR.test_with(
        [
            tb_GENERIC_EDGE_DETECTOR_case_1,
            tb_GENERIC_EDGE_DETECTOR_case_2,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
