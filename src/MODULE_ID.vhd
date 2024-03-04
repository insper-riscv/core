library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ID is

    generic (
        DATA_WIDTH_0  : natural := DATA_WIDTH;
        ADDRESS_WIDTH : natural := 5
    );

    port (
        enable              : in  std_logic := '0';
        address_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_1    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_2    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        data_destination    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        instruction         : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        pc_out              : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        id_source           : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        immediate_source    : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_source_1       : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_source_2       : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ID is
        signal immediate_shift : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
begin   
    SIGNAL_EXTENDER : entity WORK.GENERIC_SIGNAL_EXTENDER
        port map (
            source => immediate_shift,
            enable_unsigned => '0',
            destination => immediate_source
        );

    immediate_shift <= immediate_source(29 downto 0) & "00";

    ADDER : entity WORK.GENERIC_ADDER
        port map (
            source_1 => immediate_shift,
            source_2 => pc_out,
            destination => id_source
        );

    REGISTER_BANK : entity WORK.GENERIC_REGISTERS_BANK
        port (
        enable              => enable,
        address_destination => address_destination,
        address_source_1    => address_source_1,
        address_source_2    => address_source_2,
        data_destination    => data_destination,
        data_source_1       => data_source_1,
        data_source_2       => data_source_2
    );

    

end architecture;