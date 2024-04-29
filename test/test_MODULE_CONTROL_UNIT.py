import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_GENERIC_ADDER import GENERIC_ADDER
from test_GENERIC_MUX_2X1 import GENERIC_MUX_2X1


class MODULE_CONTROL_UNIT(lib.Entity):
    _package = MODULES

    instruction = lib.Entity.Input_pin
    immediate = lib.Entity.Output_pin


@MODULE_CONTROL_UNIT.testcase
async def tb_MODULE_CONTROL_UNIT_case_1(dut: "MODULE_CONTROL_UNIT", trace: lib.Waveform):
    dut.instruction.value = BinaryValue("00000000000000000001010000110111")

    await trace.cycle()
    yield trace.check(dut.immediate, "00000000000000000001000000000000")


@pytest.mark.synthesis
def test_MODULE_CONTROL_UNIT_synthesis():
    MODULE_CONTROL_UNIT.build_vhd()
    # MODULE_CONTROL_UNIT.build_netlistsvg()


@pytest.mark.testcases
def test_MODULE_CONTROL_UNIT_testcases():
    MODULE_CONTROL_UNIT.test_with(
        [
            tb_MODULE_CONTROL_UNIT_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
