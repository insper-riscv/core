library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_IF is

    generic (
        DATA_WIDTH : natural := XLEN
    );

    port (
        clock       : in  std_logic;
        source      : in t_IF_SIGNALS;
        destination : out t_IF_ID_SIGNALS
    );

end entity;

architecture RTL of STAGE_IF is

        signal pc : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    MODULE_PC : entity WORK.MODULE_PC
        port map (
            clock        => clock,
            jump_address => source.source,
            selector     => source.select_source_pc,
            enable       => source.enable_stall,
            pc           => destination.pc,
            destination  => pc
        );

    MODULE_ROM : entity WORK.MODULE_ROM
        port map (
            pc           => pc,
            destination  => destination.instruction
        );

end architecture;