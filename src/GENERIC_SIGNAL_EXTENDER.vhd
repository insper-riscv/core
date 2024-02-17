library ieee;
use ieee.std_logic_1164.all;

entity GENERIC_SIGNAL_EXTENDER is

    generic (
        SOURCE_WIDTH  : natural;
        DESTINY_WIDTH : natural
    );

    port (
        source          : in  std_logic_vector((SOURCE_WIDTH - 1) downto 0);
        enable_unsigned : in  std_logic := '0';
        destiny         : out std_logic_vector((DESTINY_WIDTH - 1) downto 0)
    );

end entity;

architecture LOWER_EXTEND of GENERIC_SIGNAL_EXTENDER is

    signal upper : std_logic_vector((DESTINY_WIDTH - 1) downto SOURCE_WIDTH);

begin

    upper <= (others => '0') when (enable_unsigned = '1') else
             (others => source(SOURCE_WIDTH - 1));

    destiny((DESTINY_WIDTH - 1) downto SOURCE_WIDTH) <= upper;
    destiny((SOURCE_WIDTH - 1) downto 0) <= source;

end architecture;

architecture LOGICAL_UPPER of GENERIC_SIGNAL_EXTENDER is

    -- No signals

begin

    destiny((DESTINY_WIDTH - 1) downto (DESTINY_WIDTH - SOURCE_WIDTH)) <= source;
    destiny((DESTINY_WIDTH - SOURCE_WIDTH - 1) downto 0) <= (others => '0');

end architecture;
