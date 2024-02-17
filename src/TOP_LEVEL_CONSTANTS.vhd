library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

package TOP_LEVEL_CONSTANTS is

    constant CLOCK_FREQUENCY : integer := 50_000_000; -- 50 MHz clock frequency
    constant DATA_WIDTH : integer := 32;

    subtype DATA_RANGE is natural range (DATA_WIDTH - 1) downto 0;
  
end package;
