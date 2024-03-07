library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_IF is

    port (
        clock       : in  std_logic;
        source_id   : in  std_logic_vector(XLEN_RANGE);
        selector    : in  std_logic;
        clear       : in  std_logic;
        enable      : in  std_logic;
        destination : out std_logic_vector(XLEN_RANGE)
    );

end entity;

architecture RTL of STAGE_IF is

    -- No signals

begin

    MODULE_PC : entity WORK.MODULE_PC
        port map (
            clock       => clock,      
            source_id   => source_id,  
            selector    => selector,   
            clear       => clear,      
            enable      => enable,     
            destination => destination
        );

end architecture;
