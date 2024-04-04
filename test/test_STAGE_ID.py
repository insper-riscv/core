import os

import pytest

import utils
from test_MODULE_REGISTER_FILE import MODULE_REGISTER_FILE
from test_MODULE_CONTROL_UNIT import MODULE_CONTROL_UNIT


class STAGE_ID(utils.DUT):
    control = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    select_destination = utils.DUT.Input_pin
    data_destination = utils.DUT.Input_pin
    address_jump = utils.DUT.Output_pin
    control_if = utils.DUT.Output_pin
    signals_ex = utils.DUT.Output_pin

    module_control_unit = MODULE_CONTROL_UNIT
    module_register_file = MODULE_REGISTER_FILE


def test_STAGE_ID_synthesis():
    STAGE_ID.build_vhd()
    # STAGE_ID.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
