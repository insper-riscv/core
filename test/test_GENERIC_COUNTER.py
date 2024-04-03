import os

import pytest
import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

import utils


class GENERIC_COUNTER(utils.DUT):
    clock = utils.DUT.Input_pin
    clear = utils.DUT.Input_pin
    update = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    state = utils.DUT.Output_pin


@GENERIC_COUNTER.testcase
async def tb_GENERIC_COUNTER_case_1(dut: GENERIC_COUNTER, trace: utils.Trace):
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    dut.clear.value = BinaryValue("1")
    dut.update.value = BinaryValue("0")
    dut.source.value = 0

    await trace.cycle()

    for i in range(5):
        yield trace.check(dut.state, "0")

        dut.source.value = i + 1
        dut.update.value = BinaryValue("1")
        dut.clear.value = BinaryValue("0")

        await trace.cycle()

        dut.update.value = BinaryValue("0")

        await trace.cycle()
        await trace.gap(2**(i + 1) - 2)
        await trace.cycle()

        yield trace.check(dut.state, "1")

        dut.clear.value = BinaryValue("1")

        await trace.cycle()

    yield trace.check(dut.state, "0")
    await trace.cycle()


def test_GENERIC_COUNTER_synthesis():
    GENERIC_COUNTER.build_vhd()
    # GENERIC_COUNTER.build_netlistsvg()


def test_GENERIC_COUNTER_testcases():
    GENERIC_COUNTER.test_with(
        [
            tb_GENERIC_COUNTER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
