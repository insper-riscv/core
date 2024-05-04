library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_HAZZARD_CONTROL_UNIT is

    port (
        stage_id_select_source_1     : in  WORK.CPU.t_REGISTER;
        stage_id_select_source_2     : in  WORK.CPU.t_REGISTER;
        stage_ex_enable_read         : in  std_logic;
        stage_ex_select_destination  : in  WORK.CPU.t_REGISTER;
        destination                  : out std_logic
    );

end entity;

architecture RTL of CPU_HAZZARD_CONTROL_UNIT is

    -- No signals

begin

    destination <= '1' when (
                        (stage_id_select_source_1 = stage_ex_select_destination or
                        stage_id_select_source_2 = stage_ex_select_destination) and
                        stage_ex_enable_read = '1' and
                        stage_ex_select_destination /= "00000"
                        ) else
                        '0';

end architecture;
