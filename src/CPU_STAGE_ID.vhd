library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_STAGE_ID is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );

    port (
        clock              : in  std_logic;
        clear              : in  std_logic;
        enable             : in  std_logic;
        enable_destination : in  std_logic;
        source             : in  WORK.CPU.t_SIGNALS_IF_ID;
        select_destination : in  WORK.CPU.t_REGISTER;
        data_destination   : in  WORK.CPU.t_DATA;
        address_jump       : out WORK.CPU.t_DATA;
        control_if         : out WORK.CPU.t_CONTROL_IF;
        signals_ex         : out WORK.CPU.t_SIGNALS_ID_EX
    );

end entity;

architecture RV32I of CPU_STAGE_ID is

    signal source_0            : WORK.CPU.t_SIGNALS_IF_ID := WORK.CPU.NULL_SIGNALS_IF_ID;
    signal control_id          : WORK.CPU.t_CONTROL_ID;
    signal data_source_1       : WORK.CPU.t_DATA;
    signal data_source_2       : WORK.CPU.t_DATA;
    signal funct_3             : WORK.RV32I.t_FUNCT3;
    signal is_branch_condition : std_logic;

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(source, clear, clock, enable)
        begin
            if (rising_edge(clock)) then
                SET_RESET : if (enable = '1') then
                    source_0 <= source;
                elsif (clear = '1') then
                    source_0 <= WORK.CPU.NULL_SIGNALS_IF_ID;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    signals_ex.address_program <= source_0.address_program;
    signals_ex.data_source_1   <= data_source_1;
    signals_ex.data_source_2   <= data_source_2;

    process(source_0.data_instruction) is
        variable instruction : WORK.RV32I.t_INSTRUCTION;
    begin
        instruction := WORK.RV32I.to_INSTRUCTION(source_0.data_instruction);

        signals_ex.funct_7            <= instruction.funct_7;
        signals_ex.funct_3            <= instruction.funct_3;
        funct_3                       <= instruction.funct_3;
        signals_ex.opcode             <= instruction.opcode;
        signals_ex.select_destination <= instruction.select_destination;
        signals_ex.select_source_1    <= instruction.select_source_1;
        signals_ex.select_source_2    <= instruction.select_source_2;
    end process;

    control_if.enable_jump <= control_id.enable_branch AND is_branch_condition;

    MODULE_CONTROL_UNIT : entity WORK.MODULE_CONTROL_UNIT(RV32I)
        port map (
            instruction => source_0.data_instruction,
            immediate   => signals_ex.data_immediate,
            control_if  => control_if,
            control_id  => control_id,
            control_ex  => signals_ex.control_ex,
            control_mem => signals_ex.control_mem,
            control_wb  => signals_ex.control_wb
    );

    MODULE_REGISTER_FILE : entity WORK.MODULE_REGISTER_FILE(RV32I)
        port map (
        clock              => clock,
        enable             => enable_destination,
        select_destination => select_destination,
        data_destination   => data_destination,   
        select_source_1    => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_1,
        select_source_2    => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_2,
        data_source_1      => data_source_1,      
        data_source_2      => data_source_2  
    );

    BRANCH_UNIT: entity WORK.MODULE_BRANCH_UNIT(RV32I)
        port map (
            selector         => control_id.select_jump,
            source_program   => source_0.address_program,
            source_immediate => signals_ex.data_immediate,
            source_register  => data_source_1,
            destination      => address_jump
        );

    BRANCH_COMPARE_UNIT: entity WORK.MODULE_BRANCH_COMPARE_UNIT(RV32I)
        port map (
            source_1        => data_source_1,
            source_2        => data_source_2,
            select_function => '0' & funct_3,
            destination     => is_branch_condition
        );

end architecture;