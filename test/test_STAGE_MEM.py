from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_MEMORY import MODULE_MEMORY


class STAGE_MEM(utils.DUT):
    CHILDREN = [MODULE_MEMORY]


def test_STAGE_MEM_syntesis():
    STAGE_MEM.build_vhd()
    STAGE_MEM.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_STAGE_MEM"])
