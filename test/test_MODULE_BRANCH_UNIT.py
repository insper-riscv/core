import pytest

import lib
from test_MODULES_package import MODULES


class MODULE_BRANCH_UNIT(lib.Device):
    _package = MODULES


@pytest.mark.synthesis
def test_MODULE_BRANCH_UNIT_synthesis():
    MODULE_BRANCH_UNIT.build_vhd()
    # MODULE_BRANCH_UNIT.build_netlistsvg()


if __name__ == "__main__":
    lib.run_test(__file__)
