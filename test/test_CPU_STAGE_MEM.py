import os

import pytest

import utils
from test_CPU_package import CPU
from test_CPU_STORE_EXTENDER import CPU_STORE_EXTENDER
from test_CPU_LOAD_EXTENDER import CPU_LOAD_EXTENDER


class CPU_STAGE_MEM(utils.DUT):
    _package = CPU

    clock = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    control_memory = utils.DUT.Output_pin
    address_memory = utils.DUT.Output_pin
    data_memory = utils.DUT.Output_pin
    destination = utils.DUT.Output_pin

    cpu_store_extender = CPU_STORE_EXTENDER
    cpu_load_extender = CPU_LOAD_EXTENDER


@pytest.mark.synthesis
def test_CPU_STAGE_MEM_synthesis():
    CPU_STAGE_MEM.build_vhd()
    # CPU_STAGE_MEM.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
