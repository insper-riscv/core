from decimal import Decimal

import pytest
import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_COUNTER(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_COUNTER(dut: GENERIC_COUNTER):
    pass


@pytest.fixture(scope='session', autouse=True)
def build_GENERIC_COUNTER():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_COUNTER.vhd"],
        hdl_toplevel="generic_counter",
        always=True,
    )

def test_GENERIC_COUNTER():
    utils.runner.test(
        hdl_toplevel="generic_counter",
        test_module="test_GENERIC_COUNTER",
        testcase="tb_GENERIC_COUNTER",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_COUNTER()
