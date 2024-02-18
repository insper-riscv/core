from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_EDGE_DETECTOR(utils.DUT):
    pass


@cocotb.test()
async def tb_GENERIC_EDGE_DETECTOR(dut: GENERIC_EDGE_DETECTOR):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_GENERIC_EDGE_DETECTOR():
    utils.runner.build(
        vhdl_sources=["src/GENERIC_EDGE_DETECTOR.vhd"],
        hdl_toplevel="generic_edge_detector",
        always=True,
    )

def test_GENERIC_EDGE_DETECTOR():
    utils.runner.test(
        hdl_toplevel="generic_edge_detector",
        test_module="test_GENERIC_EDGE_DETECTOR",
        testcase="tb_GENERIC_EDGE_DETECTOR",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_EDGE_DETECTOR()
