import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer
from cocotb_test.simulator import run
from utils import source


@cocotb.test()
async def tb_RV32I_ALU(dut):
    inA = [
        BinaryValue('0000'),
        BinaryValue('0000'),
        BinaryValue('0001'),
        BinaryValue('0001')
    ]
    inB = [
        BinaryValue('0001'),
        BinaryValue('0001'),
        BinaryValue('0001'),
        BinaryValue('0001')
    ]
    inS = [
        BinaryValue('00'),
        BinaryValue('01'),
        BinaryValue('00'),
        BinaryValue('01')
    ]
    out = [
        BinaryValue('1111'),
        BinaryValue('0001'),
        BinaryValue('0000'),
        BinaryValue('0010')
    ]

    for i, (ia, ib, iS, o) in enumerate(zip(inA, inB, inS, out)):
        dut.a.value = ia
        dut.b.value = ib
        dut.s.value = iS

        await Timer(1, units='ns')

        condition = (dut.q.value.binstr == o.binstr)

        if not condition:
            dut._log.error(
                f"Expected value: {o.binstr} Obtained value: {dut.q.value.binstr}")

        assert condition, f"Error in test {i}: inA={ia.binstr} inB={ib.binstr} inS={iS.binstr}"
        await Timer(1, units='ns')


def test_RV32I_ALU():
    run(vhdl_sources=[source("RV32I_ALU.vhd")],
        toplevel="rv32i_alu",
        module="test_RV32I_ALU",
        testcase='tb_RV32I_ALU',
        toplevel_lang="vhdl")


if __name__ == "__main__":
    test_RV32I_ALU()
