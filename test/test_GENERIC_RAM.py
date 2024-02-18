from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_RAM(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_RAM(dut: GENERIC_RAM):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_RAM():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_RAM.vhd"],
        hdl_toplevel="generic_ram",
        always=True,
    )

def test_GENERIC_RAM():
    utils.runner.test(
        hdl_toplevel="generic_ram",
        test_module="test_GENERIC_RAM",
        testcase="tb_GENERIC_RAM",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_RAM()
