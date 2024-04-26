library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity GENERIC_ROM IS

    generic (
        DATA_WIDTH        : natural := 8;
        ADDRESS_WIDTH     : natural := 8;
        ADDRESSABLE_WIDTH : natural := 7
    );

    port (
        address     : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0) 
    );

end entity;

architecture RTL of GENERIC_ROM is

    type memory_block is array(0 TO (2**ADDRESSABLE_WIDTH - 1)) of std_logic_vector((DATA_WIDTH - 1) DOWNTO 0);

    function memory_init return memory_block is
        variable tmp : memory_block := (others => (others => '0'));
    begin
    
        -- start memory
        tmp(0) := "00000001";
        tmp(1) := "00000010";
        tmp(2) := "00000100";
        tmp(3) := "00001000";
        tmp(4) := "00010000";
        tmp(5) := "00100000";
        tmp(6) := "01000000";
        tmp(7) := "10000000";
        -- end memory

        return tmp;
    end function;

    signal memory_ROM : memory_block := memory_init;

begin

    process(address)
        variable index : natural;
    begin
        index := to_integer(unsigned(address));
        if (index < (2**ADDRESSABLE_WIDTH - 1)) then
            destination <= memory_ROM(index);
        else
            destination <= (others => '0');
        end if;
    end process;

end architecture;
