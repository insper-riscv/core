library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity GENERIC_ADDER is

    generic (
        DATA_WIDTH     : natural := 8;
        DEFAULT_TARGET : integer := 1
    );

    port (
        source    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        target    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := std_logic_vector(to_signed(DEFAULT_TARGET, DATA_WIDTH));
        destiny   : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_ADDER is

    -- No signals

begin

    destiny <= std_logic_vector(unsigned(source) + unsigned(target));

end architecture;
