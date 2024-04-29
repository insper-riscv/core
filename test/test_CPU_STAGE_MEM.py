import pytest

import lib
from test_CPU_package import CPU
from test_CPU_STORE_EXTENDER import CPU_STORE_EXTENDER
from test_CPU_LOAD_EXTENDER import CPU_LOAD_EXTENDER


class CPU_STAGE_MEM(lib.Device):
    _package = CPU

    clock = lib.Device.Input_pin
    source = lib.Device.Input_pin
    control_memory = lib.Device.Output_pin
    address_memory = lib.Device.Output_pin
    data_memory = lib.Device.Output_pin
    destination = lib.Device.Output_pin

    cpu_store_extender = CPU_STORE_EXTENDER
    cpu_load_extender = CPU_LOAD_EXTENDER


@pytest.mark.synthesis
def test_CPU_STAGE_MEM_synthesis():
    CPU_STAGE_MEM.build_vhd()
    # CPU_STAGE_MEM.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
