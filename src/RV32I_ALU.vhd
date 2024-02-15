library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity RV32I_ALU is
    generic (
        dataLength : natural := 4;
		selectorLenght : natural := 2 
    );
    port (
        a:  in std_logic_vector((dataLength-1) downto 0);
        b:  in std_logic_vector((dataLength-1) downto 0);
        s:  in std_logic_vector((selectorLenght-1) downto 0);
        q:  out std_logic_vector((dataLength-1) downto 0)
    );
end RV32I_ALU;

architecture RTL of RV32I_ALU is

    signal sub : std_logic_vector((dataLength-1) downto 0);
    signal sum : std_logic_vector((dataLength-1) downto 0);
	signal pass : std_logic_vector((dataLength-1) downto 0);

begin

        sub <= std_logic_vector(unsigned(a) - unsigned(b));
        sum <= std_logic_vector(unsigned(a) + unsigned(b));
		pass <= std_logic_vector(unsigned(b));
        q <= sub when (s = "00") else
             sum when (s = "01") else 
			 pass;

end architecture;