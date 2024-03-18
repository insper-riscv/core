library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_ROM IS

    generic (
        DATA_WIDTH        : natural := XLEN;
        ADDRESS_WIDTH     : natural := XLEN;
        ADDRESSABLE_WIDTH : natural := 7
    );

    port (
        address     : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0) 
    );
end entity;

architecture RTL of GENERIC_ROM is

    type memory_block is array(0 TO 2**ADDRESSABLE_WIDTH - 1) of std_logic_vector((DATA_WIDTH - 1) DOWNTO 0);

    function memory_init return memory_block is
        variable tmp : memory_block := (others => (others => '0'));
    begin
  
        tmp(0) := "00000000000000000001010000110111";
        tmp(4) := "00000000000000000001010000110111";
        tmp(8) := "00000000000000000001010000110111";
        tmp(12) := "00000000000000000001010000110111";

        return tmp;
    end function;

    signal memory_ROM : memory_block := memory_init;

begin

    process(address)
        variable index : natural;
    begin
        index := to_integer(unsigned(address));
        if (index < memory_ROM'length) then
            destination <= memory_ROM(index);
        else
            destination <= (others => '0');
        end if;
    end process;

end architecture;
