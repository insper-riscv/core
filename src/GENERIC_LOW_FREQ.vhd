LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

LIBRARY WORK;

entity GENERIC_LOW_FREQ is

    generic (
        n : natural := 8    -- O valor "n" do n, define a divisão por "2n". 
                            -- Ou seja, não metade do perí­odo da frequência de saÃída.
        
    );

    port(
        clock     : in  std_ulogic;
        clock_out : out std_ulogic
    );

end entity;

architecture RTL of GENERIC_LOW_FREQ is

    signal counter : integer range 0 to (n + 1) := 0;
    signal tick    : std_ulogic := '0';

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