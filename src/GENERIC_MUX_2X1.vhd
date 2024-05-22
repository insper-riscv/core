library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_MUX_2X1 is

    generic (
        DATA_WIDTH : natural := 8
    );

    port (
        selector    : in  std_ulogic;
        source_1    : in  std_ulogic_vector((DATA_WIDTH - 1) downto 0);
        source_2    : in  std_ulogic_vector((DATA_WIDTH - 1) downto 0);
        destination : out std_ulogic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_2X1 is

    signal selector_vec : std_ulogic_vector((DATA_WIDTH - 1) downto 0);

begin

    selector_vec <= (others => selector);

    destination <= (source_1 AND NOT(selector_vec)) OR (source_2 AND selector_vec);

end architecture;
