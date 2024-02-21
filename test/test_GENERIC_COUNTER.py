from decimal import Decimal

import pytest
import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer
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
    values_clear = ["0", "0", "0", "1",]
    values_update = ["0", "0", "1", "0",]
    values_source = ["00000", "00000", "00000", "00000",]
    values_state = ["0", "0", "0", "0",]
    clock = Clock(dut.clock, 20000, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    for index, (clear, update, source, state) in enumerate(zip(values_clear, values_update, values_source, values_state)):
        dut.clear.value = BinaryValue(clear)
        dut.update.value = BinaryValue(update)
        dut.source.value = BinaryValue(source)

        await Timer(Decimal(20000), units="ns")

        condition = dut.state.value.binstr == state

        if not condition:
            dut._log.error(f"Expected value: {state} Obtained value: {dut.state.value.binstr}")

        assert condition, f"Error in test {index}: clear={clear} update={update} source={source} clock={clock}"
        await Timer(Decimal(20000), units="ns")


@pytest.fixture(scope='session', autouse=True)
def build_GENERIC_COUNTER():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_COUNTER.vhd"],
        hdl_toplevel="generic_counter",
        always=True,
    )

def test_GENERIC_COUNTER():
    utils.runner.test(
        hdl_toplevel="generic_counter",
        test_module="test_GENERIC_COUNTER",
        testcase="tb_GENERIC_COUNTER",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_COUNTER()
