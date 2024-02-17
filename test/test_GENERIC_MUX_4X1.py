from decimal import Decimal

import cocotb
import cocotb.runner
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils


class GENERIC_MUX_4X1(utils.DUT):
    a: utils.DUT.Input_pin
    b: utils.DUT.Input_pin
    c: utils.DUT.Input_pin
    d: utils.DUT.Input_pin
    s: utils.DUT.Input_pin
    q: utils.DUT.Output_pin


@cocotb.test()
async def tb_GENERIC_MUX_4X1(dut: GENERIC_MUX_4X1):
    inA = [
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
        "00001111000011110000111100001111",
    ]
    inB = [
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
        "11110000111100001111000011110000",
    ]
    inC = [
        "00000000111111111111111100000000",
        "00000000111111111111111100000000",
        "00000000111111111111111100000000",
        "00000000111111111111111100000000",
    ]
    inD = [
        "11111111000000000000000011111111",
        "11111111000000000000000011111111",
        "11111111000000000000000011111111",
        "11111111000000000000000011111111",
    ]
    inS = ["00", "01", "10", "11"]
    out = [
        "00001111000011110000111100001111",
        "11110000111100001111000011110000",
        "00000000111111111111111100000000",
        "11111111000000000000000011111111",
    ]

    for i, (ia, ib, ic, iD, iS, o) in enumerate(zip(inA, inB, inC, inD, inS, out)):
        dut.a.value = BinaryValue(ia)
        dut.b.value = BinaryValue(ib)
        dut.c.value = BinaryValue(ic)
        dut.d.value = BinaryValue(iD)
        dut.s.value = BinaryValue(iS)

        await Timer(Decimal(1), units="ns")

        condition = dut.q.value.binstr == o

        if not condition:
            dut._log.error(f"Expected value: {o} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {i}: inA={ia} inB={ib} inS={iS}"
        await Timer(Decimal(1), units="ns")


def test_GENERIC_MUX_4X1():
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
    test_GENERIC_MUX_4X1()
