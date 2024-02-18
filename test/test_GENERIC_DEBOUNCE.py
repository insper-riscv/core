from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_DEBOUNCE(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_DEBOUNCE(dut: GENERIC_DEBOUNCE):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_DEBOUNCE():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_DEBOUNCE.vhd"],
        hdl_toplevel="generic_debounce",
        always=True,
    )

def test_GENERIC_DEBOUNCE():
    utils.runner.test(
        hdl_toplevel="generic_debounce",
        test_module="test_GENERIC_DEBOUNCE",
        testcase="tb_GENERIC_DEBOUNCE",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_DEBOUNCE()
