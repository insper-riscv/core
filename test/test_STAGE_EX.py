import os

import pytest

import utils
from test_MODULE_ALU import MODULE_ALU
from test_MODULE_ALU_CONTROLLER import MODULE_ALU_CONTROLLER
from test_CPU_EXECUTION_FOWARDING_UNIT import CPU_EXECUTION_FOWARDING_UNIT
from test_MODULE_ALU_REGISTER_SOURCE import MODULE_ALU_REGISTER_SOURCE


class STAGE_EX(utils.DUT):
    source = utils.DUT.Input_pin
    selector_forwarding_mem = utils.DUT.Input_pin
    enable_mem              = utils.DUT.Input_pin
    selector_forwarding_wb  = utils.DUT.Input_pin
    enable_wb               = utils.DUT.Input_pin
    forwarding_mem_source   = utils.DUT.Input_pin
    forwarding_wb_source    = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    module_alu_controller = MODULE_ALU_CONTROLLER
    module_alu = MODULE_ALU
    cpu_execution_fowarding_unit = CPU_EXECUTION_FOWARDING_UNIT
    module_alu_register_source = MODULE_ALU_REGISTER_SOURCE


@pytest.mark.synthesis
def test_STAGE_EX_synthesis():
    STAGE_EX.build_vhd()
    # STAGE_EX.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
