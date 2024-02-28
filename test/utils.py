import typing as T

import cocotb.binary
import cocotb.handle
import cocotb.log
import cocotb.runner


_TESTCASE_TYPE = T.Callable[["DUT"], None] | T.Sequence[T.Callable[["DUT"], None]]
_BUILT: T.List[str] = []

runner = cocotb.runner.get_runner("ghdl")


class DUT(T.Type[cocotb.handle.HierarchyObject]):
    CHILDREN: T.List[T.Type["DUT"]] = []
    _log: T.Any

    class Input_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: cocotb.binary.BinaryValue

    class Output_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: T.Final[cocotb.binary.BinaryValue] # type: ignore

    @staticmethod
    def _get_testcase_names(case: _TESTCASE_TYPE):
        if isinstance(case, list):
            return [case.__name__ for case in case]
        else:
            return case.__name__
    
    @classmethod
    def build_vhd(cls):
        for child in cls.CHILDREN:
            if child.__name__ in _BUILT:
                continue

            child.build_vhd()
            _BUILT.append(child.__name__)

        runner.build(
            vhdl_sources=[f"src/{cls.__name__}.vhd"],
            hdl_toplevel=cls.__name__.lower(),
            always=True,
        )

    @classmethod
    def test_with(cls, testcase: _TESTCASE_TYPE, parameters: T.Mapping[str, object] | None= None):
        runner.test(
            hdl_toplevel=cls.__name__.lower(),
            test_module="test_" + cls.__name__,
            testcase=DUT._get_testcase_names(testcase),
            parameters=parameters, # type: ignore
            hdl_toplevel_lang="vhdl",
        )
