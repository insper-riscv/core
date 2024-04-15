library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.CPU.ALL;

entity CPU_STAGE_IF is

    port (
        clock           : in  std_logic;
        enable          : in  std_logic;
        source          : in  t_CONTROL_IF;
        address_jump    : in  t_DATA;
        address_program : out t_DATA
    );

end entity;

architecture RTL of CPU_STAGE_IF is

    signal enable_0 : std_logic;
    signal jump     : std_logic;

begin

    jump <= source.select_source XOR source.enable_jump;

    process(source.enable_stall) is
    begin
        enable_0 <= enable AND NOT source.enable_stall;
    end process;

    MODULE_PROGRAM_COUNTER : entity WORK.MODULE_PROGRAM_COUNTER
        port map (
            clock        => clock,
            jump_address => address_jump,
            selector     => jump,
            enable       => enable_0,
            destination  => address_program
        );

end architecture;
