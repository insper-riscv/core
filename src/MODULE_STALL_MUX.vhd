library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_STALL_MUX is

    port (
        control_ex_in    : in  WORK.CPU.t_CONTROL_EX;
        control_mem_in   : in  WORK.CPU.t_CONTROL_MEM;
        control_wb_in    : in  WORK.CPU.t_CONTROL_WB;
        selector         : in  std_logic := '0';
        control_ex_out   : out WORK.CPU.t_CONTROL_EX;
        control_mem_out  : out WORK.CPU.t_CONTROL_MEM;
        control_wb_out   : out WORK.CPU.t_CONTROL_WB
    );

end entity;

architecture RTL of MODULE_STALL_MUX is

    constant control_ex  : WORK.CPU.t_CONTROL_EX  := WORK.CPU.NULL_CONTROL_EX;
    constant control_mem : WORK.CPU.t_CONTROL_MEM := WORK.CPU.NULL_CONTROL_MEM;
    constant control_wb  : WORK.CPU.t_CONTROL_WB  := WORK.CPU.NULL_CONTROL_WB;

begin

    control_ex_out <= control_ex_in when selector = '0' else
                      control_ex;

    control_mem_out <= control_mem_in when selector = '0' else
                       control_mem;

    control_wb_out <= control_wb_in when selector = '0' else
                      control_wb;

end architecture;
