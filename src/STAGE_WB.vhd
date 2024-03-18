library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_WB is
  
    port (
        source             : in  t_SIGNALS_MEM_WB;
        enable_destination : out std_logic;
        select_destination : out t_REGISTER;
        destination        : out t_DATA
    );

end entity;

architecture RTL of STAGE_WB is

    -- No signals

begin

    MODULE_WRITE_BACK : entity WORK.MODULE_WRITE_BACK
        port map (
            source_memory => source.data_memory,
            source_ex     => source.data_destination,
            selector      => source.control_wb.select_destination,
            destination   => destination
        );

    enable_destination <= source.control_wb.enable_destination;

end architecture;
