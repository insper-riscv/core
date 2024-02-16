from decimal import Decimal

import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_AND(utils.DUT):
    a: utils.DUT.Input_pin
    b: utils.DUT.Input_pin
    q: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_AND(dut: GENERIC_AND):
    values_a = ["0", "0", "1", "1"]
    values_b = ["0", "1", "0", "1"]
    values_q = ["0", "0", "0", "1"]

    print(dut._log)
    print(type(dut._log))

    for index, (a, b, q) in enumerate(zip(values_a, values_b, values_q)):
        dut.a.value = BinaryValue(a)
        dut.b.value = BinaryValue(b)

        await Timer(Decimal(1), units="ns")

        condition = dut.q.value.binstr == q

        if not condition:
            dut._log.error(f"Expected value: {q} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {index}: inA={a} inB={b}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_AND():
    runner = cocotb.runner.get_runner("ghdl")

    runner.build(
        vhdl_sources=["src/GENERIC_AND.vhd"],
        always=True,
    )

    runner.test(
        hdl_toplevel="generic_and",
        test_module="test_GENERIC_AND",
        testcase="tb_GENERIC_AND",
        hdl_toplevel_lang="vhdl",
    )


if __name__ == "__main__":
    test_GENERIC_AND()
