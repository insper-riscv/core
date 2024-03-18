library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_MEM is
  
    port (
        clock          : in  std_logic;
        source         : in  t_SIGNALS_EX_MEM;
        control_memory : out t_CONTROL_MEM;
        address_memory : out t_DATA;
        data_memory    : out t_DATA;
        destination    : out t_SIGNALS_MEM_WB
    );

end entity;

architecture RTL of STAGE_MEM is

    -- No signals

begin

    destination.control_wb         <= source.control_wb;

    control_memory.enable_read     <= source.control_mem.enable_read;
    control_memory.enable_write    <= source.control_mem.enable_write;

    address_memory                 <= source.address_pointer;
    data_memory                    <= source.data_source_2;

    destination.data_destination   <= source.address_pointer;
    destination.select_destination <= source.select_destination;

end architecture;
