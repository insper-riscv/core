from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_MUX_2X1(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_MUX_2X1(dut: GENERIC_MUX_2X1):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_MUX_2X1():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_MUX_2X1.vhd"],
        hdl_toplevel="generic_mux_2x1",
        always=True,
    )

def test_GENERIC_MUX_2X1():
    utils.runner.test(
        hdl_toplevel="generic_mux_2x1",
        test_module="test_GENERIC_MUX_2X1",
        testcase="tb_GENERIC_MUX_2X1",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_MUX_2X1()
