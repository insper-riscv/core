import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer
from cocotb_test.simulator import run
from utils import source


@cocotb.test()
async def tb_mux_4x1(dut):
    inA = [
        BinaryValue('00001111000011110000111100001111'),
        BinaryValue('00001111000011110000111100001111'),
        BinaryValue('00001111000011110000111100001111'),
        BinaryValue('00001111000011110000111100001111')
    ]
    inB = [
        BinaryValue('11110000111100001111000011110000'),
        BinaryValue('11110000111100001111000011110000'),
        BinaryValue('11110000111100001111000011110000'),
        BinaryValue('11110000111100001111000011110000')
    ]
    inC = [
        BinaryValue('00000000111111111111111100000000'),
        BinaryValue('00000000111111111111111100000000'),
        BinaryValue('00000000111111111111111100000000'),
        BinaryValue('00000000111111111111111100000000')
    ]
    inD = [
        BinaryValue('11111111000000000000000011111111'),
        BinaryValue('11111111000000000000000011111111'),
        BinaryValue('11111111000000000000000011111111'),
        BinaryValue('11111111000000000000000011111111')
    ]
    inS = [
        BinaryValue('00'),
        BinaryValue('01'),
        BinaryValue('10'),
        BinaryValue('11')
    ]
    out = [
        BinaryValue('00001111000011110000111100001111'),
        BinaryValue('11110000111100001111000011110000'),
        BinaryValue('00000000111111111111111100000000'),
        BinaryValue('11111111000000000000000011111111')
    ]

    for i, (ia, ib, ic, iD, iS, o) in enumerate(zip(inA, inB, inC, inD, inS, out)):
        dut.a.value = ia
        dut.b.value = ib
        dut.c.value = ic
        dut.d.value = iD
        dut.s.value = iS

        await Timer(1, units='ns')

        condition = (dut.q.value.binstr == o.binstr)

        if not condition:
            dut._log.error(
                f"Expected value: {o.binstr} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {i}: inA={ia.binstr} inB={ib.binstr} inS={iS.binstr}"
        await Timer(1, units='ns')


def test_mux_4x1():
    run(vhdl_sources=[source("GENERIC_MUX_4X1.vhd")],
        toplevel="generic_mux_4x1",
        module="test_mux_4x1",
        testcase='tb_mux_4x1',
        toplevel_lang="vhdl")


if __name__ == "__main__":
    test_mux_4x1()
