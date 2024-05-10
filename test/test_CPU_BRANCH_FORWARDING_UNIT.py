import os

import pytest

import lib
from test_CPU_package import CPU


class CPU_BRANCH_FORWARDING_UNIT(lib.Entity):
    _package = CPU

    stage_id_select_source_1 = lib.Entity.Input_pin
    stage_id_select_source_2 = lib.Entity.Input_pin
    stage_mem_enable_destination = lib.Entity.Input_pin
    stage_mem_select_destination = lib.Entity.Input_pin
    stage_id_source_1 = lib.Entity.Output_pin
    stage_id_source_2 = lib.Entity.Output_pin


@pytest.mark.synthesis
def test_CPU_BRANCH_FORWARDING_UNIT_synthesis():
    CPU_BRANCH_FORWARDING_UNIT.build_vhd()
    CPU_BRANCH_FORWARDING_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
