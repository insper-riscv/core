library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.TOP_LEVEL_TYPES.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_REGISTERS_BANK is

    generic (
        DATA_WIDTH_0  : natural := DATA_WIDTH;
        ADDRESS_WIDTH : natural
    );

    port (
        clock               : in  std_logic;
        enable              : in  std_logic := '0';
        address_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_1    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_2    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        data_destination    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_source_1       : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_source_2       : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_REGISTERS_BANK is

    subtype word_t is std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
    type memory_t is array((2**ADDRESS_WIDTH - 1) downto 0) of word_t;

    function init_memory return memory_t is
        variable tmp : memory_t := (others => (others => '0'));
    begin
        for i in start_index to end_index loop
            tmp(i) <= (others => '0');
        end loop;
        return tmp;
    end function;

    shared variable registers : memory_t := init_memory;

    constant ZERO : std_logic_vector((DATA_WIDTH_0 - 1) downto 0) := (others => '0');
    constant ADDRESS_ZERO : std_logic_vector((ADDRESS_WIDTH - 1) downto 0) := (others => '0');

begin

    process(clock)
    begin
        if (rising_edge(clock)) then
            if (enable = '1') then
                registers(to_integer(unsigned(address_destination))) := data_destination;
            end if;
        end if;
    end process;

    data_source_1 <= ZERO when address_source = ADDRESS_ZERO else
                     registers(to_integer(unsigned(address_source)));

    data_source_2 <= ZERO when address_target = ADDRESS_ZERO else
                     registers(to_integer(unsigned(address_target)));

end architecture;
