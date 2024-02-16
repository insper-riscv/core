import typing as T

import cocotb.log
import cocotb.binary
import cocotb.handle



class DUT(T.Type[cocotb.handle.HierarchyObject]):
    _log: T.Any
    pass

    class Input_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: cocotb.binary.BinaryValue


    class Output_pin(T.Type[cocotb.handle.ModifiableObject]):
        value: T.Final[cocotb.binary.BinaryValue] # type: ignore
