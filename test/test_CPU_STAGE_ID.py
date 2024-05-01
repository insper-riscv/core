import os

import pytest

import utils
from test_CPU_package import CPU
from test_MODULE_REGISTER_FILE import MODULE_REGISTER_FILE
from test_MODULE_CONTROL_UNIT import MODULE_CONTROL_UNIT
from test_MODULE_BRANCH_COMPARE_UNIT import MODULE_BRANCH_COMPARE_UNIT
from test_MODULE_BRANCH_UNIT import MODULE_BRANCH_UNIT


class CPU_STAGE_ID(utils.DUT):
    _package = CPU

    control = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    select_destination = utils.DUT.Input_pin
    data_destination = utils.DUT.Input_pin
    address_jump = utils.DUT.Output_pin
    control_if = utils.DUT.Output_pin
    signals_ex = utils.DUT.Output_pin
    branch = utils.DUT.Output_pin

    module_control_unit = MODULE_CONTROL_UNIT
    module_register_file = MODULE_REGISTER_FILE
    branch_compare_unit = MODULE_BRANCH_COMPARE_UNIT
    branch_unit = MODULE_BRANCH_UNIT

@pytest.mark.synthesis
def test_CPU_STAGE_ID_synthesis():
    CPU_STAGE_ID.build_vhd()
    CPU_STAGE_ID.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
