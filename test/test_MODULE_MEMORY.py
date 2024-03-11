from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_GENERIC_RAM import GENERIC_RAM


class MODULE_MEMORY(utils.DUT):
    CHILDREN = [GENERIC_RAM]


def test_MODULE_MEMORY_syntesis():
    MODULE_MEMORY.build_vhd()
    MODULE_MEMORY.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_MODULE_MEMORY"])
