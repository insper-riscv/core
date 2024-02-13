import cocotb
from cocotb.triggers import Timer
from cocotb_test.simulator import run
from utils import source


@cocotb.test()
async def tb_alu(dut):
    inA = [0, 0, 1, 1]
    inB = [1, 1, 1, 1]
    inS = [0, 1, 0, 1]
    out = [-1, 1, 0, 2]

    for i, (ia, ib, iS, o) in enumerate(zip(inA, inB, inS, out)):
        dut.a.value = ia
        dut.b.value = ib
        dut.s.value = iS

        await Timer(1, units='ns')

        condition = (dut.q.value == o)

        if not condition:
            dut._log.error(
                f"Expected value: {o} Obtained value: {dut.q.value}")

        assert condition, f"Error in test {i}"
        await Timer(1, units='ns')


def test_alu():
    run(vhdl_sources=[source("ALU.vhd")],
        toplevel="alu",
        module="test_alu",
        testcase='tb_alu',
        toplevel_lang="vhdl")


if __name__ == "__main__":
    test_alu()
