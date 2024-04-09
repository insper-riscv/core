library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_SHIFTER is

    generic (
        DATA_WIDTH           : natural := XLEN;
        SELECTOR_WIDTH       : natural := 5
    );

    port (
        source      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        selector_1  : in  std_logic_vector((SELECTOR_WIDTH - 1) downto 0);
        selector_2  : in  std_logic_vector(2 downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_SHIFTER is

    signal shift_32         : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
    signal select_default_0 : std_logic_vector((SELECTOR_WIDTH - 1) downto 0) := (others => '0');
    signal select_default_1 : std_logic_vector((SELECTOR_WIDTH - 1) downto 0) := (others => '1');
    signal shift_r          : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
    signal shift_l          : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
    signal shift_r_a          : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
    signal tmp_r_a          : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');

begin

    SHIFT_ARITHMETIC : process(source)
        begin
            tmp_r_a <= (others => source(DATA_WIDTH - 1));
        end process;

    shift_l <= source when (selector_1 = select_default_0((SELECTOR_WIDTH - 1) downto 0)) else
               source(0) & shift_32((to_integer(unsigned(selector_1)) - 1) downto 0) when (selector_1 = select_default_1((SELECTOR_WIDTH - 1) downto 0)) else
               source((DATA_WIDTH - 1) - to_integer(unsigned(selector_1)) downto 0) & shift_32(to_integer(unsigned(selector_1)) - 1) when (selector_1 = select_default_0((SELECTOR_WIDTH - 1) downto 1) & '1') else
               source((DATA_WIDTH - 1) - (to_integer(unsigned(selector_1))) downto 0) & shift_32((to_integer(unsigned(selector_1)) - 1) downto 0);

    shift_r <= source when (selector_1 = select_default_0((SELECTOR_WIDTH - 1) downto 0)) else
               shift_32((to_integer(unsigned(selector_1)) - 1) downto 0) & source(DATA_WIDTH - 1) when (selector_1 = select_default_1((SELECTOR_WIDTH - 1) downto 0)) else
               shift_32(to_integer(unsigned(selector_1))) & source((DATA_WIDTH - 1) downto to_integer(unsigned(selector_1))) when (selector_1 = select_default_0((SELECTOR_WIDTH - 1) downto 1) & '1') else
               shift_32((to_integer(unsigned(selector_1)) - 1) downto 0) & source((DATA_WIDTH - 1) downto (to_integer(unsigned(selector_1))));
    
    shift_r_a <= source when (selector_1 = select_default_0((SELECTOR_WIDTH - 1) downto 0)) else
                 tmp_r_a((to_integer(unsigned(selector_1)) - 1) downto 0) & source(DATA_WIDTH - 1) when (selector_1 = select_default_1((SELECTOR_WIDTH - 1) downto 0)) else
                 tmp_r_a(to_integer(unsigned(selector_1))) & source((DATA_WIDTH - 1) downto to_integer(unsigned(selector_1))) when (selector_1 = select_default_0((SELECTOR_WIDTH - 1) downto 1) & '1') else
                 tmp_r_a((to_integer(unsigned(selector_1)) - 1) downto 0) & source((DATA_WIDTH - 1) downto (to_integer(unsigned(selector_1))));

    destination <= shift_l when (selector_2 = "100") else
                   shift_r when (selector_2 = "101") else
                   shift_r_a when (selector_2 = "110") else
                   source;

end architecture;