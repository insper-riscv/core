import os
from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_PC import MODULE_PC
from test_MODULE_ROM import MODULE_ROM


class STAGE_IF(utils.DUT):
    CHILDREN = [MODULE_PC, MODULE_ROM]


def test_STAGE_IF_synthesis():
    STAGE_IF.build_vhd()
    # STAGE_IF.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
