library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_MUX_2X1 is

    generic (
        DATA_WIDTH_0 : natural := DATA_WIDTH
    );

    port (
        source_1    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        source_2    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        selector    : in  std_logic;
        destination : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_2X1 is

    -- No signals

begin

    destination <= source_2 when (selector = '1') else
                   source_1;

end architecture;
