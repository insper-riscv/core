library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_WB is
  
    port (
        source_ex     : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        source_memory : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        selector      : in  std_logic;
        destination   : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of STAGE_WB is
        
begin
    MODULE_WRITE_BACK : entity WORK.MODULE_WRITE_BACK
        port map (
            source_ex     => source_ex,
            source_memory => source_memory,
            selector      => selector,
            destination   => destination
        );
    

end architecture;