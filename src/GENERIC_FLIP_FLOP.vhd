library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_FLIP_FLOP is

    port (
        clock  : in  std_logic;
        clear  : in  std_logic := '1';
        enable : in  std_logic := 'X';
        source : in  std_logic := 'X';
        state  : out std_logic := '0'
    );

end entity;

architecture RTL of GENERIC_FLIP_FLOP is

    -- No signals

begin

    UPDATE : process(clock)
    begin
        if (rising_edge(clock)) then
            if (enable = '1') then
                if (clear = '1') then
                    state <= '0';
                else
                    state <= source;
                end if;
            end if;
        end if;
    end process;

end architecture;
