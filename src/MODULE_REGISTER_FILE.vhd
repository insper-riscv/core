library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_REGISTER_FILE is

    generic (
        DATA_WIDTH    : natural := WORK.CPU.DATA_WIDTH;
        ADDRESS_WIDTH : natural := WORK.CPU.REGISTER_ADDRESS_WIDTH
    );

    port (
        clock              : in  std_logic;
        enable             : in  std_logic;
        select_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        select_source_1    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        select_source_2    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        data_destination   : in  std_logic_vector((DATA_WIDTH    - 1) downto 0);
        data_source_1      : out std_logic_vector((DATA_WIDTH    - 1) downto 0);
        data_source_2      : out std_logic_vector((DATA_WIDTH    - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_REGISTER_FILE is

    -- No Signals

begin

    REGISTER_FILE : entity WORK.RV32I_REGISTER_FILE
        port map (
            clock               => clock,
            enable              => enable,
            address_destination => select_destination,
            address_source_1    => select_source_1,
            address_source_2    => select_source_2,
            data_destination    => data_destination,
            data_source_1       => data_source_1,
            data_source_2       => data_source_2
    );

end architecture;
