import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_RV32I_package import RV32I


class RV32I_BRANCH_CONTROLLER(utils.DUT):
    _package = RV32I

    select_function : utils.DUT.Input_pin
    source_1        : utils.DUT.Input_pin
    source_2        : utils.DUT.Input_pin
    destination     : utils.DUT.Output_pin    



@pytest.mark.synthesis
def test_RV32I_BRANCH_CONTROLLER_synthesis():
    RV32I_BRANCH_CONTROLLER.build_vhd()
    RV32I_BRANCH_CONTROLLER.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
