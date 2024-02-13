library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ALU is
    generic (
        dataLenght : natural := 4;
		selectorLenght : natural := 2 
    );
    port (
        a:  in std_logic_vector((dataLenght-1) downto 0);
        b:  in std_logic_vector((dataLenght-1) downto 0);
        s:  in std_logic_vector((selectorLenght-1) downto 0);
        q:  out std_logic_vector((dataLenght-1) downto 0)--;
	    -- flag: out std_logic
    );
end ALU;

architecture RTL of ALU is
    signal sum : std_logic_vector((dataLenght-1) downto 0);
    signal sub : std_logic_vector((dataLenght-1) downto 0);
	signal pass : std_logic_vector((dataLenght-1) downto 0);
    begin
        sum <= std_logic_vector(unsigned(a) + unsigned(b));
        sub <= std_logic_vector(unsigned(a) - unsigned(b));
		pass <= std_logic_vector(unsigned(b));
        q <= sum when (s = "01") else 
		    sub when (s = "00") else
			pass;
					
		-- flag <= '1' when unsigned(q) = 0 else '0';
end architecture;