import pytest

import lib
from test_GENERICS_package import GENERICS


class RV32I(lib.Package):
    children = [
        GENERICS
    ]


@pytest.mark.synthesis
def test_RV32I_package_synthesis():
    RV32I.build_vhd()


if __name__ == "__main__":
    lib.run_test(__file__)
