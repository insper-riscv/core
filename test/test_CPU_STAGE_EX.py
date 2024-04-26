import os

import pytest

import utils
from test_CPU_package import CPU
from test_MODULE_EXECUTION_UNIT import MODULE_EXECUTION_UNIT
from test_MODULE_EXECUTION_UNIT_CONTROLLER import MODULE_EXECUTION_UNIT_CONTROLLER
from test_CPU_EXECUTION_FOWARDING_UNIT import CPU_EXECUTION_FOWARDING_UNIT


class CPU_STAGE_EX(utils.DUT):
    _package = CPU

    source = utils.DUT.Input_pin
    selector_forwarding_mem = utils.DUT.Input_pin
    enable_mem              = utils.DUT.Input_pin
    selector_forwarding_wb  = utils.DUT.Input_pin
    enable_wb               = utils.DUT.Input_pin
    forwarding_mem_source   = utils.DUT.Input_pin
    forwarding_wb_source    = utils.DUT.Input_pin
    destination             = utils.DUT.Output_pin

    module_execution_unit_controller = MODULE_EXECUTION_UNIT_CONTROLLER
    module_execution_unit = MODULE_EXECUTION_UNIT
    cpu_execution_fowarding_unit = CPU_EXECUTION_FOWARDING_UNIT


@pytest.mark.synthesis
def test_CPU_STAGE_EX_synthesis():
    CPU_STAGE_EX.build_vhd()
    # CPU_STAGE_EX.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
