library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_SIGNAL_EXTENDER is

    generic (
        SOURCE_WIDTH      : natural := 4;
        DESTINATION_WIDTH : natural := 8
    );

    port (
        source          : in  std_logic_vector((SOURCE_WIDTH - 1) downto 0);
        enable_unsigned : in  std_logic := '0';
        destination     : out std_logic_vector((DESTINATION_WIDTH - 1) downto 0)
    );

end entity;

architecture LOGICAL_UPPER of GENERIC_SIGNAL_EXTENDER is

    -- No signals

begin

    destination((DESTINATION_WIDTH - 1) downto (DESTINATION_WIDTH - SOURCE_WIDTH)) <= source;
    destination((DESTINATION_WIDTH - SOURCE_WIDTH - 1) downto 0) <= (others => '0');

end architecture;

architecture LOWER_EXTEND of GENERIC_SIGNAL_EXTENDER is

    signal upper : std_logic_vector((DESTINATION_WIDTH - 1) downto SOURCE_WIDTH);

begin

    upper <= (others => '0') when (enable_unsigned = '1') else
             (others => source(SOURCE_WIDTH - 1));

    destination((DESTINATION_WIDTH - 1) downto SOURCE_WIDTH) <= upper;
    destination((SOURCE_WIDTH - 1) downto 0) <= source;

end architecture;
