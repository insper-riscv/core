library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_EX is
  
    port (
        source      : in  t_SIGNALS_ID_EX;
        destination : out t_SIGNALS_EX_MEM
    );

end entity;

architecture RTL of STAGE_EX is

    signal select_function : std_logic_vector(3 downto 0);

begin

    MODULE_ALU_CONTROLLER : entity WORK.MODULE_ALU_CONTROLLER
        port map (
            opcode      => source.opcode,
            function_3  => source.funct_3,
            function_7  => source.funct_7,
            destination => select_function
        );

    MODULE_ALU : entity WORK.MODULE_ALU
        port map (
            select_source_1 => source.control_ex.select_source_1,
            select_source_2 => source.control_ex.select_source_2,
            address_program => source.address_program,
            data_source_1   => source.data_source_1,
            data_source_2   => source.data_source_2,
            data_immediate  => source.data_immediate,
            select_function => select_function,
            destination     => destination.address_pointer
        );

    destination.control_mem        <= source.control_mem;
    destination.control_wb         <= source.control_wb;
    destination.select_destination <= source.select_destination;

end architecture;
