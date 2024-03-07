library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_WB is
  
    port (
        source_ex     : in  std_logic_vector(XLEN_RANGE);
        source_memory : in  std_logic_vector(XLEN_RANGE);
        selector      : in  std_logic;
        destination   : out std_logic_vector(XLEN_RANGE)
    );

end entity;

architecture RTL of STAGE_WB is

    -- No signals

begin

    MODULE_WRITE_BACK : entity WORK.MODULE_WRITE_BACK
        port map (
            source_ex     => source_ex,
            source_memory => source_memory,
            selector      => selector,
            destination   => destination
        );

end architecture;
