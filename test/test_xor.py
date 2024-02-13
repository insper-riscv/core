import cocotb
from cocotb.triggers import Timer
from cocotb_test.simulator import run
from utils import source


@cocotb.test()
async def tb_xor(dut):
    inA = [0, 0, 1, 1]
    inB = [0, 1, 0, 1]
    out = [0, 1, 1, 0]

    for i, (ia, ib, o) in enumerate(zip(inA, inB, out)):
        dut.a.value = ia
        dut.b.value = ib

        await Timer(1, units='ns')

        condition = (dut.q.value == o)

        if not condition:
            dut._log.error(
                f"Expected value: {o} Obtained value: {dut.q.value}")

        assert condition, f"Error in test {i}"
        await Timer(1, units='ns')


def test_xor():
    run(vhdl_sources=[source("GENERIC_XOR.vhd")],
        toplevel="generic_xor",
        module="test_xor",
        testcase='tb_xor',
        toplevel_lang="vhdl")


if __name__ == "__main__":
    test_xor()
