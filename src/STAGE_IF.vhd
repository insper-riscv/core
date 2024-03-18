library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_IF is

    port (
        control         : in  t_CONTROL_CLK_CLR_EN;
        source          : in  t_CONTROL_IF;
        address_jump    : in  t_DATA;
        address_program : out t_DATA
    );

end entity;

architecture RTL of STAGE_IF is

    signal enable : std_logic;

begin

    process(source.enable_stall) is
    begin
        enable <= control.enable AND NOT source.enable_stall;
    end process;

    MODULE_PC : entity WORK.MODULE_PC
        port map (
            clock        => control.clock,
            jump_address => address_jump,
            selector     => source.select_source,
            enable       => enable,
            destination  => address_program
        );

end architecture;
