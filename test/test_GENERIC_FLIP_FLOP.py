from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_FLIP_FLOP(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_FLIP_FLOP(dut: GENERIC_FLIP_FLOP):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_FLIP_FLOP():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_FLIP_FLOP.vhd"],
        hdl_toplevel="generic_flip_flop",
        always=True,
    )

def test_GENERIC_FLIP_FLOP():
    utils.runner.test(
        hdl_toplevel="generic_flip_flop",
        test_module="test_GENERIC_FLIP_FLOP",
        testcase="tb_GENERIC_FLIP_FLOP",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_FLIP_FLOP()
