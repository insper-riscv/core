import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_REGISTER(lib.Entity):
    _package = GENERICS

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin


@GENERIC_REGISTER.testcase
async def tb_GENERIC_REGISTER_case_1(dut: GENERIC_REGISTER, trace: lib.Waveform):
    values_clear = ["0", "0", "1", "0", "0"]
    values_enable = ["1", "0", "0", "1", "1"]
    values_source = [
        "11111111",
        "00000000",
        "00000000",
        "11111111",
        "00000000",
    ]
    values_destination = [
        "11111111",
        "11111111",
        "00000000",
        "11111111",
        "00000000",
    ]

    for index, (clear, enable, source, destination) in enumerate(
        zip(values_clear, values_enable, values_source, values_destination)
    ):
        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")


@pytest.mark.synthesis
def test_GENERIC_REGISTER_synthesis():
    GENERIC_REGISTER.build_vhd()
    GENERIC_REGISTER.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_REGISTER_testcases():
    GENERIC_REGISTER.test_with(
        [
            tb_GENERIC_REGISTER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
