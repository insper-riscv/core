library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity CPU_HAZZARD_CONTROL_UNIT is

    port (
        stage_id_select_source_1     : in  WORK.CPU.t_REGISTER;
        stage_id_select_source_2     : in  WORK.CPU.t_REGISTER;
        stage_ex_enable_read         : in  std_logic;
        stage_ex_enable_destination  : in  std_logic;
        stage_ex_select_destination  : in  WORK.CPU.t_REGISTER;
        stage_mem_enable_read        : in  std_logic;
        stage_mem_select_destination : in  WORK.CPU.t_REGISTER;
        stall_branch                 : out std_logic;
        destination                  : out std_logic
    );

end entity;

architecture RTL of CPU_HAZZARD_CONTROL_UNIT is

    -- No signals

begin

    stall_branch <= (
                        (
                            is_equal_dynamic(stage_id_select_source_1, stage_ex_select_destination) OR
                            is_equal_dynamic(stage_id_select_source_2, stage_ex_select_destination)
                        ) AND
                        NOT(is_equal_dynamic(stage_ex_select_destination, 5X"0")) AND
                        stage_ex_enable_destination
                    ) OR  (
                        (
                            is_equal_dynamic(stage_id_select_source_1, stage_mem_select_destination) OR
                            is_equal_dynamic(stage_id_select_source_2, stage_mem_select_destination)
                        ) AND
                        NOT(is_equal_dynamic(stage_mem_select_destination, 5X"0")) AND
                        stage_mem_enable_read
                    );

    destination <=  (
                        is_equal_dynamic(stage_id_select_source_1, stage_ex_select_destination) OR
                        is_equal_dynamic(stage_id_select_source_2, stage_ex_select_destination)
                    ) AND
                    NOT(is_equal_dynamic(stage_ex_select_destination, 5X"0")) AND
                    stage_ex_enable_read;

end architecture;
