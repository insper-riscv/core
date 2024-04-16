import os

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

import utils
from test_GENERICS_package import GENERICS


class GENERIC_RAM(utils.DUT):
    _package = GENERICS

    clock = utils.DUT.Input_pin
    enable = utils.DUT.Input_pin
    enable_read = utils.DUT.Input_pin
    enable_write = utils.DUT.Input_pin
    address = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_RAM.testcase
async def tb_GENERIC_RAM_case_1(dut: GENERIC_RAM, trace: utils.Trace):
    values_enable = ["0", "1", "1", "1", "1"]
    values_enable_read = ["1", "0", "1", "0", "1"]
    values_enable_write = ["1", "1", "0", "1", "0"]
    values_address = [
        "00000001",
        "00000001",
        "00000001",
        "00010001",
        "00010001",
    ]
    values_source = [
        "00001111",
        "00001111",
        "00000000",
        "11110000",
        "00000000",
    ]
    values_destination = [
        "ZZZZZZZZ",
        "ZZZZZZZZ",
        "00001111",
        "ZZZZZZZZ",
        "11110000",
    ]
    clock = Clock(dut.clock, 20000, units="ns")

    cocotb.start_soon(clock.start(start_high=False))

    for index, (
        enable,
        enable_read,
        enable_write,
        address,
        source,
        destination,
    ) in enumerate(
        zip(
            values_enable,
            values_enable_read,
            values_enable_write,
            values_address,
            values_source,
            values_destination,
        )
    ):
        dut.enable.value = BinaryValue(enable)
        dut.enable_read.value = BinaryValue(enable_read)
        dut.enable_write.value = BinaryValue(enable_write)
        dut.address.value = BinaryValue(address)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")


@pytest.mark.synthesis
def test_GENERIC_RAM_synthesis():
    GENERIC_RAM.build_vhd()
    # GENERIC_RAM.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_RAM_testcases():
    GENERIC_RAM.test_with(
        [
            tb_GENERIC_RAM_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
