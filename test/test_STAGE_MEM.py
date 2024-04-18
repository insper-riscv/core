import os

import pytest

import utils


class STAGE_MEM(utils.DUT):
    clock = utils.DUT.Input_pin
    source = utils.DUT.Input_pin
    control_memory = utils.DUT.Output_pin
    address_memory = utils.DUT.Output_pin
    data_memory = utils.DUT.Output_pin
    funct_3 = utils.DUT.Output_pin
    store_byte = utils.DUT.Output_pin
    store_halfword = utils.DUT.Output_pin
    destination = utils.DUT.Output_pin


@pytest.mark.synthesis
def test_STAGE_MEM_synthesis():
    STAGE_MEM.build_vhd()
    # STAGE_MEM.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
