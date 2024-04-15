library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity GENERIC_SHIFTER is

    generic (
        DATA_WIDTH  : natural := 8;
        SHAMT_WIDTH : natural := 3
    );

    port (
        source          : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        shamt           : in  std_logic_vector((SHAMT_WIDTH - 1) downto 0);
        select_function : in  std_logic_vector(2 downto 0);
        destination     : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_SHIFTER is

    signal shift_32         : std_logic_vector((DATA_WIDTH - 1)  downto 0) := (others => '0');
    signal select_default_0 : std_logic_vector((SHAMT_WIDTH - 1) downto 0) := (others => '0');
    signal select_default_1 : std_logic_vector((SHAMT_WIDTH - 1) downto 0) := (others => '1');
    signal shift_r          : std_logic_vector((DATA_WIDTH - 1)  downto 0) := (others => '0');
    signal shift_l          : std_logic_vector((DATA_WIDTH - 1)  downto 0) := (others => '0');
    signal shift_r_a        : std_logic_vector((DATA_WIDTH - 1)  downto 0) := (others => '0');
    signal tmp_r_a          : std_logic_vector((DATA_WIDTH - 1)  downto 0) := (others => '0');

begin

    SHIFT_ARITHMETIC : process(source)
    begin
        tmp_r_a <= (others => source(DATA_WIDTH - 1));
    end process;

    shift_l <= source when (shamt = select_default_0((SHAMT_WIDTH - 1) downto 0)) else
               source(0) & shift_32((to_integer(unsigned(shamt)) - 1) downto 0) when (shamt = select_default_1((SHAMT_WIDTH - 1) downto 0)) else
               source((DATA_WIDTH - 1) - to_integer(unsigned(shamt)) downto 0) & shift_32(to_integer(unsigned(shamt)) - 1) when (shamt = select_default_0((SHAMT_WIDTH - 1) downto 1) & '1') else
               source((DATA_WIDTH - 1) - (to_integer(unsigned(shamt))) downto 0) & shift_32((to_integer(unsigned(shamt)) - 1) downto 0);

    shift_r <= source when (shamt = select_default_0((SHAMT_WIDTH - 1) downto 0)) else
               shift_32((to_integer(unsigned(shamt)) - 1) downto 0) & source(DATA_WIDTH - 1) when (shamt = select_default_1((SHAMT_WIDTH - 1) downto 0)) else
               shift_32(to_integer(unsigned(shamt))) & source((DATA_WIDTH - 1) downto to_integer(unsigned(shamt))) when (shamt = select_default_0((SHAMT_WIDTH - 1) downto 1) & '1') else
               shift_32((to_integer(unsigned(shamt)) - 1) downto 0) & source((DATA_WIDTH - 1) downto (to_integer(unsigned(shamt))));
    
    shift_r_a <= source when (shamt = select_default_0((SHAMT_WIDTH - 1) downto 0)) else
                 tmp_r_a((to_integer(unsigned(shamt)) - 1) downto 0) & source(DATA_WIDTH - 1) when (shamt = select_default_1((SHAMT_WIDTH - 1) downto 0)) else
                 tmp_r_a(to_integer(unsigned(shamt))) & source((DATA_WIDTH - 1) downto to_integer(unsigned(shamt))) when (shamt = select_default_0((SHAMT_WIDTH - 1) downto 1) & '1') else
                 tmp_r_a((to_integer(unsigned(shamt)) - 1) downto 0) & source((DATA_WIDTH - 1) downto (to_integer(unsigned(shamt))));

    destination <= shift_l when (select_function = "100") else
                   shift_r when (select_function = "101") else
                   shift_r_a when (select_function = "110") else
                   source;

end architecture;
