library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_BRANCH_FORWARDING_UNIT is

    port (
        stage_id_select_source_1     : in  WORK.CPU.t_REGISTER;
        stage_id_select_source_2     : in  WORK.CPU.t_REGISTER;
        stage_mem_enable_destination : in  std_logic;
        stage_mem_select_destination : in  WORK.CPU.t_REGISTER;
        stage_id_select_1            : out std_logic;
        stage_id_select_2            : out std_logic
    );

end entity;

architecture RTL of CPU_BRANCH_FORWARDING_UNIT is

    -- No signals

begin

    stage_id_select_1 <= '1' when (
                            stage_mem_enable_destination = '1' and
                            stage_id_select_source_1 = stage_mem_select_destination and
                            stage_mem_select_destination /= "00000"
                        ) else
                        '0';

    stage_id_select_2 <= '1' when (
                            stage_mem_enable_destination = '1' and
                            stage_id_select_source_2 = stage_mem_select_destination and
                            stage_mem_select_destination /= "00000"
                        ) else
                        '0';

end architecture;
