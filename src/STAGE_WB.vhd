library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_WB is
  
    port (
        source           : in t_MEM_WB_SIGNALS;
        enable           : out std_logic;
        address_register : out std_logic_vector(4 downto 0);
        destination      : out std_logic_vector(XLEN_RANGE)
    );

end entity;

architecture RTL of STAGE_WB is

    -- No signals

begin

    MODULE_WRITE_BACK : entity WORK.MODULE_WRITE_BACK
        port map (
            source_memory => source.destination,
            source_ex     => source.address,
            selector      => source.wb_signals.select_destination,
            destination   => destination
        );

end architecture;
