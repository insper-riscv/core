library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity TOP_LEVEL is

    port (
        CLOCK : in  std_logic;
        SW    : in std_logic_vector(3 downto 0);
        LED   : out std_logic_vector(7 downto 0)
    );

end entity;

architecture RTL of TOP_LEVEL is

    -- No signals

begin

    LED(0) <= SW(1);

end architecture;
