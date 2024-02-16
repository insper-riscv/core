from decimal import Decimal

import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class RV32I_ALU(utils.DUT):
    a: utils.DUT.Input_pin
    b: utils.DUT.Input_pin
    s: utils.DUT.Input_pin
    q: utils.DUT.Output_pin


@cocotb.test()
async def tb_RV32I_ALU(dut: RV32I_ALU):
    in_a = ["0000", "0000", "0001", "0001"]
    in_b = ["0001", "0001", "0001", "0001"]
    in_s = ["00", "01", "00", "01"]
    out_q = ["1111", "0001", "0000", "0010"]

    for index, (value_a, value_b, value_s, value_q) in enumerate(
        zip(in_a, in_b, in_s, out_q)
    ):
        dut.a.value = BinaryValue(value_a)
        dut.b.value = BinaryValue(value_b)
        dut.s.value = BinaryValue(value_s)

        await Timer(Decimal(1), units="ns")

        condition = dut.q.value.binstr == value_q

        if not condition:
            dut._log.error(
                f"Expected value: {value_q} Obtained value: {dut.q.value.binstr}"
            )

        assert (
            condition
        ), f"Error in test {index}: inA={value_a} inB={value_b} inS={value_s}"
        await Timer(Decimal(1), units="ns")


def test_RV32I_ALU():
    runner = cocotb.runner.get_runner("ghdl")

    runner.build(
        vhdl_sources=["src/RV32I_ALU.vhd"],
        always=True,
    )

    runner.test(
        hdl_toplevel="rv32i_alu",
        test_module="test_RV32I_ALU",
        testcase="tb_RV32I_ALU",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_RV32I_ALU()
