import os

import pytest
from cocotb.binary import BinaryValue

import utils


class CPU_LOAD_EXTENDER(utils.DUT):
    source      = utils.DUT.Input_pin
    selector    = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    output_1 = utils.DUT.Output_pin

@pytest.mark.synthesis
def test_CPU_LOAD_EXTENDER_synthesis():
    CPU_LOAD_EXTENDER.build_vhd()
    # CPU_LOAD_EXTENDER.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_LOAD_EXTENDER_testcases():
    CPU_LOAD_EXTENDER.test_with(
        [
            #tb_CPU_LOAD_EXTENDER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
