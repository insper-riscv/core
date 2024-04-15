import os

import pytest

import utils
from test_CPU_package import CPU
from test_MODULE_WRITE_BACK import MODULE_WRITE_BACK


class CPU_STAGE_WB(utils.DUT):
    _package = CPU

    source = utils.DUT.Input_pin
    enable_destination = utils.DUT.Output_pin
    select_destination = utils.DUT.Output_pin
    destination = utils.DUT.Output_pin

    module_write_back = MODULE_WRITE_BACK


@pytest.mark.synthesis
def test_CPU_STAGE_WB_synthesis():
    CPU_STAGE_WB.build_vhd()
    # CPU_STAGE_WB.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
