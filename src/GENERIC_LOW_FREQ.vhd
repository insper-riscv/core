LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

entity GENERIC_LOW_FREQ is
generic (n : natural := 8);
    port(
      clock      :   in std_logic;
      clock_out :   out std_logic);
end entity;

-- O valor "n" do n, define a divisao por "2n".
-- Ou seja, n é metade do período da frequência de saída.

architecture RTL of GENERIC_LOW_FREQ is
    signal tick : std_logic := '0';
    signal counter : integer range 0 to n+1 := 0;
begin
    process(clock)
    begin
        if rising_edge(clock) then
            if counter = n then
                counter <= 0;
                tick <= not tick;
            else
                counter <= counter + 1;
            end if;
        end if;
    end process;
clock_out <= tick;
end architecture RTL;