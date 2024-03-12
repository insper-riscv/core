from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock

import utils
from test_GENERIC_RAM import GENERIC_RAM


class MODULE_MEMORY(utils.DUT):
    CHILDREN = [GENERIC_RAM]
    clock: utils.DUT.Input_pin
    enable: utils.DUT.Input_pin
    enable_read: utils.DUT.Input_pin
    enable_write: utils.DUT.Input_pin
    source_ex: utils.DUT.Input_pin
    register_source_2: utils.DUT.Input_pin
    destination: utils.DUT.Output_pin

@cocotb.test()
async def tb_MODULE_MEMORY_case_1(dut: MODULE_MEMORY):
    values_enable = ["0", "1", "1", "1", "1"]
    values_enable_read = ["1", "0", "1", "0", "1"]
    values_enable_write = ["1", "1", "0", "1", "0"]
    values_source_ex = [
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000001000001",
        "00000000000000000000000001000001",
    ]
    values_register_source_2 = [
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00000000000000000000000000000000",
        "11110000111100001111000011110000",
        "00000000000000000000000000000000",
    ]
    values_destination = [
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "00001111000011110000111100001111",
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "11110000111100001111000011110000",
    ]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    for index, (
        enable,
        enable_read,
        enable_write,
        source_ex,
        register_source_2,
        destination,
    ) in enumerate(
        zip(
            values_enable,
            values_enable_read,
            values_enable_write,
            values_source_ex,
            values_register_source_2,
            values_destination,
        )
    ):
        dut.enable.value = BinaryValue(enable)
        dut.enable_read.value = BinaryValue(enable_read)
        dut.enable_write.value = BinaryValue(enable_write)
        dut.source_ex.value = BinaryValue(source_ex)
        dut.register_source_2.value = BinaryValue(register_source_2)

        await RisingEdge(dut.clock)
        await Timer(Decimal(20000), units="ns")
        utils.assert_output(dut.destination, destination, f"At clock {index}.")
        await Timer(Decimal(20000), units="ns")


def test_MODULE_MEMORY_synthesis():
    MODULE_MEMORY.build_vhd()
    #MODULE_MEMORY.build_netlistsvg()


def test_MODULE_MEMORY_case_1():
    MODULE_MEMORY.test_with(tb_MODULE_MEMORY_case_1)


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_MEMORY"])
