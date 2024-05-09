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

    destination <=  (
                        (source_1 AND (NOT(selector(0)) AND NOT(selector(1)))) OR
                        (source_2 AND (selector(0) AND NOT(selector(1))))
                    ) OR (
                        (source_3 AND (NOT(selector(0)) AND selector(1))) OR
                        (source_4 AND (selector(0) AND selector(1)))
                    );

end architecture;
