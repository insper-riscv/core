import os

import pytest
from cocotb.binary import BinaryValue

import utils


class GENERIC_ROM(utils.DUT):
    address = utils.DUT.Input_pin
    destination = utils.DUT.Output_pin


@GENERIC_ROM.testcase
async def tb_GENERIC_ROM_case_1(dut: GENERIC_ROM, trace: utils.Trace):
    dut.address.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000001010000110111")


def test_GENERIC_ROM_synthesis():
    GENERIC_ROM.build_vhd()
    # GENERIC_ROM.build_netlistsvg()


def test_GENERIC_ROM_testcases():
    GENERIC_ROM.test_with(
        [
            tb_GENERIC_ROM_case_1,
        ]
    )


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
