import cocotb
from cocotb.binary import BinaryRepresentation, BinaryValue
from cocotb.triggers import Timer
from cocotb_test.simulator import run
from utils import source


@cocotb.test()
async def tb_and(dut):
    inA = [
        BinaryValue('0'),
        BinaryValue('0'),
        BinaryValue('1'),
        BinaryValue('1')
    ]
    inB = [
        BinaryValue('0'),
        BinaryValue('1'),
        BinaryValue('0'),
        BinaryValue('1')
    ]
    out = [
        BinaryValue('0'),
        BinaryValue('0'),
        BinaryValue('0'),
        BinaryValue('1')
    ]

    for i, (ia, ib, o) in enumerate(zip(inA, inB, out)):
        dut.a.value = ia
        dut.b.value = ib

        await Timer(1, units='ns')

        condition = (dut.q.value.binstr == o.binstr)

        if not condition:
            dut._log.error(
                f"Expected value: {o.binstr} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {i}: inA={ia.binstr} inB={ib.binstr}"
        await Timer(1, units='ns')


def test_and():
    run(vhdl_sources=[source("GENERIC_AND.vhd")],
        toplevel="generic_and",
        module="test_and",
        testcase='tb_and',
        toplevel_lang="vhdl")


if __name__ == "__main__":
    test_and()
