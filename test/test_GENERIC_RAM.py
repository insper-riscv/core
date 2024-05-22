import pytest
import cocotb
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_RAM(lib.Entity):
    _package = GENERICS

    clock = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    enable_read = lib.Entity.Input_pin
    enable_write = lib.Entity.Input_pin
    address = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_RAM.testcase
async def tb_GENERIC_RAM_case_1(dut: GENERIC_RAM, trace: lib.Waveform):
    values_enable = ["0", "1", "1", "1", "1"]
    values_enable_read = ["1", "0", "1", "0", "1"]
    values_enable_write = ["0", "1", "0", "1", "0"]
    values_address = [
        "00000000",
        "00000001",
        "00000001",
        "10000000",
        "10000000",
    ]
    values_source = [
        "00000000",
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
    GENERIC_RAM.build_netlistsvg()

@pytest.mark.testcases
def test_GENERIC_RAM_testcases():
    GENERIC_RAM.test_with(tb_GENERIC_RAM_case_1)


if __name__ == "__main__":
    lib.run_test(__file__)
