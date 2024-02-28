library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_ADDER is

    generic (
        DATA_WIDTH_0     : natural := DATA_WIDTH;
        DEFAULT_SOURCE_1 : integer := 1
    );

    port (
        source_1    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        source_2    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0) := std_logic_vector(to_signed(DEFAULT_SOURCE_1, DATA_WIDTH_0));
        destination : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_ADDER is

    -- No signals

begin

    destination <= std_logic_vector(unsigned(source_1) + unsigned(source_2));

end architecture;
