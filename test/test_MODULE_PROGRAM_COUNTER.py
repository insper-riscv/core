import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_PROGRAM_COUNTER(lib.Entity):
    _package = MODULES

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    selector = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    mux_source = GENERIC_MUX_2X1
    count_register = GENERIC_REGISTER
    count_adder = GENERIC_ADDER


@MODULE_PROGRAM_COUNTER.testcase
async def tb_MODULE_PROGRAM_COUNTER_case_1(dut: MODULE_PROGRAM_COUNTER, trace: lib.Waveform):
    values_enable = ["1", "1", "1", "1", "1", "1", "1", "0"]
    values_selector = ["0", "0", "0", "1", "0", "0", "0", "1"]
    values_source = [
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
        "00000000000000000000000000100000",
    ]
    values_destination = [
        "00000000000000000000000000000100",
        "00000000000000000000000000001000",
        "00000000000000000000000000001100",
        "00000000000000000000000000100000",
        "00000000000000000000000000100100",
        "00000000000000000000000000101000",
        "00000000000000000000000000101100",
        "00000000000000000000000000101100",
    ]
    
    yield trace.check(dut.destination, "00000000000000000000000000000000", f"At clock 0.")

    for index, (enable, selector, source, destination) in enumerate(
        zip(values_enable, values_selector, values_source, values_destination),
        1,
    ):
        dut.enable.value = BinaryValue(enable)
        dut.selector.value = BinaryValue(selector)
        dut.source.value = BinaryValue(source)

        await trace.cycle()
        yield trace.check(dut.destination, destination, f"At clock {index}.")


@pytest.mark.synthesis
def test_MODULE_PROGRAM_COUNTER_synthesis():
    MODULE_PROGRAM_COUNTER.build_vhd()
    MODULE_PROGRAM_COUNTER.build_netlistsvg()

@pytest.mark.testcases
def test_MODULE_PROGRAM_COUNTER_testcases():
    MODULE_PROGRAM_COUNTER.test_with(tb_MODULE_PROGRAM_COUNTER_case_1)


if __name__ == "__main__":
    lib.run_test(__file__)
