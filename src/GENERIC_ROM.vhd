library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.MATH_REAL.ALL;
use std.textio.all;

library WORK;

entity GENERIC_ROM is

    generic (
        DATA_WIDTH        : natural := 8;
        ADDRESS_WIDTH     : natural := 8;
        ADDRESSABLE_WIDTH : natural := 7;
        INIT_FILE         : string  := "../data/mif/generic_rom_dummy.mif"
    );

    port (
        clock       : in  std_logic := '1';
        address     : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0) 
    );

end entity;

architecture RTL of GENERIC_ROM is

    type memory_block is array(0 TO (2**ADDRESSABLE_WIDTH - 1)) of std_logic_vector((DATA_WIDTH - 1) DOWNTO 0);

    signal memory_ROM: memory_block;
    attribute ram_init_file : string;
    attribute ram_init_file of memory_ROM : signal is INIT_FILE;

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
