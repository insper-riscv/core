library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ROM is

    generic (
        DATA_WIDTH : natural := XLEN
    );

    port (
        pc           : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ROM is

begin

    ROM : entity WORK.GENERIC_ROM
        port map (
            address     => pc,
            destination => destination
        );

end architecture;
