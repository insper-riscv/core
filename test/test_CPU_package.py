import pytest

import lib
from test_RV32I_package import RV32I
from test_GENERICS_package import GENERICS


class CPU(lib.Package):
    children = [
        RV32I,
        GENERICS,
    ]


@pytest.mark.synthesis
def test_CPU_package_synthesis():
    CPU.build_vhd()


if __name__ == "__main__":
    lib.run_test(__file__)
