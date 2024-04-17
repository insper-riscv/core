library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity GENERIC_RAM is

    generic (
        DATA_WIDTH        : natural := 8;
        ADDRESS_WIDTH     : natural := 8;
        BYTE_WIDTH        : natural := 8;
        HALFWORD_WIDTH    : natural := 16;
        ADDRESSABLE_WIDTH : natural := 7
    );

    port (
        clock          : in  std_logic;
        enable         : in  std_logic;
        enable_read    : in  std_logic;
        enable_write   : in  std_logic;
        store_byte     : in  std_logic;
        store_halfword : in  std_logic;
        address        : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        source         : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination    : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL OF GENERIC_RAM IS

    subtype word_t is std_logic_vector((DATA_WIDTH - 1) downto 0);
    type memory_t is array(0 to (2**ADDRESSABLE_WIDTH - 1)) of word_t;

    signal ram: memory_t;

    -- Utiliza uma quantidade menor de endereços locais:
    signal local_address : std_logic_vector((ADDRESSABLE_WIDTH - 1) downto 0);

begin

    -- Ajusta o enderecamento para o acesso endereçavel.
    local_address <= address((ADDRESSABLE_WIDTH - 1) downto 0);

    WRITE : process(clock)
    begin
        if(rising_edge(clock)) then
            STORE : if(enable_write = '1' AND enable = '1' AND store_byte = '1' AND store_halfword = '0') then
                ram(to_integer(unsigned(local_address))) <= ram(to_integer(unsigned(local_address)))((DATA_WIDTH - 1) downto BYTE_WIDTH) & source((BYTE_WIDTH - 1) downto 0);
            elsif(enable_write = '1' AND enable = '1' AND store_byte = '0' AND store_halfword = '1')  then
                ram(to_integer(unsigned(local_address))) <= ram(to_integer(unsigned(local_address)))((DATA_WIDTH - 1) downto HALFWORD_WIDTH) & source((HALFWORD_WIDTH - 1) downto 0);
            elsif(enable_write = '1' AND enable = '1' AND store_byte = '0' AND store_halfword = '0')  then
                ram(to_integer(unsigned(local_address))) <= source ;
            end if;
        end if;
    end process;

    destination <=  ram(to_integer(unsigned(local_address))) when (
                        enable_read = '1' and enable = '1'
                    ) else
                    (others => 'Z');

end architecture;
