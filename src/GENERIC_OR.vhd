library ieee;
use ieee.std_logic_1164.all;

entity GENERIC_OR is
    port (
        a : in std_logic;
        b : in std_logic;
        q : out std_logic
    );
end;

architecture RTL of GENERIC_OR is

    -- No Signals

begin

    process(a, b)
    begin
        q <= a OR b;
    end process;

end architecture;
