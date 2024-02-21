from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils


class GENERIC_FLIP_FLOP(utils.DUT):
    clock: utils.DUT.Input_pin
    clear: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    source: utils.DUT.Input_pin
    state: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_FLIP_FLOP(dut: GENERIC_FLIP_FLOP):
    values_clear = ["0", "0", "1", ]
    values_enable = ["1", "1", "0", ]
    values_source = ["1", "0", "1", ]
    values_state = ["1", "0", "0", ]
    clock = Clock(dut.clock, 20000, units="ns")

    for index, (clear, enable, source, state) in enumerate(zip(values_clear, values_enable, values_source, values_state)):
        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)
        cocotb.start_soon(clock.start(start_high=False))

        await RisingEdge(dut.clock)

        await Timer(Decimal(20000), units="ns")

        condition = dut.state.value.binstr == state

        if not condition:
            dut._log.error(f"Expected value: {state} Obtained value: {dut.state.value.binstr}")

        assert condition, f"Error in test {index}: clear={clear} enable={enable} source={source} clock={clock}"
        await Timer(Decimal(20000), units="ns")


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_FLIP_FLOP():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_FLIP_FLOP.vhd"],
        hdl_toplevel="generic_flip_flop",
        always=True,
    )

def test_GENERIC_FLIP_FLOP():
    utils.runner.test(
        hdl_toplevel="generic_flip_flop",
        test_module="test_GENERIC_FLIP_FLOP",
        testcase="tb_GENERIC_FLIP_FLOP",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_FLIP_FLOP()
