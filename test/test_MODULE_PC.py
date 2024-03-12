from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

import utils
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_PC(utils.DUT):
    CHILDREN = [GENERIC_MUX_2X1, GENERIC_REGISTER, GENERIC_ADDER]
    clock        : utils.DUT.Input_pin
    jump_address : utils.DUT.Input_pin
    selector     : utils.DUT.Input_pin
    enable       : utils.DUT.Input_pin
    #pc           : utils.DUT.Output_pin
    destination  : utils.DUT.Output_pin


@cocotb.test()
async def tb_MODULE_PC_case_1(dut: MODULE_PC):
    values_jump_address = [
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
    ]

    values_selector = ["1", "1", "0", "1", "1"]

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

        await RisingEdge(dut.clock)
        await Timer(Decimal(20000), units="ns")
        utils.assert_output(dut.destination, destination, f"At clock {index}.")

def test_MODULE_PC_syntesis():
    MODULE_PC.build_vhd()
    #MODULE_PC.build_netlistsvg()

def test_MODULE_PC_case_1():
    MODULE_PC.test_with(tb_MODULE_PC_case_1)

if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_PC"])
