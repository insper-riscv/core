library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_WRITE_BACK is

    generic (
        DATA_WIDTH  : natural := XLEN
    );

    port (
        source_memory : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_ex     : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        selector      : in  std_logic;
        destination   : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_WRITE_BACK is

    -- No signals

begin

    MUX : entity WORK.GENERIC_MUX_2X1
        port map (
            source_1 => source_memory,
            source_2 => source_ex,
            selector => selector,
            destination => destination
        );

end architecture;
