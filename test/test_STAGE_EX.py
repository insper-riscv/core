import os

import pytest

import utils
from test_MODULE_ALU import MODULE_ALU
from test_MODULE_ALU_CONTROLLER import MODULE_ALU_CONTROLLER
from test_RV32I_FORWARDING_UNIT_ALU import RV32I_FORWARDING_UNIT_ALU
from test_MODULE_ALU_REGISTER_SOURCE import MODULE_ALU_REGISTER_SOURCE


class STAGE_EX(utils.DUT):
    source = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    module_alu_controller = MODULE_ALU_CONTROLLER
    module_alu = MODULE_ALU
    rv32i_forwarding_unit_alu = RV32I_FORWARDING_UNIT_ALU
    module_alu_register_source = MODULE_ALU_REGISTER_SOURCE


def test_STAGE_EX_synthesis():
    STAGE_EX.build_vhd()
    # STAGE_EX.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
