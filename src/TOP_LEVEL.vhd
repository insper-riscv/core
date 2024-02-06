library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.TOP_LEVEL_CONSTANTS.ALL;

entity TOP_LEVEL is

  port (
    CLOCK : in  std_logic;
  );

end entity;

architecture RTL of TOP_LEVEL is

  signal signal1 : std_logic;
  signal signal2 : std_logic;
  signal signal3 : std_logic_vector(31 downto 0);
  signal signal4 : std_logic_vector(31 downto 0);

 begin

  NAME : entity WORK.ENTITY_NAME
    generic map (
	   property1 => signal1,
	   property2 => signal2
	 )
    port map (
	   property3 => signal3,
	   property4 => signal4
    );

end architecture;
