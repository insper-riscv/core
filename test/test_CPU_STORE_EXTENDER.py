import os

import pytest
from cocotb.binary import BinaryValue

import utils
from test_CPU_package import CPU


class CPU_STORE_EXTENDER(utils.DUT):
    _package = CPU

    source      = utils.DUT.Input_pin
    selector    = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin

    output_1 = utils.DUT.Output_pin

@pytest.mark.synthesis
def test_CPU_STORE_EXTENDER_synthesis():
    CPU_STORE_EXTENDER.build_vhd()
    # CPU_STORE_EXTENDER.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_STORE_EXTENDER_testcases():
    CPU_STORE_EXTENDER.test_with(
        [
            #tb_CPU_STORE_EXTENDER_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
