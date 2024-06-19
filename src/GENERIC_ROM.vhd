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

architecture SYN of GENERIC_ROM is

    type memory_block is array(0 TO (2**ADDRESSABLE_WIDTH - 1)) of std_logic_vector((DATA_WIDTH - 1) DOWNTO 0);

    impure function read_mif_file return memory_block is
        file     file_text    : text open READ_MODE is INIT_FILE;
        variable file_line    : line;
        variable file_begin   : string(1 to 13);
        variable file_address : integer := 0;
        variable file_sep     : string(1 to 1);
        variable result       : memory_block := (others => (others => '0'));
    begin
        while not endfile(file_text) loop
            readline(file_text, file_line);
            if file_line'length = 13 then
                read(file_line, file_begin);

                if file_begin = "CONTENT BEGIN" then
                    exit;
                end if;
            end if;
        end loop;

        while not endfile(file_text) loop
            readline(file_text, file_line);

            if file_line'length = 4 then
                exit;
            end if;

            read(file_line, file_address);
            read(file_line, file_sep);
            read(file_line, result(file_address));
        end loop;

        file_close(file_text);

        return result;
    end function;

    signal memoryy : memory_block := read_mif_file;

begin

    process(address)
        variable index : natural;
    begin
        index := to_integer(unsigned(address));
        if (index < (2**ADDRESSABLE_WIDTH - 1)) then
            destination <= memoryy(index);
        else
            destination <= (others => '0');
        end if;
    end process;

end architecture;
