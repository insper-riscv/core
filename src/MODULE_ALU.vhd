library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU is

    generic (
        DATA_WIDTH_0 : natural := DATA_WIDTH
    );
  
    port (
        opcode                : in std_logic_vector(OPCODE_RANGE);
        function_3            : in std_logic_vector(FUNCTION_RANGE);
        function_7            : in std_logic_vector(6 downto 0);
        register_source_1     : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        register_source_2     : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        memory_source         : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        write_back_source     : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        immediate_source      : in std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        flag_z                : out std_logic;
        register_source_2_out : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        destination           : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ALU is

        signal MUX_REGISTER_ALU_1_OUT : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        signal MUX_REGISTER_ALU_2_OUT : std_logic_vector((DATA_WIDTH_0 - 1) downto 0); 
        signal select_function : std_logic_vector(3 downto 0);
begin

    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1 => register_source_1,
            source_2 => memory_source,
            source_3 => write_back_source,
            source_4 => (others => '0'),
            selector => forwarding_unit_1,
            destination => MUX_REGISTER_ALU_1_OUT
        );

    MUX_REGISTER_ALU_2 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => register_source_2,
            source_2    => memory_source,
            source_3    => write_back_source,
            source_4    => immediate_source,
            selector    => forwarding_unit_1,
            destination => MUX_REGISTER_ALU_2_OUT
        );

    ALU_CONTROLLER : entity WORK.RV32I_ALU_CONTROLLER
        port map (
            opcode      => opcode,
            function_3  => function_3,
            function_7  => function_7,
            destination => select_function
        );

    ALU : entity WORK.RV32I_ALU
        port (
            invert_source_1 => select_function[3],
            invert_source_2 => select_function[2],
            select_function => select_function[1 downto 0],
            source_1        => MUX_REGISTER_ALU_1_OUT,
            source_2        => MUX_REGISTER_ALU_2_OUT,
            destination     => destination,
            flag_z          => flag_z
        );

end architecture;