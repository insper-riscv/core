library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_EXECUTION_FORWARDING_UNIT is

    port (
        stage_ex_select_source_1     : in  WORK.CPU.t_REGISTER;
        stage_ex_select_source_2     : in  WORK.CPU.t_REGISTER;
        stage_mem_enable_destination : in  std_logic;
        stage_mem_select_destination : in  WORK.CPU.t_REGISTER;
        stage_wb_enable_destination  : in  std_logic;
        stage_wb_select_destination  : in  WORK.CPU.t_REGISTER;
        stage_id_select_source_1     : out std_logic_vector(1 downto 0);
        stage_id_select_source_2     : out std_logic_vector(1 downto 0)
    );

end entity;

architecture RTL of CPU_EXECUTION_FORWARDING_UNIT is

    -- No signals

begin

    stage_id_select_source_1 <= "10" when (
                                    stage_mem_enable_destination = '1' and
                                    stage_ex_select_source_1 = stage_mem_select_destination and
                                    stage_mem_select_destination /= "00000"
                                ) else
                                "01" when (
                                    stage_wb_enable_destination = '1' and
                                    stage_ex_select_source_1 = stage_wb_select_destination and
                                    stage_wb_select_destination /= "00000"
                                ) else
                                "00";

    stage_id_select_source_2 <= "10" when (
                                    stage_mem_enable_destination = '1' and
                                    stage_ex_select_source_2 = stage_mem_select_destination and
                                    stage_mem_select_destination /= "00000"
                                ) else
                                "01" when (
                                    stage_wb_enable_destination = '1' and
                                    stage_ex_select_source_2 = stage_wb_select_destination and
                                    stage_wb_select_destination /= "00000"
                                ) else
                                "00";

end architecture;
