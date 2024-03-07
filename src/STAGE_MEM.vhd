library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_MEM is
  
    port (
        clock             : in  std_logic;
        enable            : in  std_logic;
        enable_read       : in  std_logic;
        enable_write      : in  std_logic;
        source_ex         : in  std_logic_vector((XLEN_RANGE);
        register_source_2 : in  std_logic_vector((XLEN_RANGE);
        destination       : out std_logic_vector((XLEN_RANGE)
    );

end entity;

architecture RTL of STAGE_MEM is

    -- No signals

begin

    MODULE_MEMORY : entity WORK.MODULE_MEMORY
        port map (
            clock             => clock,
            enable            => enable,      
            enable_read       => enable_read,
            enable_write      => enable_write,
            source_ex         => source_ex,    
            register_source_2 => register_source_2,      
            destination       => destination 
        );

end architecture;
