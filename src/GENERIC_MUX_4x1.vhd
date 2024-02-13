library ieee;
use ieee.std_logic_1164.all;

entity GENERIC_MUX_4x1 is
    generic (
        dataLength : natural := 32
    );
    port (
        a:  in std_logic_vector((dataLength-1) downto 0);
        b:  in std_logic_vector((dataLength-1) downto 0);
        c:  in std_logic_vector((dataLength-1) downto 0);
        d:  in std_logic_vector((dataLength-1) downto 0);
        s:  in std_logic_vector(1 downto 0);
        q:  out std_logic_vector((dataLength-1) downto 0)
    );
end GENERIC_MUX_4x1;

architecture RTL of GENERIC_MUX_4x1 is

begin

    q <= a when (s = "00") else
         b when (s = "01") else
         c when (s = "10") else
         d;

end architecture;