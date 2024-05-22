import pytest

import lib


class GENERICS(lib.Package):
    pass


@pytest.mark.synthesis
def test_GENERICS_package_synthesis():
    GENERICS.build_vhd()


if __name__ == "__main__":
    lib.run_test(__file__)
