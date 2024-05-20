import pytest

import lib
from test_CPU_package import CPU
from test_MODULE_PROGRAM_COUNTER import MODULE_PROGRAM_COUNTER


class CPU_STAGE_IF(lib.Entity):
    _package = CPU

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    address_jump = lib.Entity.Input_pin
    address_program = lib.Entity.Output_pin

    program_counter = MODULE_PROGRAM_COUNTER


@pytest.mark.synthesis
def test_CPU_STAGE_IF_synthesis():
    CPU_STAGE_IF.build_vhd()
    CPU_STAGE_IF.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
