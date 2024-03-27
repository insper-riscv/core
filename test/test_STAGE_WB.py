import os

import pytest

import utils
from test_MODULE_WRITE_BACK import MODULE_WRITE_BACK


class STAGE_WB(utils.DUT):
    source = utils.DUT.Input_pin
    enable_destination = utils.DUT.Output_pin
    select_destination = utils.DUT.Output_pin
    destination = utils.DUT.Output_pin

    module_write_back = MODULE_WRITE_BACK


def test_STAGE_WB_synthesis():
    STAGE_WB.build_vhd()
    # STAGE_WB.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
