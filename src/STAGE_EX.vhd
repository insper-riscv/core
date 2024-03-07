library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU is
  
    port (
        opcode                : in std_logic_vector(OPCODE_RANGE);
        function_3            : in std_logic_vector(FUNCTION_RANGE);
        function_7            : in std_logic_vector(6 downto 0);
        source_register_1     : in std_logic_vector(XLEN_RANGE);
        source_register_2     : in std_logic_vector(XLEN_RANGE);
        source_memory         : in std_logic_vector(XLEN_RANGE);
        source_write_back     : in std_logic_vector(XLEN_RANGE);
        source_immediate      : in std_logic_vector(XLEN_RANGE);
        select_foward_1       : in std_logic_vector(1 downto 0);
        select_foward_2       : in std_logic_vector(1 downto 0);
        flag_z                : out std_logic;
        source_register_2_out : out std_logic_vector(XLEN_RANGE);
        destination           : out std_logic_vector(XLEN_RANGE)
    );

end entity;

architecture RTL of MODULE_ALU is

    -- No signals

begin

    MODULE_ALU : entity WORK.MODULE_ALU
        port map (
            opcode                => opcode,               
            function_3            => function_3,           
            function_7            => function_7,           
            source_register_1     => source_register_1,    
            source_register_2     => source_register_2,    
            source_memory         => source_memory,        
            source_write_back     => source_write_back,    
            source_immediate      => source_immediate,     
            select_foward_1       => select_foward_1,      
            select_foward_2       => select_foward_2,      
            flag_z                => flag_z,               
            source_register_2_out => source_register_2_out,
            destination           => destination
        );

end architecture;
