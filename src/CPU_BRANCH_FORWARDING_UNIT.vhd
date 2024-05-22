library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity CPU_BRANCH_FORWARDING_UNIT is

    port (
        stage_id_select_source_1     : in  WORK.CPU.t_REGISTER;
        stage_id_select_source_2     : in  WORK.CPU.t_REGISTER;
        stage_mem_enable_destination : in  std_ulogic;
        stage_mem_select_destination : in  WORK.CPU.t_REGISTER;
        select_source_1              : out std_ulogic;
        select_source_2              : out std_ulogic
    );

end entity;

architecture RV32I of CPU_BRANCH_FORWARDING_UNIT is

    constant ZERO : WORK.RV32I.t_REGISTER := (others => '0');

    signal mem_source_1 : std_ulogic;
    signal mem_source_2 : std_ulogic;
    signal mem_zero     : std_ulogic;

begin

    mem_source_1 <= is_equal_dynamic(stage_id_select_source_1, stage_mem_select_destination);
    mem_source_2 <= is_equal_dynamic(stage_id_select_source_2, stage_mem_select_destination);
    mem_zero     <= is_equal_dynamic(stage_mem_select_destination, ZERO);

    select_source_1 <= (stage_mem_enable_destination AND mem_source_1 AND NOT(mem_zero));
    select_source_2 <= (stage_mem_enable_destination AND mem_source_2 AND NOT(mem_zero));

end architecture;
