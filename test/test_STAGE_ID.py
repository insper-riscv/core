from decimal import Decimal

import pytest
import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer

import utils
from test_MODULE_REGISTER_FILE import MODULE_REGISTER_FILE
from test_MODULE_CONTROL_UNIT import MODULE_CONTROL_UNIT

class STAGE_ID(utils.DUT):
    CHILDREN = [MODULE_REGISTER_FILE, MODULE_CONTROL_UNIT]


def test_STAGE_ID_syntesis():
    STAGE_ID.build_vhd()
    #STAGE_ID.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", f"test_STAGE_ID"])
