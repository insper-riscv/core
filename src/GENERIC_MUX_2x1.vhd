library ieee;
use ieee.std_logic_1164.all;

entity GENERIC_MUX_2x1 is
    generic (
        dataLength : natural := 32
    );
    port (
        a:  in std_logic_vector((dataLength-1) downto 0);
        b:  in std_logic_vector((dataLength-1) downto 0);
        s:  in std_logic;
        q:  out std_logic_vector((dataLength-1) downto 0)
    );
end GENERIC_MUX_2x1;

architecture RTL of GENERIC_MUX_2x1 is

begin

    q <= a when (s = '0') else b;

end architecture;