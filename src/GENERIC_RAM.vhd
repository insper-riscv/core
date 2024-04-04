library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_RAM is

    generic (
        DATA_WIDTH        : natural := XLEN;
        ADDRESS_WIDTH     : natural := XLEN;
        ADDRESSABLE_WIDTH : natural := 10
    );

    port (
        clock        : in  std_logic;
        enable       : in  std_logic;
        enable_read  : in  std_logic;
        enable_write : in  std_logic;
        address      : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        source       : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL OF GENERIC_RAM IS

    subtype word_t is std_logic_vector((DATA_WIDTH - 1) downto 0);
    type memory_t is array(0 to (2**ADDRESSABLE_WIDTH - 1)) of word_t;

    signal ram: memory_t;

    -- Utiliza uma quantidade menor de endereços locais:
    signal local_address : std_logic_vector((ADDRESSABLE_WIDTH - 1) downto 0);

begin

    -- Ajusta o enderecamento para o acesso de 32 bits.
    local_address <= address((ADDRESSABLE_WIDTH + 1) downto 2);

    WRITE : process(clock)
    begin
        if(rising_edge(clock)) then
            STORE : if(enable_write = '1' AND enable = '1') then
                ram(to_integer(unsigned(local_address))) <= source ;
            end if;
        end if;
    end process;

    destination <= ram(to_integer(unsigned(local_address))) when (
                       enable_read = '1' and enable = '1'
                   ) else
                   (others => 'Z');

end architecture;
