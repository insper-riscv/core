import os

import pytest

import utils
from test_CPU_package import CPU
from test_MODULE_PROGRAM_COUNTER import MODULE_PROGRAM_COUNTER


class CPU_STAGE_IF(utils.DUT):
    _package = CPU

    control = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    address_jump = utils.DUT.Input_pin
    branch = utils.DUT.Input_pin
    address_program = utils.DUT.Output_pin

    module_program_counter = MODULE_PROGRAM_COUNTER


@pytest.mark.synthesis
def test_CPU_STAGE_IF_synthesis():
    CPU_STAGE_IF.build_vhd()
    # CPU_STAGE_IF.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
