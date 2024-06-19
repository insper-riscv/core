library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_MUX_4X1 is

    generic (
        DATA_WIDTH : natural := 8
    );

    port (
        selector     : in  std_logic_vector(1 downto 0)                := (others => '0');
        source_1     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_2     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_3     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_4     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_4X1 is

    signal selector_0 : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal selector_1 : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    selector_0 <= (others => selector(0));
    selector_1 <= (others => selector(1));

    destination <=  (
                        (source_1 AND (NOT(selector_0) AND NOT(selector_1))) OR
                        (source_2 AND (selector_0 AND NOT(selector_1)))
                    ) OR (
                        (source_3 AND (NOT(selector_0) AND selector_1)) OR
                        (source_4 AND (selector_0 AND selector_1))
                    );

end architecture;

architecture SYN of GENERIC_MUX_4X1 is

    with selector select
    destination <=  source_1 when "00",
                    source_2 when "01",
                    source_3 when "10",
                    source_4 when "11",
                    source_1 when others;

end architecture
