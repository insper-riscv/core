import pytest

import lib
from test_CPU_package import CPU
from test_MODULE_MEMORY_INTERFACE import MODULE_MEMORY_INTERFACE


class CPU_STAGE_MEM(lib.Entity):
    _package = CPU

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    data_memory_in = lib.Entity.Input_pin
    control_memory = lib.Entity.Output_pin
    address_memory = lib.Entity.Output_pin
    data_memory_out = lib.Entity.Output_pin
    destination = lib.Entity.Output_pin

    mem_interface = MODULE_MEMORY_INTERFACE


@pytest.mark.synthesis
def test_CPU_STAGE_MEM_synthesis():
    CPU_STAGE_MEM.build_vhd()
    CPU_STAGE_MEM.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
