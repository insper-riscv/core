from decimal import Decimal

import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_XOR(utils.DUT):
    a: utils.DUT.Input_pin
    b: utils.DUT.Input_pin
    q: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_XOR(dut: GENERIC_XOR):
    inA = ["0", "0", "1", "1"]
    inB = ["0", "1", "0", "1"]
    out = ["0", "1", "1", "0"]

    for i, (ia, ib, o) in enumerate(zip(inA, inB, out)):
        dut.a.value = BinaryValue(ia)
        dut.b.value = BinaryValue(ib)

        await Timer(Decimal(1), units="ns")

        condition = dut.q.value.binstr == o

        if not condition:
            dut._log.error(f"Expected value: {o} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {i}: inA={ia} inB={ib}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_XOR():
    runner = cocotb.runner.get_runner("ghdl")

    runner.build(
        vhdl_sources=["src/GENERIC_XOR.vhd"],
        always=True,
    )

    runner.test(
        hdl_toplevel="generic_xor",
        test_module="test_GENERIC_XOR",
        testcase="tb_GENERIC_XOR",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_XOR()
