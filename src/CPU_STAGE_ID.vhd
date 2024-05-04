library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_STAGE_ID is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );

    port (
        clock                 : in  std_logic;
        clear                 : in  std_logic;
        enable                : in  std_logic;
        enable_destination    : in  std_logic;
        source                : in  WORK.CPU.t_SIGNALS_IF_ID;
        select_destination    : in  WORK.CPU.t_REGISTER;
        data_destination      : in  WORK.CPU.t_DATA;
        enable_read_ex        : in  std_logic;
        enable_destination_ex : in  std_logic;
        enable_read_mem       : in  std_logic;
        hazzard_register_ex   : in  WORK.CPU.t_REGISTER;
        hazzard_register_mem  : in  WORK.CPU.t_REGISTER;
        forward_register_mem  : in  WORK.CPU.t_REGISTER;
        forward_data_mem      : in  WORK.CPU.t_DATA;
        forward_enable_mem    : in  std_logic;
        flag_stall            : out std_logic;
        branch                : out std_logic;
        address_jump          : out WORK.CPU.t_DATA;
        control_if            : out WORK.CPU.t_CONTROL_IF;
        signals_ex            : out WORK.CPU.t_SIGNALS_ID_EX
    );

end entity;

architecture RV32I of CPU_STAGE_ID is

    signal source_0            : WORK.CPU.t_SIGNALS_IF_ID := WORK.CPU.NULL_SIGNALS_IF_ID;
    signal control_id          : WORK.CPU.t_CONTROL_ID;
    signal data_source_1       : WORK.CPU.t_DATA;
    signal data_source_2       : WORK.CPU.t_DATA;
    signal funct_3             : WORK.RV32I.t_FUNCT3;
    signal is_branch_condition : std_logic;
    signal enable_branch       : std_logic;

    signal control_unit_ex     : WORK.CPU.t_CONTROL_EX    := WORK.CPU.NULL_CONTROL_EX;
    signal control_unit_mem    : WORK.CPU.t_CONTROL_MEM   := WORK.CPU.NULL_CONTROL_MEM;
    signal control_unit_wb     : WORK.CPU.t_CONTROL_WB    := WORK.CPU.NULL_CONTROL_WB;
    signal control_ex          : WORK.CPU.t_CONTROL_EX    := WORK.CPU.NULL_CONTROL_EX;
    signal control_mem         : WORK.CPU.t_CONTROL_MEM   := WORK.CPU.NULL_CONTROL_MEM;
    signal control_wb          : WORK.CPU.t_CONTROL_WB    := WORK.CPU.NULL_CONTROL_WB;
    signal flag_hazzard        : std_logic;
    signal flag_stall_branch   : std_logic;
    signal enable_pipeline     : std_logic;
    signal forward_selector_1  : std_logic;
    signal forward_selector_2  : std_logic;

begin

    enable_pipeline <= (flag_hazzard OR (flag_stall_branch AND enable_branch)) XOR enable;

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(source, clear, clock, enable, enable_pipeline)
        begin
            if (rising_edge(clock)) then
                SET_RESET : if (enable_pipeline = '1') then
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

    branch <= (control_id.enable_jump OR is_branch_condition) AND NOT (flag_stall_branch);
    enable_branch <= control_id.enable_branch;

    MODULE_CONTROL_UNIT : entity WORK.MODULE_CONTROL_UNIT(RV32I)
        port map (
            instruction => source_0.data_instruction,
            immediate   => signals_ex.data_immediate,
            control_if  => control_if,
            control_id  => control_id,
            control_ex  => control_unit_ex,
            control_mem => control_unit_mem,
            control_wb  => control_unit_wb
    );

    HAZZARD_UNIT : entity WORK.CPU_HAZZARD_CONTROL_UNIT
        port map (
            stage_id_select_source_1     => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_1,
            stage_id_select_source_2     => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_2,
            stage_ex_enable_read         => enable_read_ex,
            stage_ex_enable_destination  => enable_destination_ex,
            stage_ex_select_destination  => hazzard_register_ex,
            stage_mem_enable_read        => enable_read_mem,
            stage_mem_select_destination => hazzard_register_mem,
            stall_branch                 => flag_stall_branch,
            destination                  => flag_hazzard
        );

    flag_stall <= flag_hazzard OR (flag_stall_branch AND enable_branch);

    STALL_MODULE : entity WORK.MODULE_STALL_MUX
        port map (
            control_ex_in   => control_unit_ex,
            control_mem_in  => control_unit_mem,
            control_wb_in   => control_unit_wb,
            selector        => flag_hazzard,
            control_ex_out  => signals_ex.control_ex,
            control_mem_out => signals_ex.control_mem,
            control_wb_out  => signals_ex.control_wb
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

    BRANCH_FORWARDING_UNIT : entity WORK.CPU_BRANCH_FORWARDING_UNIT
        port map (
        stage_id_select_source_1     => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_1,
        stage_id_select_source_2     => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_2,
        stage_mem_enable_destination => forward_enable_mem,
        stage_mem_select_destination => forward_register_mem,
        stage_id_select_1            => forward_selector_1,
        stage_id_select_2            => forward_selector_2
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
            enable             => enable_branch,
            source_1           => data_source_1,
            source_2           => data_source_2,
            select_function    => '0' & funct_3,
            forward_selector_1 => forward_selector_1,
            forward_selector_2 => forward_selector_2,
            forward_source     => forward_data_mem,
            destination        => is_branch_condition
        );

end architecture;
