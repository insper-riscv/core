library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_MEMORY is

    generic (
        DATA_WIDTH_0  : natural := DATA_WIDTH;
        ADDRESS_WIDTH : natural := 32
    );
  
    port (
        clock             : in  std_logic;
        enable            : in  std_logic;
        enable_read       : in  std_logic;
        enable_write      : in  std_logic;
        source_ex         : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        register_source_2 : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        destination       : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_MEMORY is
        
begin
    RAM : entity WORK.GENERIC_RAM
        port map (
            clock        => clock,
            enable       => enable,      
            enable_read  => enable_read,
            enable_write => enable_write,
            address      => source_ex,    
            source       => register_source_2,      
            destination  => destination 
        );
    

end architecture;