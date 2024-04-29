library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity MODULE_MEMORY_INTERFACE is

    generic (
        FUNCTION_WIDTH : natural := WORK.RV32I.FUNCT3_WIDTH;
        DATA_WIDTH     : natural := WORK.RV32I.XLEN
    );

    port (
        select_function      : in  std_logic_vector((FUNCTION_WIDTH - 1) downto 0);
        source_data_in       : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_data_out      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination_data_in  : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination_data_out : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_MEMORY_INTERFACE is

    -- No signals

begin

    DATA_IN : entity WORK.RV32I_TYPE_CONVERTER
        port map (
            select_type => select_function,
            source      => source_data_in,
            destination => destination_data_in
        );

    DATA_OUT : entity WORK.RV32I_TYPE_CONVERTER
        port map (
            select_type => select_function,
            source      => source_data_out,
            destination => destination_data_out
        );

end architecture;
