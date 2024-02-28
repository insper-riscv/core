library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_REGISTER is

    generic (
        DATA_WIDTH_0 : natural := DATA_WIDTH
    );

    port (
        clock       : in  std_logic;
        clear       : in  std_logic;
        enable      : in  std_logic;
        source      : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0) := (others => '0')
    );

end entity;

architecture RTL of GENERIC_REGISTER is

    -- No signals

begin

    UPDATE : process(clear, clock, enable)
    begin
        if (rising_edge(clock)) then
            SET_RESET : if (enable = '1') then
                destination <= source;
            elsif (clear = '1') then
                destination <= (others => '0');
            end if;
        end if;
    end process;

end architecture;
