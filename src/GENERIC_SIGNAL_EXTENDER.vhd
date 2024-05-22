library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_SIGNAL_EXTENDER is

    generic (
        SOURCE_WIDTH      : natural := 4;
        DESTINATION_WIDTH : natural := 8
    );

    port (
        source          : in  std_ulogic_vector((SOURCE_WIDTH - 1) downto 0);
        enable_unsigned : in  std_ulogic := '0';
        destination     : out std_ulogic_vector((DESTINATION_WIDTH - 1) downto 0)
    );

end entity;

architecture LOGICAL_UPPER of GENERIC_SIGNAL_EXTENDER is

    -- No signals

begin

    destination((DESTINATION_WIDTH - 1) downto (DESTINATION_WIDTH - SOURCE_WIDTH)) <= source;
    destination((DESTINATION_WIDTH - SOURCE_WIDTH - 1) downto 0) <= (others => '0');

end architecture;

architecture LOWER_EXTEND of GENERIC_SIGNAL_EXTENDER is

    signal upper : std_ulogic_vector((DESTINATION_WIDTH - 1) downto SOURCE_WIDTH);

begin

    MUX_UPPER : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => upper'length
        )
        port map (
            selector    => enable_unsigned,
            source_1    => (others => source(SOURCE_WIDTH - 1)),
            source_2    => (others => '0'),
            destination => upper
        );

    destination((DESTINATION_WIDTH - 1) downto SOURCE_WIDTH) <= upper;
    destination((SOURCE_WIDTH - 1) downto 0) <= source;

end architecture;
