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
        select_source_1        : std_logic_vector(1 downto 0);
        select_source_2        : std_logic_vector(1 downto 0);
        source_pc              : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_register_1      : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_register_2      : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_immediate       : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        opcode                 : t_OPCODE_COMPACT;
        function_3             : t_FUNCTION;
        function_7             : in std_logic_vector(6 downto 0);
        --source_memory          : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        --source_write_back      : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        --select_foward_1        : in std_logic_vector(1 downto 0);
        --select_foward_2        : in std_logic_vector(1 downto 0);
        --flag_z                 : out std_logic;
        source_register_2_out  : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination            : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ALU is

        signal mux_register_alu_1_out : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal mux_register_alu_2_out : std_logic_vector((DATA_WIDTH - 1) downto 0); 
        signal select_function : std_logic_vector(3 downto 0);
begin

    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1 => source_register_1,
            source_2 => source_pc,
            source_3 => (others => '0'),
            source_4 => (others => '0'),
            selector => select_source_1,
            destination => mux_register_alu_1_out
        );

    MUX_REGISTER_ALU_2 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => source_register_2,
            source_2    => source_immediate,
            source_3    => std_logic_vector(to_unsigned(4, 32)),
            source_4    => (others => '0'),
            selector    => select_source_2,
            destination => mux_register_alu_2_out
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
            source_1        => mux_register_alu_1_out,
            source_2        => mux_register_alu_2_out,
            destination     => destination
            --flag_z          => flag_z
        );
    
    source_register_2_out <= source_register_2;
end architecture;