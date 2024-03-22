library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_ID is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );

    port (
        clock              : in  std_logic;
        clear              : in  std_logic;
        enable             : in  std_logic;
        enable_destination : in  std_logic;
        source             : in  t_SIGNALS_IF_ID;
        select_destination : in  t_REGISTER;
        data_destination   : in  t_DATA;
        address_jump       : out t_DATA;
        control_if         : out t_CONTROL_IF;
        signals_ex         : out t_SIGNALS_ID_EX
    );

end entity;

architecture RTL of STAGE_ID is

    signal source_0      : t_SIGNALS_IF_ID := NULL_SIGNALS_IF_ID;
    signal data_source_1 : t_DATA;

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(source, clear, clock, enable)
        begin
            if (rising_edge(clock)) then
                SET_RESET : if (enable = '1') then
                    source_0 <= source;
                elsif (clear = '1') then
                    source_0 <= NULL_SIGNALS_IF_ID;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    MODULE_CONTROL_UNIT : entity WORK.MODULE_CONTROL_UNIT
        port map (
            instruction      => source_0.data_instruction,
            address_program  => source_0.address_program,
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
        clock              => clock,              
        enable             => enable,             
        select_destination => select_destination,
        data_destination   => data_destination,   
        instruction        => source_0.data_instruction,          
        data_source_1      => data_source_1,      
        data_source_2      => signals_ex.data_source_2   
    );

    signals_ex.address_program <= source_0.address_program;

    process(source_0.data_instruction) is
        variable instruction : t_RV32I_INSTRUCTION;
    begin
        instruction := to_RV32I_INSTRUCTION(source_0.data_instruction);

        signals_ex.data_source_1      <= data_source_1;
        signals_ex.funct_7            <= instruction.funct_7;
        signals_ex.funct_3            <= instruction.funct_3;
        signals_ex.opcode             <= instruction.opcode;
        signals_ex.select_destination <= instruction.select_destination;
    end process;

end architecture;
