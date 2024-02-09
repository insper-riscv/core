from cocotb_test.simulator import run

import os


def source(name):
    dir = os.path.dirname(os.path.dirname(__file__))
    dir = os.path.join(dir, "src")    
    return os.path.join(dir, name)

def test_and():
    run(vhdl_sources=[source("and_gate.vhd")], 
        toplevel="and_gate",
        module="tests_cocotb", 
        testcase='tb_and', 
        toplevel_lang="vhdl")  
    
if __name__ == "__main__":
    test_and()