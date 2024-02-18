from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_REGISTER(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_REGISTER(dut: GENERIC_REGISTER):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_REGISTER():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_REGISTER.vhd"],
        hdl_toplevel="generic_register",
        always=True,
    )

def test_GENERIC_REGISTER():
    utils.runner.test(
        hdl_toplevel="generic_register",
        test_module="test_GENERIC_REGISTER",
        testcase="tb_GENERIC_REGISTER",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_REGISTER()
