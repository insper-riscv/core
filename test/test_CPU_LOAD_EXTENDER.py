import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_CPU_package import CPU


class CPU_LOAD_EXTENDER(utils.DUT):
    _package = CPU

    source      = utils.DUT.Input_pin
    selector    = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

@CPU_LOAD_EXTENDER.testcase
async def tb_CPU_LOAD_EXTENDER_case_1(dut: CPU_LOAD_EXTENDER, trace: utils.Trace):
    dut.source.value = BinaryValue("00000000000000000000000010000000")
    dut.selector.value = BinaryValue("000")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111110000000")

@pytest.mark.synthesis
def test_CPU_LOAD_EXTENDER_synthesis():
    CPU_LOAD_EXTENDER.build_vhd()
    CPU_LOAD_EXTENDER.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_LOAD_EXTENDER_testcases():
    CPU_LOAD_EXTENDER.test_with(
        [
            tb_CPU_LOAD_EXTENDER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
