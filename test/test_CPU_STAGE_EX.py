import pytest

import lib
from test_CPU_package import CPU
from test_MODULE_EXECUTION_UNIT import MODULE_EXECUTION_UNIT
from test_MODULE_EXECUTION_UNIT_CONTROLLER import MODULE_EXECUTION_UNIT_CONTROLLER
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1


class CPU_STAGE_EX(lib.Entity):
    _package = CPU

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    forward = lib.Entity.Input_pin
    select_source_1n = lib.Entity.Output_pin
    select_source_2n = lib.Entity.Output_pin
    destinationn = lib.Entity.Output_pin

    mux_forward_source_1 = GENERIC_MUX_4X1
    mux_forward_source_2 = GENERIC_MUX_4X1
    module_execution_unit_controller = MODULE_EXECUTION_UNIT_CONTROLLER
    module_execution_unit = MODULE_EXECUTION_UNIT


@pytest.mark.synthesis
def test_CPU_STAGE_EX_synthesis():
    CPU_STAGE_EX.build_vhd()
    CPU_STAGE_EX.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
