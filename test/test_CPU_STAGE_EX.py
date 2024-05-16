import pytest

import lib
from test_CPU_package import CPU
from test_MODULE_EXECUTION_UNIT import MODULE_EXECUTION_UNIT
from test_MODULE_EXECUTION_UNIT_CONTROLLER import MODULE_EXECUTION_UNIT_CONTROLLER
from test_CPU_EXECUTION_FORWARDING_UNIT import CPU_EXECUTION_FORWARDING_UNIT
from test_GENERIC_MUX_4X1 import GENERIC_MUX_4X1


class CPU_STAGE_EX(lib.Entity):
    _package = CPU

    source = lib.Entity.Input_pin
    selector_forwarding_mem = lib.Entity.Input_pin
    enable_mem = lib.Entity.Input_pin
    selector_forwarding_wb = lib.Entity.Input_pin
    enable_wb = lib.Entity.Input_pin
    forwarding_mem_source = lib.Entity.Input_pin
    forwarding_wb_source = lib.Entity.Input_pin
    enable_read = lib.Entity.Output_pin
    destination = lib.Entity.Output_pin

    module_execution_unit_controller = MODULE_EXECUTION_UNIT_CONTROLLER
    module_execution_unit = MODULE_EXECUTION_UNIT
    cpu_execution_forwarding_unit = CPU_EXECUTION_FORWARDING_UNIT
    mux_forward_source_1 = GENERIC_MUX_4X1
    mux_forward_source_2 = GENERIC_MUX_4X1


@pytest.mark.synthesis
def test_CPU_STAGE_EX_synthesis():
    CPU_STAGE_EX.build_vhd()
    CPU_STAGE_EX.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
