# from cocotb_test.simulator import run
import cocotb
import cocotb.runner
import cocotb._vendor

import find_libpython

find_libpython.find_libpython

# import os


# def source(name):
#     dir = os.path.dirname(os.path.dirname(__file__))
#     dir = os.path.join(dir, "src")
#     return os.path.join(dir, name)


def test_and():
    runner = cocotb.runner.get_runner("questa")
    
    runner.build(
        vhdl_sources=["src/GENERIC_AND.vhd"],
        build_dir="quartus/simulation/sim_build",
        hdl_toplevel="GENERIC_AND",
    )
    runner.test(
        hdl_toplevel="GENERIC_AND",
        test_module="tests_and",
        testcase="tb_and",
        hdl_toplevel_lang="vhdl",
    )

    # run(
    #     verilog_sources=[],
    #     vhdl_sources=["src/GENERIC_AND.vhd"],
    #     toplevel="GENERIC_AND",
    #     module="tests_and",
    #     testcase='tb_and',
    #     toplevel_lang="vhdl"
    # )


if __name__ == "__main__":
    test_and()
