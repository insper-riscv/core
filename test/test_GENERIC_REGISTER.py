import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

import utils


class GENERIC_REGISTER(utils.DUT):
    clock = utils.DUT.Input_pin
    clear = utils.DUT.Input_pin
    enable = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_1(dut: GENERIC_REGISTER, trace: utils.Trace):
    values_clear = ["0", "0", "1", "0", "0"]
    values_enable = ["1", "0", "0", "1", "1"]
    values_source = [
        "11111111111111111111111111111111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111111111111111111111111",
        "00000000000000000000000000000000",
    ]
    values_destination = [
        "11111111111111111111111111111111",
        "11111111111111111111111111111111",
        "00000000000000000000000000000000",
        "11111111111111111111111111111111",
        "00000000000000000000000000000000",
    ]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    for index, (clear, enable, source, destination) in enumerate(
        zip(values_clear, values_enable, values_source, values_destination)
    ):
        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")


def test_GENERIC_REGISTER_synthesis():
    GENERIC_REGISTER.build_vhd()
    # GENERIC_REGISTER.build_netlistsvg()


def test_GENERIC_REGISTER_testcases():
    GENERIC_REGISTER.test_with(
        [
            tb_GENERIC_REGISTER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
