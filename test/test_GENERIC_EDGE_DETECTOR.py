from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_EDGE_DETECTOR(utils.DUT):
    clock: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    pulse: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_EDGE_DETECTOR(dut: GENERIC_EDGE_DETECTOR):
    values_clock =  ["0", "0", "1", "1"]
    values_source = ["0", "1", "0", "1"]
    values_pulse =  ["0", "0", "0", "0"]

    for index, (clock, source, pulse) in enumerate(zip(values_clock, values_source, values_pulse)):
        dut.clock.value = BinaryValue(clock)
        dut.source.value = BinaryValue(source)

        await Timer(Decimal(1), units="ns")

        condition = dut.pulse.value.binstr == pulse

        if not condition:
            dut._log.error(f"Expected value: {pulse} Obtained value: {dut.pulse.value.binstr}")

        assert condition, f"Error in test {index}: clock={clock} source={source}"
        await Timer(Decimal(1), units="ns")


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_EDGE_DETECTOR():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_EDGE_DETECTOR.vhd"],
        hdl_toplevel="generic_edge_detector",
        always=True,
    )

def test_GENERIC_EDGE_DETECTOR():
    utils.runner.test(
        hdl_toplevel="generic_edge_detector",
        test_module="test_GENERIC_EDGE_DETECTOR",
        testcase="tb_GENERIC_EDGE_DETECTOR",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_EDGE_DETECTOR()
