import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tb_and(dut):
    inA = [0, 0, 1, 1]
    inB = [0, 1, 0, 1]
    out = [0, 0, 0, 1]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units='ns')
        condition = (dut.result.value == out[i])
        if not condition:
            dut._log.error(f"Expected value: {out[i]} Obtained value: {dut.result.value}" )
            assert condition, f"Error in test {i}"
        await Timer(1, units='ns')