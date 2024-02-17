library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity GENERIC_MUX_2X1 is

    generic (
        DATA_WIDTH : natural := 8
    );

    port (
        source_0 : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_1 : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        selector : in  std_logic;
        destiny  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_2X1 is

    -- No signals

begin

    destiny <= source_1 when (selector = '1') else
               source_0;

end architecture;
