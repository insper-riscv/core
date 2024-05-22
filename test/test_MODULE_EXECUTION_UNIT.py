import pytest
from cocotb.binary import BinaryValue

import lib
from test_MODULES_package import MODULES
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1
from test_RV32I_ALU import RV32I_ALU


class MODULE_EXECUTION_UNIT(lib.Entity):
    _package = MODULES

    select_source_1 = lib.Entity.Input_pin
    select_source_2 = lib.Entity.Input_pin
    select_function = lib.Entity.Input_pin
    address_program = lib.Entity.Input_pin
    source_1 = lib.Entity.Input_pin
    source_2 = lib.Entity.Input_pin
    immediate = lib.Entity.Input_pin
    destination = lib.Entity.Output_pin

    mux_alu_source_1 = GENERIC_MUX_4X1
    mux_alu_source_2 = GENERIC_MUX_4X1
    alu = RV32I_ALU


@pytest.mark.synthesis
def test_MODULE_EXECUTION_UNIT_synthesis():
    MODULE_EXECUTION_UNIT.build_vhd()
    MODULE_EXECUTION_UNIT.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
