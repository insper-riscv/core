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


def test_RV32I_ALU_BIT():
    RV32I_ALU_BIT.build_vhd()
    RV32I_ALU_BIT.test_with(tb_RV32I_ALU_BIT)


if __name__ == "__main__":
    test_RV32I_ALU_BIT()
