from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_ADDER(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_ADDER(dut: GENERIC_ADDER):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_ADDER():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_ADDER.vhd"],
        hdl_toplevel="generic_adder",
        always=True,
    )

def test_GENERIC_ADDER():
    utils.runner.test(
        hdl_toplevel="generic_adder",
        test_module="test_GENERIC_ADDER",
        testcase="tb_GENERIC_ADDER",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_ADDER()
