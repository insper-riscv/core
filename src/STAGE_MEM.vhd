library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_MEM is
  
    port (
        clock       : in  std_logic;
        source      : in t_EX_MEM_SIGNALS;
        destination : out t_MEM_WB_SIGNALS
    );

end entity;

architecture RTL of STAGE_MEM is

    -- No signals

begin

    MODULE_MEMORY : entity WORK.MODULE_MEMORY
        port map (
            clock             => clock,
            enable            => '1',      
            enable_read       => source.mem_signals.enable_read,
            enable_write      => source.mem_signals.enable_write,
            source_ex         => source.pointer,    
            register_source_2 => source.source_2,      
            destination       => destination.destination
        );
    
    destination.address <= source.pointer;
    destination.select_destination <= source.select_destination;
    destination.wb_signals <= source.wb_signals;

end architecture;
