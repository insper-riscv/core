library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_MUX_4X1 is

    generic (
        DATA_WIDTH : natural := 8
    );

    port (
        source_1     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_2     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_3     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_4     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        selector     : in  std_logic_vector(1 downto 0);
        destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_4X1 is

    -- No signals

begin

    destination <= source_2 when (selector = "01") else
                   source_3 when (selector = "10") else
                   source_4 when (selector = "11") else
                   source_1;

end architecture;
