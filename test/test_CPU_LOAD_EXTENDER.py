import pytest
from cocotb.binary import BinaryValue

import lib
from test_CPU_package import CPU


class CPU_LOAD_EXTENDER(lib.Device):
    _package = CPU

    source      = lib.Device.Input_pin
    selector    = lib.Device.Input_pin
    destination = lib.Device.Output_pin

    tmp = lib.Device.Output_pin


@CPU_LOAD_EXTENDER.testcase
async def tb_CPU_LOAD_EXTENDER_case_1(dut: CPU_LOAD_EXTENDER, trace: lib.Waveform):
    dut.source.value = BinaryValue("00000000000000000000000010000000")
    dut.selector.value = BinaryValue("000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111110000000")

@pytest.mark.synthesis
def test_CPU_LOAD_EXTENDER_synthesis():
    CPU_LOAD_EXTENDER.build_vhd()
    # CPU_LOAD_EXTENDER.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_LOAD_EXTENDER_testcases():
    CPU_LOAD_EXTENDER.test_with(
        [
            tb_CPU_LOAD_EXTENDER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
