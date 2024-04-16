library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_REGISTER_FILE is

    generic (
        DATA_WIDTH      : natural   := WORK.RV32I.XLEN;
        ADDRESS_WIDTH   : natural   := WORK.RV32I.REGISTER_WIDTH
    );

    port (
        clock               : in  std_logic;
        enable              : in  std_logic                                         := '0';
        address_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_1    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_2    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        data_destination    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_1       : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_2       : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_REGISTER_FILE is

    type t_file is array (natural range <>) of std_logic_vector(DATA_WIDTH - 1 downto 0);

    constant ZERO           : std_logic_vector((DATA_WIDTH - 1) downto 0)       := (others => '0');
    constant ADDRESS_ZERO   : std_logic_vector((ADDRESS_WIDTH - 1) downto 0)    := (others => '0');

    signal registers    : t_file(0 to (2**ADDRESS_WIDTH - 1))   := (others => (others => '0'));

begin

    process(clock)
    begin
        if (rising_edge(clock)) then
            if (enable = '1') then
                registers(to_integer(unsigned(address_destination))) <= data_destination;
            end if;
        end if;
    end process;

    data_source_1 <=    ZERO when address_source_1 = ADDRESS_ZERO else
                        registers(to_integer(unsigned(address_source_1)));

    data_source_2 <=    ZERO when address_source_2 = ADDRESS_ZERO else
                        registers(to_integer(unsigned(address_source_2)));

end architecture;
