library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity CPU_EXECUTION_FORWARDING_UNIT is

    port (
        stage_ex_select_source_1     : in  WORK.CPU.t_REGISTER;
        stage_ex_select_source_2     : in  WORK.CPU.t_REGISTER;
        stage_mem_enable_destination : in  std_logic;
        stage_mem_select_destination : in  WORK.CPU.t_REGISTER;
        stage_wb_enable_destination  : in  std_logic;
        stage_wb_select_destination  : in  WORK.CPU.t_REGISTER;
        select_source_1              : out std_logic_vector(1 downto 0);
        select_source_2              : out std_logic_vector(1 downto 0)
    );

end entity;

architecture RV32I of CPU_EXECUTION_FORWARDING_UNIT is

    constant ZERO : WORK.RV32I.t_REGISTER := (others => '0');

    signal mem_source_1 : std_logic;
    signal mem_source_2 : std_logic;
    signal mem_not_zero : std_logic;
    signal wb_source_1  : std_logic;
    signal wb_source_2  : std_logic;
    signal wb_not_zero  : std_logic;

begin

    mem_source_1 <= is_equal_dynamic(stage_ex_select_source_1, stage_mem_select_destination);
    mem_source_2 <= is_equal_dynamic(stage_ex_select_source_2, stage_mem_select_destination);
    wb_source_1  <= is_equal_dynamic(stage_ex_select_source_1, stage_wb_select_destination);
    wb_source_2  <= is_equal_dynamic(stage_ex_select_source_2, stage_wb_select_destination);
    mem_not_zero <= reduce_or(stage_mem_select_destination);
    wb_not_zero  <= reduce_or(stage_wb_select_destination);

    select_source_1(1) <= (stage_mem_enable_destination AND mem_source_1 AND mem_not_zero);
    select_source_1(0) <= (stage_wb_enable_destination  AND wb_source_1  AND wb_not_zero) AND NOT select_source_1(1);
    select_source_2(1) <= (stage_mem_enable_destination AND mem_source_2 AND mem_not_zero);
    select_source_2(0) <= (stage_wb_enable_destination  AND wb_source_2  AND wb_not_zero) AND NOT select_source_2(1);

end architecture;
