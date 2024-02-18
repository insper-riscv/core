from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_ALU_BIT(utils.DUT):
    pass


@cocotb.test()
async def tb_RV32I_ALU_BIT(dut: RV32I_ALU_BIT):
    pass


@pytest.fixture(scope="module", autouse=True)
def build_RV32I_ALU_BIT():
    utils.runner.build(
        vhdl_sources=["src/RV32I_ALU_BIT.vhd"],
        hdl_toplevel="rv32i_alu_bit",
        always=True,
    )

def test_RV32I_ALU_BIT():
    utils.runner.test(
        hdl_toplevel="rv32i_alu_bit",
        test_module="test_RV32I_ALU_BIT",
        testcase="tb_RV32I_ALU_BIT",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_RV32I_ALU_BIT()
