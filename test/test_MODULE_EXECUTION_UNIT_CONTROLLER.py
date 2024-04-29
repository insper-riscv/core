import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_RV32I_ALU_CONTROLLER import RV32I_ALU_CONTROLLER


class MODULE_EXECUTION_UNIT_CONTROLLER(lib.Device):
    _package = MODULES

    opcode = lib.Device.Input_pin
    funct_3 = lib.Device.Input_pin
    funct_7 = lib.Device.Input_pin
    destination = lib.Device.Output_pin

    alu_controller = RV32I_ALU_CONTROLLER


@MODULE_EXECUTION_UNIT_CONTROLLER.testcase
async def tb_MODULE_EXECUTION_UNIT_CONTROLLER_case_1(dut: "MODULE_EXECUTION_UNIT_CONTROLLER", trace: lib.Waveform):
    dut.opcode.value = BinaryValue("01100")
    dut.funct_3.value = BinaryValue("111")
    dut.funct_7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000")

    dut.opcode.value = BinaryValue("01100")
    dut.funct_3.value = BinaryValue("000")
    dut.funct_7.value = BinaryValue("0000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00011")

    dut.opcode.value = BinaryValue("01100")
    dut.funct_3.value = BinaryValue("000")
    dut.funct_7.value = BinaryValue("0100000")

    await trace.cycle()
    yield trace.check(dut.destination, "01011")


@pytest.mark.synthesis
def test_MODULE_EXECUTION_UNIT_CONTROLLER_synthesis():
    MODULE_EXECUTION_UNIT_CONTROLLER.build_vhd()
    # MODULE_EXECUTION_UNIT_CONTROLLER.build_netlistsvg()


@pytest.mark.testcases
def test_MODULE_EXECUTION_UNIT_CONTROLLER_testcases():
    MODULE_EXECUTION_UNIT_CONTROLLER.test_with(
        [
            tb_MODULE_EXECUTION_UNIT_CONTROLLER_case_1,
        ]
    )


if __name__ == "__main__":
    lib.run_test(__file__)
