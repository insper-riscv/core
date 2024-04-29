import pytest

import lib


class RV32M(lib.Package):
    pass


@pytest.mark.synthesis
def test_RV32M_package_synthesis():
    RV32M.build_vhd()


if __name__ == "__main__":
    lib.run_test(__file__)
