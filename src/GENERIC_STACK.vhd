library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_STACK is

    generic (
        DATA_WIDTH_0 : natural := DATA_WIDTH;
        SIZE        : natural := 8
    );

    port (
        clock        : in  std_logic;
        enable_read  : in  std_logic;
        enable_write : in  std_logic;
        source       : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        destination  : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        overflow     : out std_logic
    );

end entity;

architecture LIFO of GENERIC_STACK is

    subtype word_t is std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
    type memory_t is array((SIZE - 1) downto 0) of word_t;

    shared variable registers : memory_t;

    signal top     : natural := 0;
    signal pointer : natural := 0;

begin

    STACK : process(clock, enable_read, enable_write, pointer) is
    begin
        if (rising_edge(clock)) then
            PUSH : if (enable_write = '1' and pointer < SIZE) then
                registers(pointer) := source;
                pointer <= pointer + 1;
            end if;

            POP : if (enable_read = '1' and pointer > 0) then
                pointer <= pointer - 1;
            end if;
        end if;
    end process;

    process(pointer)
    begin
        if (pointer < SIZE) then
            overflow <= '1';
        else
            overflow <= '0';
        end if;
    end process;

    top      <= 0 when (pointer = 0) else
                pointer - 1;

    destination <= registers(top);

end architecture;
