import math
import re
import subprocess
import typing as T
from pathlib import Path

from cocotb.binary import BinaryValue

import lib


class Program:
    ENVIRONMENT_CALL = "00000000000000000000000001110011"
    ENVIRONMENT_BREAKPOINT = "00000000000100000000000001110011"

    memory_enable_pin: T.Union[T.Type[lib.Entity.Output_pin], None]
    memory_enable_read_pin: T.Union[T.Type[lib.Entity.Output_pin], None]
    memory_enable_write_pin: T.Union[T.Type[lib.Entity.Output_pin], None]
    memory_address_pin: T.Union[T.Type[lib.Entity.Output_pin], None]
    memory_source_pin: T.Union[T.Type[lib.Entity.Output_pin], None]
    memory_destination_pin: T.Union[T.Type[lib.Entity.Input_pin], None]
    memory: T.Union[T.Dict[int, str], None]

    def __init__(self, filename: str, dependencies: T.List[str] = [], stepping: bool = False):
        self.entry = Path(filename)
        self.dependencies = dependencies
        self.stepping = stepping
        self.memory_enable_pin = None
        self.memory_enable_read_pin = None
        self.memory_enable_write_pin = None
        self.memory_address_pin = None
        self.memory_source_pin = None
        self.memory_destination_pin = None
        self.memory = None

    def enable_stepping(self):
        self.stepping = True

    def disable_stepping(self):
        self.stepping = False

    def get_memory_map(self):
        elf = self._build_program_executable()
        bins = self._build_program_dump(elf)
        dump = self._get_program_dump(bins)

        elf.unlink()
        bins.unlink()

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

            if self.memory is not None:
                memory_address = self.memory_address_pin.value.integer # type: ignore

                if self.memory_enable_read_pin.value.binstr == "1": # type: ignore
                    if memory_address in self.memory:
                        self.memory_destination_pin.value = BinaryValue(self.memory[memory_address]) # type: ignore
                    else:
                        self.memory_destination_pin.value = BinaryValue("0" * len(self.memory_destination_pin.value.binstr)) # type: ignore
                else:
                    self.memory_destination_pin.value = BinaryValue("Z" * len(self.memory_destination_pin.value.binstr)) # type: ignore

                if self.memory_enable_write_pin.value.binstr == "1": # type: ignore
                    self.memory[memory_address] = self.memory_source_pin.value.binstr # type: ignore

            if self.stepping or value == Program.ENVIRONMENT_BREAKPOINT:
                yield index, key

                index += 1
            elif value == Program.ENVIRONMENT_CALL:    
                await trace.cycle()
                break

            await trace.cycle()

    def attach_memory(
            self,
            enable_read: T.Type[lib.Entity.Output_pin],
            enable_write: T.Type[lib.Entity.Output_pin],
            address: T.Type[lib.Entity.Output_pin],
            source: T.Type[lib.Entity.Output_pin],
            destination: T.Type[lib.Entity.Input_pin]
    ):
        self.memory_enable_read_pin = enable_read
        self.memory_enable_write_pin = enable_write
        self.memory_address_pin = address
        self.memory_source_pin = source
        self.memory_destination_pin = destination
        self.memory = {}

    def to_memory_initialization_file(self, width: int, depth: int):
        mem = {
            key: value
            for key, value in self.get_memory_map().items()
        }
        argmax = max(mem.keys())
        pad_size = math.floor(math.log10(argmax) + 1)
        bins = [
            f"    {key:0{pad_size}}: {value};"
            for key, value in mem.items()
        ]

        if width is None:
            width = len(mem.get(0)) # type: ignore

        if depth is None:
            depth = len(bins)

        return "\n".join([
            f"WIDTH={width};",
            f"DEPTH={depth};",
            "ADDRESS_RADIX=DEC;",
            "DATA_RADIX=BIN;\n",
            "CONTENT BEGIN",
            *bins,
            "END;\n",
        ])

    def _build_program_executable(self):
        output = Path(self.entry.with_suffix('.out').name)
        process = subprocess.Popen(
            [
                "riscv32-unknown-elf-gcc",
                "-T",
                f"{lib.WORKSPACE_FOLDER}/data/gcc/linker.ld",
                "-nostartfiles",
                f"{lib.WORKSPACE_FOLDER}/data/gcc/start.S",
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
