library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU is

    generic (
        DATA_WIDTH : natural := XLEN
    );
  
    port (
        select_source_1        : in  std_logic_vector(1 downto 0);
        select_source_2        : in  std_logic_vector(1 downto 0);
        address_program        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_1          : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_2          : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_immediate         : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        select_function        : in  std_logic_vector(4 downto 0);
        -- source_memory          : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        -- source_write_back      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        -- select_foward_1        : in  std_logic_vector(1 downto 0);
        -- select_foward_2        : in  std_logic_vector(1 downto 0);
        destination            : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ALU is

    signal alu_source_1 : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal alu_source_2 : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => data_source_1,
            source_2    => address_program,
            source_3    => std_logic_vector(to_unsigned(0, DATA_WIDTH)),
            source_4    => (others => '0'),
            selector    => select_source_1,
            destination => alu_source_1
        );

    MUX_REGISTER_ALU_2 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => data_source_2,
            source_2    => data_immediate,
            source_3    => std_logic_vector(to_unsigned(4, DATA_WIDTH)),
            source_4    => (others => '0'),
            selector    => select_source_2,
            destination => alu_source_2
        );

    ALU : entity WORK.RV32I_ALU
        port map (
            invert_source_1 => select_function(4),
            invert_source_2 => select_function(3),
            select_function => select_function(2 downto 0),
            source_1        => alu_source_1,
            source_2        => alu_source_2,
            destination     => destination
        );

end architecture;
