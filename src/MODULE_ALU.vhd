library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU is

    generic (
        DATA_WIDTH_0 : natural := DATA_WIDTH
    );
  
    port (
        alu_op : in std_logic_vector(1 downto 0);
        data_source_1 : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_source_2 : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_mem : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        data_wb : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        flagzero : out std_logic;
        alu_out: out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ALU is

        signal MUX_REGISTER_ALU_1_OUT : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        signal MUX_REGISTER_ALU_2_OUT : std_logic_vector((DATA_WIDTH_0 - 1) downto 0); 
begin

    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1 => data_source_1,
            source_2 => data_mem,
            source_3 => data_wb,
            source_4 => (others => '0'),
            selector => forwarding_unit_1,
            destination => MUX_REGISTER_ALU_1_OUT
        );

    MUX_REGISTER_ALU_2 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => data_source_2,
            source_2    => data_mem,
            source_3    => data_wb,
            source_4    => (others => '0'),
            selector    => forwarding_unit_1,
            destination => MUX_REGISTER_ALU_2_OUT
        );

    ALU : entity WORK.RV32I_ALU
        port (
            invert_source_1 => MUX_REGISTER_ALU_1_OUT,
            invert_source_2 => MUX_REGISTER_ALU_2_OUT,
            select_function => alu_op,
            source_1        => MUX_REGISTER_ALU_1_OUT,
            source_2        => MUX_REGISTER_ALU_2_OUT,
            destination     => alu_out,
            flag_z          => flagzero
        );

end architecture;