import os
import subprocess
import json
import typing as T
from fractions import Fraction
from pathlib import Path
from inspect import isclass

import pytest_check as check
import cocotb.binary
import cocotb.handle
import cocotb.runner
import cocotb.triggers

import lib
from lib.package import Package
from lib.waveform import Waveform


_TESTCASE_TYPE = T.Union[
    T.Callable[["Entity", Waveform], T.AsyncGenerator[bool, T.Any]],
    list[T.Callable[["Entity", Waveform], T.AsyncGenerator[bool, T.Any]]],
]

runner = cocotb.runner.get_runner("ghdl")

class Entity(T.Type[cocotb.handle.HierarchyObject]):
    _package: T.Union[T.Type[Package], None] = None

    class Input_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: cocotb.binary.BinaryValue

    class Output_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: T.Final[cocotb.binary.BinaryValue]  # type: ignore

    class Signal(T.Type[cocotb.handle.ModifiableObject]):
        value: T.Final[cocotb.binary.BinaryValue]  # type: ignore

    @staticmethod
    def _get_testcase_names(case: _TESTCASE_TYPE):
        if isinstance(case, list):
            return [case.__name__ for case in case]

        return case.__name__ # type: ignore

    @classmethod
    def testcase(cls, fn):
        @cocotb.test() # type: ignore
        async def _testcase_wrapper(dut: "Entity"):
            signals = [
                getattr(dut, key)
                for key in dir(dut)
                if not key.startswith("_")
                and key != "clock"
                and isinstance(getattr(dut, key), cocotb.handle.ModifiableObject)
            ]

            if hasattr(dut, "clock"):
                tracer = Waveform(*signals, clock=dut.clock, model=cls) # type: ignore
            else:
                tracer = Waveform(*signals, clock=None, model=cls) # type: ignore

            tracer.set_title(fn.__name__)

            with tracer as trace:
                await tracer.start()

                pased = all([result async for result in fn(dut, trace)])

                if trace.enabled:
                    trace.write(f"../sim_build/{fn.__name__.lower()}.svg")

                if not pased:
                    message = "\n".join(check.check_log.get_failures()) # type: ignore

                    raise AssertionError(message)

        _testcase_wrapper.__name__ = fn.__name__

        return _testcase_wrapper

    @classmethod
    def _get_input_pins(cls):
        children: T.Set[str] = set()

        for key in dir(cls):
            if key.startswith("_"):
                continue

            value = getattr(cls, key)

            if value == Entity.Input_pin:
                children.add(key)

        return children

    @classmethod
    def _get_output_pins(cls):
        children: T.Set[str] = set()

        for key in dir(cls):
            if key.startswith("_"):
                continue

            value = getattr(cls, key)

            if value == Entity.Output_pin:
                children.add(key)

        return children

    @classmethod
    def _get_children(cls):
        children: T.Set[T.Type[Entity]] = set()

        for key in dir(cls):
            if key.startswith("_"):
                continue

            value = getattr(cls, key)

            if not isclass(value):
                continue

            if issubclass(value, Entity):
                children.add(value)

        return children

    @staticmethod
    def _normalize_netlist_keys(filename):
        def rename_keys(obj):
            if isinstance(obj, dict):
                for key in list(obj.keys()):
                    new_key = key.replace(".", " ")
                    obj[new_key] = obj.pop(key)

                    if isinstance(obj[new_key], (dict, list)):
                        rename_keys(obj[new_key])
            elif isinstance(obj, list):
                for item in obj:
                    rename_keys(item)

        with open(filename, "r") as text_file:
            design = json.load(text_file)

        rename_keys(design)

        with open(filename, "w") as text_file:
            json.dump(design, text_file, indent=4)

    @classmethod
    def build_vhd(cls):
        if cls._package is not None:
            cls._package.build_vhd()

        for child in cls._get_children():

            child.build_vhd()

        runner.build(
            always=True,
            build_args=["--std=08"],
            vhdl_sources=[
                f"src/{cls.__name__}.vhd"
            ],
            hdl_toplevel=cls.__name__.lower(),
        )

    @classmethod
    def build_netlistsvg(cls, filename: T.Optional[str] = None):
        if filename is not None:
            Path(filename).mkdir(exist_ok=True)

        entity = cls.__name__.lower()

        os.makedirs("sim_build", exist_ok=True)

        process = subprocess.Popen(
            [
                "yosys",
                "-m",
                "ghdl",
                "-p",
                f"ghdl --std=08 --work=top {entity}; prep -top {cls.__name__}; write_json -compat-int {entity}.json",
            ],
            cwd="sim_build",
            stdout=subprocess.PIPE,
        )

        outs, errs = process.communicate(timeout=60)

        assert process.returncode == 0, outs.decode()

        cls._normalize_netlist_keys(f"sim_build/{entity}.json")

        process = subprocess.Popen(
            [
                "netlistsvg",
                f"{entity}.json",
                "-o",
                filename or f"{entity}_netlist.svg",
                "--skin",
                f"{lib.WORKSPACE_FOLDER}/data/netlistsvg/digital.svg",
            ],
            cwd="sim_build",
            stdout=subprocess.PIPE,
        )

        outs, errs = process.communicate(timeout=30)

        assert process.returncode == 0, outs.decode()

    @classmethod
    def test_with(
        cls,
        testcase: T.Any,
        parameters: T.Mapping[str, object] = {},
    ):
        with check.check() as context:
            context.set_max_fail(1)
            runner.test(
                hdl_toplevel=cls.__name__.lower(),
                test_args=["--std=08"],
                test_module="test_" + cls.__name__,
                testcase=Entity._get_testcase_names(testcase),
                parameters=parameters,
                hdl_toplevel_lang="vhdl",
            )

            if check.any_failures():
                assert False
