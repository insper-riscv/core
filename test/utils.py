from inspect import isclass
import os
import typing as T
import subprocess
from pathlib import Path

import cocotb.binary
import cocotb.handle
import cocotb.log
import cocotb.runner


_TESTCASE_TYPE = T.Union[
    T.Callable[["DUT"], None], T.Sequence[T.Callable[["DUT"], None]]
]
_BUILT: T.List[str] = []

runner = cocotb.runner.get_runner("ghdl")


class DUT(T.Type[cocotb.handle.HierarchyObject]):
    _log: T.Any

    class Input_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: cocotb.binary.BinaryValue

    class Output_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: T.Final[cocotb.binary.BinaryValue]  # type: ignore

    @staticmethod
    def _get_testcase_names(case: _TESTCASE_TYPE):
        if isinstance(case, list):
            return [case.__name__ for case in case]

        return case.__name__

    @classmethod
    def _get_children(cls):
        children: T.Set[T.Type[DUT]] = set()

        for key in dir(cls):
            if key.startswith("_"):
                continue

            value = getattr(cls, key)

            if not isclass(value):
                continue

            if issubclass(value, DUT):
                children.add(value)

        return children

    @classmethod
    def build_vhd(cls):
        for child in cls._get_children():
            if child.__name__ in _BUILT:
                continue

            child.build_vhd()
            _BUILT.append(child.__name__)

        runner.build(
            always=True,
            build_args=["--std=08"],
            vhdl_sources=[
                "src/TOP_LEVEL_CONSTANTS.vhd",
                f"src/{cls.__name__}.vhd",
            ],
            hdl_toplevel=cls.__name__.lower(),
            hdl_library="work",
        )

    @classmethod
    def build_netlistsvg(cls, filename: T.Optional[str] = None):
        if filename is not None:
            Path(filename).mkdir(exist_ok=True)

        entity = cls.__name__.lower()

        print(True, os.getcwd())

        exit_code = subprocess.call(
            [
                "yosys",
                "-m",
                "ghdl",
                "-p",
                f"ghdl --work=top {entity}; prep -top {cls.__name__}; aigmap; write_json -compat-int {entity}.json",
            ],
            cwd="sim_build",
        )

        if exit_code != 0:
            raise SystemError("Failed to build synthesis!")

        exit_code = subprocess.call(
            [
                "netlistsvg",
                f"{entity}.json",
                "-o",
                filename or f"{entity}_netlist.svg",
            ],
            cwd="sim_build",
        )

        if exit_code != 0:
            raise SystemError("Failed to build NetList SVG!")

    @classmethod
    def test_with(
        cls,
        testcase: _TESTCASE_TYPE,
        parameters: T.Mapping[str, object] = {},
    ):
        runner.test(
            hdl_toplevel=cls.__name__.lower(),
            test_args=["--std=08"],
            test_module="test_" + cls.__name__,
            testcase=DUT._get_testcase_names(testcase),
            parameters=parameters,
            hdl_toplevel_lang="vhdl",
            hdl_toplevel_library="work",
            waves=True,
        )


def assert_output(pin: T.Type[DUT.Output_pin], value: str, message: str = ""):
    condition = pin.value.binstr == value

    assert condition, f"Expected {value} and obtained {pin.value.binstr}. {message}"
