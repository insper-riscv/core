import os

import pytest

import utils
from test_MODULES_package import MODULES


class MODULE_BRANCH_UNIT(utils.DUT):
    _package = MODULES


@pytest.mark.synthesis
def test_MODULE_BRANCH_UNIT_synthesis():
    MODULE_BRANCH_UNIT.build_vhd()
    # MODULE_BRANCH_UNIT.build_netlistsvg()


if __name__ == "__main__":
    pytest.main(["-k", os.path.basename(__file__)])
