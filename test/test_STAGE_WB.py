from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_WRITE_BACK import MODULE_WRITE_BACK


class STAGE_WB(utils.DUT):
    CHILDREN = [MODULE_WRITE_BACK]


def test_STAGE_WB_syntesis():
    STAGE_WB.build_vhd()
    STAGE_WB.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_STAGE_WB"])
