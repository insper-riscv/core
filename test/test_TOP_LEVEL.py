from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_STAGE_IF import STAGE_IF
from test_STAGE_ID import STAGE_ID
from test_STAGE_EX import STAGE_EX
from test_STAGE_MEM import STAGE_MEM
from test_STAGE_WB import STAGE_WB


class TOP_LEVEL(utils.DUT):
    CHILDREN = [STAGE_IF, STAGE_ID, STAGE_EX, STAGE_MEM, STAGE_WB]


def test_TOP_LEVEL_syntesis():
    TOP_LEVEL.build_vhd()
    TOP_LEVEL.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_TOP_LEVEL"])
