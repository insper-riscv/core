import pytest
from cocotb.binary import BinaryValue

import lib
from test_GENERICS_package import GENERICS


class GENERIC_FLIP_FLOP(lib.Entity):
    _package = GENERICS

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    state = lib.Entity.Output_pin


@GENERIC_FLIP_FLOP.testcase
async def tb_GENERIC_FLIP_FLOP_case_1(dut: GENERIC_FLIP_FLOP, trace: lib.Waveform):
    values_clear = ["0", "0", "1"]
    values_enable = ["1", "1", "0"]
    values_source = ["1", "0", "1"]
    values_state = ["1", "0", "0"]

    for index, (clear, enable, source, state) in enumerate(
        zip(values_clear, values_enable, values_source, values_state)
    ):
        dut.clear.value = BinaryValue(clear)
        dut.enable.value = BinaryValue(enable)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.state, state, f"At clock {index}.")


@pytest.mark.synthesis
def test_GENERIC_FLIP_FLOP_synthesis():
    GENERIC_FLIP_FLOP.build_vhd()
    GENERIC_FLIP_FLOP.build_netlistsvg()


@pytest.mark.testcases
def test_GENERIC_FLIP_FLOP_testcases():
    GENERIC_FLIP_FLOP.test_with(
        [
            tb_GENERIC_FLIP_FLOP_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
