library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_FLIP_FLOP is

    port (
        clock  : in  std_logic;
        clear  : in  std_logic;
        enable : in  std_logic;
        source : in  std_logic;
        state  : out std_logic := '0'
    );

end entity;

architecture RTL of GENERIC_FLIP_FLOP is

    -- No signals

begin

    UPDATE : process(clock)
    begin
        if (rising_edge(clock)) then
            SET_RESET : if (enable = '1') then
                state <= source;
            elsif (clear = '1') then
                state <= '0';
            end if;
        end if;
    end process;

end architecture;
