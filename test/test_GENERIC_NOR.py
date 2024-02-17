from decimal import Decimal

import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_NOR(utils.DUT):
    a: utils.DUT.Input_pin
    b: utils.DUT.Input_pin
    q: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_NOR(dut: GENERIC_NOR):
    inA = ["0", "0", "1", "1"]
    inB = ["0", "1", "0", "1"]
    out = ["1", "0", "0", "0"]

    for i, (ia, ib, o) in enumerate(zip(inA, inB, out)):
        dut.a.value = BinaryValue(ia)
        dut.b.value = BinaryValue(ib)

        await Timer(Decimal(1), units="ns")

        condition = dut.q.value.binstr == o

        if not condition:
            dut._log.error(f"Expected value: {o} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {i}: inA={ia} inB={ib}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_NOR():
    runner = cocotb.runner.get_runner("ghdl")

    runner.build(
        vhdl_sources=["src/GENERIC_MUX_4X1.vhd"],
        hdl_toplevel="generic_mux_4x1",
        always=True,
    )

    runner.test(
        hdl_toplevel="generic_mux_4x1",
        test_module="test_GENERIC_MUX_4X1",
        testcase="tb_GENERIC_MUX_4X1",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_NOR()
