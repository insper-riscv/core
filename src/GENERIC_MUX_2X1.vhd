library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_MUX_2X1 is

    generic (
        DATA_WIDTH : natural := 8
    );

    port (
        selector    : in  std_logic                                   := '0';
        source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_2    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_2X1 is

    signal selector_vec : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    selector_vec <= (others => selector);

    destination <= (source_1 AND NOT(selector_vec)) OR (source_2 AND selector_vec);

end architecture;

architecture SYN of GENERIC_MUX_2X1 is

    with selector select
    destination <=  source_1 when '0',
                    source_2 when '1',
                    source_1 when others;

end architecture
