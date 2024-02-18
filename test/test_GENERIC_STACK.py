from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_STACK(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_STACK(dut: GENERIC_STACK):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_STACK():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_STACK.vhd"],
        hdl_toplevel="generic_stack",
        always=True,
    )

def test_GENERIC_STACK():
    utils.runner.test(
        hdl_toplevel="generic_stack",
        test_module="test_GENERIC_STACK",
        testcase="tb_GENERIC_STACK",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_STACK()
