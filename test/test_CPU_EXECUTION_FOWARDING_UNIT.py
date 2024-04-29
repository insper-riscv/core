import pytest

import lib
from test_CPU_package import CPU


@pytest.mark.synthesis
class CPU_EXECUTION_FOWARDING_UNIT(lib.Device):
    _package = CPU

    stage_ex_select_source_1     = lib.Device.Input_pin
    stage_ex_select_source_2     = lib.Device.Input_pin
    stage_mem_enable_destination = lib.Device.Input_pin
    stage_mem_select_destination = lib.Device.Input_pin
    stage_wb_enable_destination  = lib.Device.Input_pin
    stage_wb_select_destination  = lib.Device.Input_pin
    stage_id_select_source_1     = lib.Device.Output_pin
    stage_id_select_source_2     = lib.Device.Output_pin


def test_CPU_EXECUTION_FOWARDING_UNIT_synthesis():
    CPU_EXECUTION_FOWARDING_UNIT.build_vhd()
    # CPU_EXECUTION_FOWARDING_UNIT.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
