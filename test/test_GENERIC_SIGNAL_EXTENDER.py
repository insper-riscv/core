from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_SIGNAL_EXTENDER(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_SIGNAL_EXTENDER(dut: GENERIC_SIGNAL_EXTENDER):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_SIGNAL_EXTENDER():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_SIGNAL_EXTENDER.vhd"],
        hdl_toplevel="generic_signal_extender",
        always=True,
    )

def test_GENERIC_SIGNAL_EXTENDER():
    utils.runner.test(
        hdl_toplevel="generic_signal_extender",
        test_module="test_GENERIC_SIGNAL_EXTENDER",
        testcase="tb_GENERIC_SIGNAL_EXTENDER",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_SIGNAL_EXTENDER()
