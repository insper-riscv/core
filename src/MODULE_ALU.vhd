library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU is

    generic (
        DATA_WIDTH : natural := DATA_WIDTH
    );
  
    port (
        opcode                : in std_logic_vector(OPCODE_RANGE);
        function_3            : in std_logic_vector(FUNCTION_RANGE);
        function_7            : in std_logic_vector(6 downto 0);
        source_register_1     : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_register_2     : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_memory         : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_write_back     : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_immediate      : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        select_foward_1       : in std_logic_vector(1 downto 0);
        select_foward_2       : in std_logic_vector(1 downto 0);
        flag_z                : out std_logic;
        source_register_2_out : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination           : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ALU is

        signal MUX_REGISTER_ALU_1_OUT : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal MUX_REGISTER_ALU_2_OUT : std_logic_vector((DATA_WIDTH - 1) downto 0); 
        signal select_function : std_logic_vector(3 downto 0);
begin

    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1 => source_register_1,
            source_2 => source_memory,
            source_3 => source_write_back,
            source_4 => (others => '0'),
            selector => select_foward_1,
            destination => MUX_REGISTER_ALU_1_OUT
        );

    MUX_REGISTER_ALU_2 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => source_register_2,
            source_2    => source_memory,
            source_3    => source_write_back,
            source_4    => source_immediate,
            selector    => select_foward_2,
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
        port map (
            invert_source_1 => select_function(3),
            invert_source_2 => select_function(2),
            select_function => select_function(1 downto 0),
            source_1        => MUX_REGISTER_ALU_1_OUT,
            source_2        => MUX_REGISTER_ALU_2_OUT,
            destination     => destination,
            flag_z          => flag_z
        );

end architecture;