import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_WRITE_BACK(lib.Entity):
    _package = MODULES

    selector = lib.Entity.Input_pin
    source_memory = lib.Entity.Input_pin
    source_execution = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    MUX_SOURCE = GENERIC_MUX_2X1


@MODULE_WRITE_BACK.testcase
async def tb_MODULE_WRITE_BACK_case_1(dut: MODULE_WRITE_BACK, trace: lib.Waveform):
    dut.selector.value = BinaryValue("0")
    dut.source_memory.value = BinaryValue("00001111000011110000111100001111")
    dut.source_execution.value = BinaryValue("11110000111100001111000011110000")

    await trace.cycle()
    yield trace.check(dut.destination, "00001111000011110000111100001111")

    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "11110000111100001111000011110000")

    dut.selector.value = BinaryValue("0")
    dut.source_memory.value = BinaryValue("00000000000000000000000000000000")
    dut.source_execution.value = BinaryValue("11111111111111111111111111111111")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000")

    dut.selector.value = BinaryValue("1")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")


@pytest.mark.synthesis
def test_MODULE_WRITE_BACK_synthesis():
    MODULE_WRITE_BACK.build_vhd()
    MODULE_WRITE_BACK.build_netlistsvg()


@pytest.mark.testcases
def test_MODULE_WRITE_BACK_testcases():
    MODULE_WRITE_BACK.test_with(
        [
            tb_MODULE_WRITE_BACK_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
