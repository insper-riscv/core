import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_PC(utils.DUT):
    clock = utils.DUT.Input_pin
    jump_address = utils.DUT.Input_pin
    selector = utils.DUT.Input_pin
    enable = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    mux_register_alu_1 = GENERIC_MUX_2X1
    pc_register = GENERIC_REGISTER
    adder = GENERIC_ADDER


@MODULE_PC.testcase
async def tb_MODULE_PC_case_1(dut: MODULE_PC, trace: utils.Trace):
    values_jump_address = [
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
    ]

    values_selector = ["1", "1", "1", "0", "1"]

    values_enable = ["0", "1", "1", "1", "1"]

    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000001000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000100",
    ]

    clock = Clock(dut.clock, 20000, units="ns")
    cocotb.start_soon(clock.start(start_high=False))

    for index, (jump_address, selector, enable, destination) in enumerate(
        zip(values_jump_address, values_selector, values_enable, values_destination)
    ):
        dut.jump_address.value = BinaryValue(jump_address)
        dut.enable.value = BinaryValue(enable)
        dut.selector.value = BinaryValue(selector)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")


def test_MODULE_PC_synthesis():
    MODULE_PC.build_vhd()
    # MODULE_PC.build_netlistsvg()


def test_MODULE_PC_testcases():
    MODULE_PC.test_with(
        [
            tb_MODULE_PC_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
