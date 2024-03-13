library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_REGISTER_FILE is

    generic (
        DATA_WIDTH    : natural := XLEN;
        ADDRESS_WIDTH : natural := 5
    );

    port (
        clock               : in  std_logic;
        enable              : in  std_logic := '0';
        address_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        data_destination    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        instruction         : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_1       : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_2       : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_REGISTER_FILE is

begin   

    REGISTER_BANK : entity WORK.RV32I_REGISTER_FILE
        port map (
            clock               => clock,
            enable              => enable,
            address_destination => address_destination,
            address_source_1    => instruction(19 downto 15),
            address_source_2    => instruction(24 downto 20),
            data_destination    => data_destination,
            data_source_1       => data_source_1,
            data_source_2       => data_source_2
    );

end architecture;
