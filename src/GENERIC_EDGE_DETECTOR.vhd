library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_EDGE_DETECTOR is

    Port (
        clock  : in  std_ulogic;
        source : in  std_ulogic;
        pulse  : out std_ulogic
    );

end entity;

architecture RISING_DETECTOR of GENERIC_EDGE_DETECTOR is

    signal state_1 : std_ulogic := '0';
    signal state_2 : std_ulogic := '0';

begin

    EDGE : process(clock)
    begin
        if rising_edge(clock) then
            state_1 <= source;
            state_2 <= state_1;
        end if;
    end process;

    pulse <= state_1 AND NOT(state_2);

end architecture;

architecture FALLING_DETECTOR of GENERIC_EDGE_DETECTOR is

    signal state_1 : std_ulogic := '0';
    signal state_2 : std_ulogic := '0';

begin

    EDGE : process(clock)
    begin
        if rising_edge(clock) then
            state_1 <= source;
            state_2 <= state_1;
        end if;
    end process;

    pulse <= NOT(state_1) AND state_2;

end architecture;
