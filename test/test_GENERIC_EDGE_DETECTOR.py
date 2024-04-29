import pytest
from cocotb.binary import BinaryValue
from cocotb.triggers import RisingEdge, FallingEdge

import lib
from test_GENERICS_package import GENERICS


class GENERIC_EDGE_DETECTOR(lib.Device):
    _package = GENERICS

    clock = lib.Device.Input_pin
    source = lib.Device.Input_pin
    pulse = lib.Device.Output_pin


@GENERIC_EDGE_DETECTOR.testcase
async def tb_GENERIC_EDGE_DETECTOR_case_1(dut: GENERIC_EDGE_DETECTOR, trace: lib.Waveform):
    values_source = ["0", "1", "0", "0"]
    values_pulse = ["0", "0", "0", "1"]

    for index, (source_rise, pulse) in enumerate(zip(values_source, values_pulse)):
        dut.source.value = BinaryValue(source_rise)

        await RisingEdge(dut.clock)
        yield trace.check(dut.pulse, pulse, f"At clock {index}.")
        await FallingEdge(dut.clock)


@GENERIC_EDGE_DETECTOR.testcase
async def tb_GENERIC_EDGE_DETECTOR_case_2(dut: GENERIC_EDGE_DETECTOR, trace: lib.Waveform):
    values_source = ["0", "1", "0", "0"]
    values_pulse = ["0", "0", "0", "1"]

    for index, (source_fall, pulse) in enumerate(zip(values_source, values_pulse)):
        dut.source.value = BinaryValue(source_fall)

        await FallingEdge(dut.clock)
        yield trace.check(dut.pulse, pulse, f"At clock {index}.")
        await RisingEdge(dut.clock)


@pytest.mark.synthesis
def test_GENERIC_EDGE_DETECTOR_synthesis():
    GENERIC_EDGE_DETECTOR.build_vhd()
    # GENERIC_EDGE_DETECTOR.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_EDGE_DETECTOR_testcases():
    GENERIC_EDGE_DETECTOR.test_with(
        [
            tb_GENERIC_EDGE_DETECTOR_case_1,
            tb_GENERIC_EDGE_DETECTOR_case_2,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
