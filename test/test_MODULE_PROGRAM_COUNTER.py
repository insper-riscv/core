import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1
from test_GENERIC_REGISTER import GENERIC_REGISTER
from test_GENERIC_ADDER import GENERIC_ADDER


class MODULE_PROGRAM_COUNTER(lib.Device):
    _package = MODULES

    clock = lib.Device.Input_pin
    selector = lib.Device.Input_pin
    source = lib.Device.Input_pin
    enable = lib.Device.Input_pin
    destination = lib.Device.Output_pin

    mux_source = GENERIC_MUX_2X1
    count_register = GENERIC_REGISTER
    count_adder = GENERIC_ADDER


@MODULE_PROGRAM_COUNTER.testcase
async def tb_MODULE_PROGRAM_COUNTER_case_1(dut: MODULE_PROGRAM_COUNTER, trace: lib.Waveform):
    values_source = [
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
        "11111111111111110000000000000000",
    ]

    values_selector = ["0", "1", "0", "0", "1"]

    values_enable = ["1", "1", "1", "0", "0"]

    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "11111111111111110000000000000000",
        "11111111111111110000000000000100",
        "11111111111111110000000000000100",
    ]

    for index, (source, selector, enable, destination) in enumerate(
        zip(values_source, values_selector, values_enable, values_destination)
    ):
        dut.source.value = BinaryValue(source)
        dut.enable.value = BinaryValue(enable)
        dut.selector.value = BinaryValue(selector)

        yield trace.check(dut.destination, destination, f"At clock {index}.")
        await trace.cycle()


@pytest.mark.synthesis
def test_MODULE_PROGRAM_COUNTER_synthesis():
    MODULE_PROGRAM_COUNTER.build_vhd()
    # MODULE_PROGRAM_COUNTER.build_netlistsvg()


@pytest.mark.testcases
def test_MODULE_PROGRAM_COUNTER_testcases():
    MODULE_PROGRAM_COUNTER.test_with(
        [
            tb_MODULE_PROGRAM_COUNTER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
