library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_ID is

    port (
        control            : in  t_CONTROL_CLK_CLR_EN;
        source             : in  t_SIGNALS_IF_ID;
        select_destination : in  t_REGISTER;
        data_destination   : in  t_DATA;
        address_jump       : out t_DATA;
        control_if         : out t_CONTROL_IF;
        signals_ex         : out t_SIGNALS_ID_EX
    );

end entity;

architecture RTL of STAGE_ID is

    signal data_source_1 : t_DATA;

begin

    MODULE_CONTROL_UNIT : entity WORK.MODULE_CONTROL_UNIT
        port map (
            instruction      => source.data_instruction,
            address_program  => source.address_program,
            data_source_1    => data_source_1,
            jump_address     => address_jump,
            immediate_source => signals_ex.data_immediate,
            control_if       => control_if,
            control_ex       => signals_ex.control_ex,
            control_mem      => signals_ex.control_mem,
            control_wb       => signals_ex.control_wb
    );

    MODULE_REGISTER_FILE : entity WORK.MODULE_REGISTER_FILE
        port map (
        clock              => control.clock,              
        enable             => control.enable,             
        select_destination => select_destination,
        data_destination   => data_destination,   
        instruction        => source.data_instruction,          
        data_source_1      => data_source_1,      
        data_source_2      => signals_ex.data_source_2   
    );

    process(source.data_instruction) is
        variable instruction : t_RV32I_INSTRUCTION;
    begin
        instruction := to_RV32I_INSTRUCTION(source.data_instruction);

        signals_ex.data_source_1      <= data_source_1;
        signals_ex.funct_7            <= instruction.funct_7;
        signals_ex.funct_3            <= instruction.funct_3;
        signals_ex.opcode             <= instruction.opcode;
        signals_ex.select_destination <= instruction.select_destination;
    end process;

end architecture;
