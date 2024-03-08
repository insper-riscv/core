from decimal import Decimal

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_INSTRUCTION_DECODER(utils.DUT):
    pass


@cocotb.test()
async def tb_RV32I_INSTRUCTION_DECODER(dut: RV32I_INSTRUCTION_DECODER):
    pass


def test_RV32I_INSTRUCTION_DECODER():
    RV32I_INSTRUCTION_DECODER.test_with(tb_RV32I_INSTRUCTION_DECODER)


if __name__ == "__main__":
    test_RV32I_INSTRUCTION_DECODER()
