library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.TOP_LEVEL_CONSTANTS.ALL;

entity TOP_LEVEL is

    port (
        CLOCK : in  std_logic;
        SW    : in std_logic_vector(3 downto 0);
        LED   : out std_logic_vector(7 downto 0)
    );

end entity;

architecture RTL of TOP_LEVEL is

    signal signal1 : std_logic;
    signal signal2 : std_logic;
    signal signal3 : std_logic_vector(DATA_WIDTH downto 0);
    signal signal4 : std_logic_vector(DATA_WIDTH downto 0);

begin

    LED(0) <= SW(1);

end architecture;
