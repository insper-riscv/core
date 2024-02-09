library ieee;
use ieee.std_logic_1164.all;

entity and_gate is
    port (
        a, b : in std_logic;
        result : out std_logic
    );
end and_gate;

architecture behavioral of and_gate is
begin
    process(a, b)
    begin
        result <= a and b;
    end process;
end architecture;