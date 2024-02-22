from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_RV32I_ALU_BIT import RV32I_ALU_BIT


class RV32I_ALU(utils.DUT):
    CHILDREN = [RV32I_ALU_BIT]


@cocotb.test()
async def tb_RV32I_ALU(dut: RV32I_ALU):
    pass


def test_RV32I_ALU():
    RV32I_ALU.build_vhd()
    RV32I_ALU.test_with(tb_RV32I_ALU)


if __name__ == "__main__":
    test_RV32I_ALU()
