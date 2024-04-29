import pytest

import lib
from test_CPU_package import CPU
from test_MODULE_REGISTER_FILE import MODULE_REGISTER_FILE
from test_MODULE_CONTROL_UNIT import MODULE_CONTROL_UNIT
from test_MODULE_BRANCH_COMPARE_UNIT import MODULE_BRANCH_COMPARE_UNIT
from test_MODULE_BRANCH_UNIT import MODULE_BRANCH_UNIT


class CPU_STAGE_ID(lib.Entity):
    _package = CPU

    control = lib.Entity.Input_pin
    source = lib.Entity.Input_pin
    select_destination = lib.Entity.Input_pin
    data_destination = lib.Entity.Input_pin
    address_jump = lib.Entity.Output_pin
    control_if = lib.Entity.Output_pin
    signals_ex = lib.Entity.Output_pin
    branch = lib.Entity.Output_pin

    module_control_unit = MODULE_CONTROL_UNIT
    module_register_file = MODULE_REGISTER_FILE
    branch_compare_unit = MODULE_BRANCH_COMPARE_UNIT
    branch_unit = MODULE_BRANCH_UNIT


@pytest.mark.synthesis
def test_CPU_STAGE_ID_synthesis():
    CPU_STAGE_ID.build_vhd()
    # CPU_STAGE_ID.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
