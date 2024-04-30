import re
import subprocess
import typing as T
from pathlib import Path

from cocotb.binary import BinaryValue

import lib


class Program:
    ENVIRONMENT_CALL = "00000000000000000000000001110011"
    ENVIRONMENT_BREAKPOINT = "00000000000100000000000001110011"

    def __init__(self, filename: str, dependencies: T.List[str] = [], basedir: str = "sim_build", stepping: bool = False):
        self.entry = Path(filename)
        self.dependencies = dependencies
        self.basedir = basedir
        self.stepping = stepping

    def enable_stepping(self):
        self.stepping = True

    def disable_stepping(self):
        self.stepping = False

    def get_memory_map(self):
        elf = self._build_program_executable()
        bins = self._build_program_dump(elf)
        dump = self._get_program_dump(bins)

        return self._get_program_binaries(dump)

    async def attach_device(self, trace: lib.Waveform, address: T.Type[lib.Entity.Output_pin], data: T.Type[lib.Entity.Input_pin]):
        mem_map = self.get_memory_map()
        index = 0

        while True:
            key = address.value.integer

            try:
                value = mem_map[key]
            except KeyError:
                break

            data.value = BinaryValue(value)

            if self.stepping or value == Program.ENVIRONMENT_BREAKPOINT:
                yield index, key

                index += 1

            await trace.cycle()

    def _build_program_executable(self):
        output = Path(self.entry.with_suffix('.out').name)
        process = subprocess.Popen(
            [
                "riscv32-unknown-elf-gcc",
                "-T",
                "../test/data/gcc/linker.ld",
                "-nostartfiles",
                "../test/data/gcc/start.S",
                "-fno-exceptions",
                "-nolibc",
                "-nostdlib",
                "-O3",
                str(self.entry),
                *self.dependencies,
                "-o",
                output,
            ],
            stdout=subprocess.PIPE,
        )
        outs, errs = process.communicate(timeout=60)

        assert process.returncode == 0, outs.decode()
        return output

    @staticmethod
    def _build_program_dump(elf_file: Path):
        output = elf_file.with_suffix('.bin')
        process = subprocess.Popen(
            [
                "riscv32-unknown-elf-objcopy",
                "-O",
                "binary",
                elf_file,
                output,
            ],
            stdout=subprocess.PIPE,
        )
        outs, errs = process.communicate(timeout=60)

        assert process.returncode == 0, outs.decode()
        return output

    @staticmethod
    def _get_program_dump(bins_file: Path):
        process = subprocess.Popen(
            [
                "xxd",
                "-g",
                "4",
                "-c",
                "4",
                "-e",
                "-u",
                f"{bins_file.with_suffix('.bin').name}",
            ],
            stdout=subprocess.PIPE,
        )

        outs, errs = process.communicate(timeout=60)

        assert process.returncode == 0, outs.decode()

        return outs.decode()

    @staticmethod
    def _get_program_binaries(dump: str):
        memory_map: T.Dict[int, str] = {}

        for line in dump.split("\n"):
            if len(line) == 0:
                continue

            address, hex_dump, *_ = re.split(r":?\s+", line)
            key = int(address, base=16)
            memory_map[key] = lib.to_binstr(int(hex_dump, base=16), 32)

        return memory_map
