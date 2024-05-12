import pytest

import lib
from test_CPU_package import CPU
from test_CPU_STAGE_IF import CPU_STAGE_IF
from test_CPU_STAGE_ID import CPU_STAGE_ID
from test_CPU_STAGE_EX import CPU_STAGE_EX
from test_CPU_STAGE_MEM import CPU_STAGE_MEM
from test_CPU_STAGE_WB import CPU_STAGE_WB


class CPU_TOP_LEVEL(lib.Entity):
    _package = CPU

    clock = lib.Entity.Input_pin
    clear = lib.Entity.Input_pin
    enable = lib.Entity.Input_pin
    data_program = lib.Entity.Input_pin
    data_memory_in = lib.Entity.Input_pin
    data_memory_out = lib.Entity.Output_pin
    address_program = lib.Entity.Output_pin
    address_memory = lib.Entity.Output_pin
    memory_read = lib.Entity.Output_pin
    memory_write = lib.Entity.Output_pin

    instruction_fetch = CPU_STAGE_IF
    instruction_decode = CPU_STAGE_ID
    execute = CPU_STAGE_EX
    memory_access = CPU_STAGE_MEM
    write_back = CPU_STAGE_WB


@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_ADDI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_ADDI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000010",
        "00000000000000000000000000000100",
        "00000000000000000000000000001000",
        "00000000000000000000000000010000",
        "00000000000000000000000000100000",
        "00000000000000000000000001000000",
        "00000000000000000000000010000000",
        "00000000000000000000000100000000",
        "00000000000000000000000100000001",
        "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_ADD(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_ADD.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SUB(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SUB.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000100",
        "00000000000000000000000000000010",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_BEQ(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_BEQ.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_BNE(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_BNE.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_BLT(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_BLT.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_BLTU(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_BLTU.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_BGE(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_BGE.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_BGEU(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_BGEU.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000010",
        "00000000000000000000000000000001",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000111",
        "00000000000000000000000000000011",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_LUI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_LUI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000001000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_AUIPC(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_AUIPC.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000001000000000100",
        "00000000000000000001000000001000",
        "00000000000000000001000000001100",
        "00000000000000000001000000010000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLT(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SLT.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "01000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000111",
        "00000000000000000000000000001001",
        "10000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLTI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SLTI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "10000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "01000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLTU(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SLTU.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "01000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000111",
        "00000000000000000000000000001001",
        "10000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLTIU(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SLTIU.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "10000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "01000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000001",
        "00000000000000000000000000000001",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_JAL(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_JAL.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000010001",
        "00000000000000000000000000011100",
        "00000000000000000000000000000000",
        "00000000000000000000000000001100",
        "00000000000000000000000000010000",
        "00000000000000000000000000010001",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_JALR(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_JALR.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000011100",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000011100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_LB(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_LB.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000010000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "11111111111111111111111110000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111111111111111110000010",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_LBU(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_LBU.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000010000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000010000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000010000010",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_LH(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_LH.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000001000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "11111111111111111000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111111111000000000000010",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_LHU(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_LHU.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000001000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000001000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000001000000000000010",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_LW(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_LW.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001100",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000010000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001100",
        "00000000000000000000000000010000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001100",
        "00000000000000000000000000010000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_XOR(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_XOR.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_XORI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_XORI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_AND(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_AND.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "00000000000000000000000000000110",
        "00000000000000000000000000000101",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000101",
        "00000000000000000000000000000100",
        "00000000000000000000000000000101",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_ANDI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_ANDI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "00000000000000000000000000000110",
        "00000000000000000000000000000101",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_OR(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_OR.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000111",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_ORI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_ORI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "11111111111000000000000000000000",
        "11111111111000000000000000000111",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
        "11111111111000000000000000000111",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLL(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SLL.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000100000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000100000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SLLI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SLLI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000010000000",
        "00000000000000000000000010000000",
        "00000000000000000000000000000000",
        "00000000000000000000000010000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRL(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SRL.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000100000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRLI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SRLI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000100000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRA(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SRA.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000100000000",
        "00000000000000000000000000000110",
        "00000000000000000000000000000100",
        "00000000000000000001000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000001000000",
        "10000000000000000000000000000000",
        "11111110000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SRAI(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SRAI.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000100000000",
        "00000000000000000000000000000100",
        "00000000000000000000000000000100",
        "00000000000000000001000000000000",
        "00000000000000000000000001000000",
        "00000000000000000000000001000000",
        "10000000000000000000000000000000",
        "11111110000000000000000000000000",
        "11111110000000000000000000000000",
        "00000000000000000000000000000100",
        "00000000000000000000000001000000",
        "11111110000000000000000000000000",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SB(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SB.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000001001111111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000001111111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000010000001",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SH(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SH.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000011000000000000000",
        "00000000000000000000000000001000",
        "00000000000000011000001001111111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000001000001001111111",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000001000001010000001",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@CPU_TOP_LEVEL.testcase
async def tb_CPU_TOP_LEVEL_SW(dut: CPU_TOP_LEVEL, trace: lib.Waveform):
    program = lib.Program("../test/data/c/testcase_SW.c", stepping=True)
    values_destination = [
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001000",
        "00000000000000000000000000001000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000000000",
        "00000000000000000000000000001010",
        "00000000000000000000000000000000",
    ]

    program.attach_memory(dut.memory_read, dut.memory_write, dut.address_memory, dut.data_memory_out, dut.data_memory_in)
    trace.set_scale(2)
    await trace.cycle()

    async for index, address in program.attach_device(trace, dut.address_program, dut.data_program):
        yield trace.check(dut.write_back.destination, values_destination[index], f"At clock {index} (PC = {address}).")

        if index == len(values_destination):
            break

@pytest.mark.synthesis
def test_CPU_TOP_LEVEL_synthesis():
    CPU_TOP_LEVEL.build_vhd()
    CPU_TOP_LEVEL.build_netlistsvg()


@pytest.mark.testcases
def test_CPU_TOP_LEVEL_arithmetic_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_ADDI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_ADD,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SUB,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_branch_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_BEQ,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_BNE,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_BLT,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_BLTU,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_BGE,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_BGEU,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_build_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_LUI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_AUIPC,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_compare_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SLT,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SLTI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SLTU,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SLTIU,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_jump_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_JAL,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_JALR,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_load_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_LB,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_LBU,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_LH,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_LHU,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_LW,
        ]
    )


@pytest.mark.testcases
def test_CPU_TOP_LEVEL_logical_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_XOR,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_XORI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_AND,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_ANDI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_OR,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_ORI,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_shifting_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SLL,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SLLI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SRL,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SRLI,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SRA,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SRAI,
        ]
    )

@pytest.mark.testcases
def test_CPU_TOP_LEVEL_store_testcases():
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SB,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SH,
        ]
    )
    CPU_TOP_LEVEL.test_with(
        [
            tb_CPU_TOP_LEVEL_SW,
        ]
    )

if __name__ == "__main__":
    lib.run_test(__file__)
