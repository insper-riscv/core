library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_STAGE_ID is

    generic (
        GENERATE_REGISTERS : boolean := TRUE;
		QUARTUS_MEMORY     : boolean := FALSE
    );

    port (
        clock                 : in  std_logic;
        clear                 : in  std_logic;
        enable                : in  std_logic;
        enable_destination    : in  std_logic;
        select_destination    : in  WORK.CPU.t_REGISTER;
        data_destination      : in  WORK.CPU.t_DATA;
        forward               : in  WORK.CPU.t_FORWARD_BRANCH;
        source                : in  WORK.CPU.t_SIGNALS_IF_ID;
        address_jump          : out WORK.CPU.t_DATA;
        control_if            : out WORK.CPU.t_CONTROL_IF;
        signals_ex            : out WORK.CPU.t_SIGNALS_ID_EX
    );

end entity;

architecture RV32I of CPU_STAGE_ID is

    signal source_0            : WORK.CPU.t_SIGNALS_IF_ID := WORK.CPU.NULL_SIGNALS_IF_ID;
    signal control_id          : WORK.CPU.t_CONTROL_ID;
    signal data_source_1       : WORK.CPU.t_DATA;
    signal forward_source_1    : WORK.CPU.t_DATA;
    signal data_source_2       : WORK.CPU.t_DATA;
    signal data_immediate      : WORK.CPU.t_DATA;
	signal address_out         : WORK.CPU.t_DATA;
    signal enable_flush        : std_logic;
    signal enable_branch       : std_logic;

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(clock)
        begin
            if (rising_edge(clock)) then
                if (enable = '1') then
                    if ((clear AND enable_flush) = '1') then
                        source_0 <= WORK.CPU.NULL_SIGNALS_IF_ID;
                    else
                        source_0 <= source;
                    end if;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    enable_flush <= control_id.enable_jump OR enable_branch;

    control_if.enable_stall  <= control_id.enable_branch or control_id.enable_jalr;
    control_if.select_source <= control_id.enable_jump OR enable_branch;

    signals_ex.address_program <= source_0.address_program;
    signals_ex.data_source_1   <= data_source_1;
    signals_ex.data_source_2   <= data_source_2;
    signals_ex.data_immediate  <= data_immediate;

    process(source_0.data_instruction) is
        variable instruction : WORK.RV32I.t_INSTRUCTION;
    begin
        instruction := WORK.RV32I.to_INSTRUCTION(source_0.data_instruction);

        signals_ex.funct_7            <= instruction.funct_7;
        signals_ex.funct_3            <= instruction.funct_3;
        signals_ex.opcode             <= instruction.opcode;
        signals_ex.select_destination <= instruction.select_destination;
        signals_ex.select_source_1    <= instruction.select_source_1;
        signals_ex.select_source_2    <= instruction.select_source_2;
    end process;

    MODULE_CONTROL_UNIT : entity WORK.MODULE_CONTROL_UNIT(RV32I)
        port map (
            clear       => '0',
            instruction => source_0.data_instruction,
            immediate   => data_immediate,
            control_id  => control_id,
            control_ex  => signals_ex.control_ex,
            control_mem => signals_ex.control_mem,
            control_wb  => signals_ex.control_wb
    );

    MODULE_REGISTER_FILE : entity WORK.MODULE_REGISTER_FILE(RV32I)
        port map (
        clock              => clock,
        clear              => '0',
        enable             => enable_destination,
        select_destination => select_destination,
        data_destination   => data_destination,
        select_source_1    => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_1,
        select_source_2    => WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).select_source_2,
        data_source_1      => data_source_1,
        data_source_2      => data_source_2
    );

	QUARTUS_DELAY : if (QUARTUS_MEMORY = TRUE) generate
        UPDATE : process(clock)
        begin
            if (rising_edge(clock)) then
                if (enable = '1') then
						address_out <= source_0.address_program;
                end if;
            end if;
        end process;
    else generate
         address_out <= source_0.address_program;
    end generate;

    BRANCH_UNIT: entity WORK.MODULE_BRANCH_UNIT(RV32I)
        port map (
            selector         => control_id.select_jump,
            source_program   => address_out,
            source_immediate => data_immediate,
            source_register  => forward_source_1,
            destination      => address_jump
        );

    BRANCH_COMPARE_UNIT: entity WORK.MODULE_BRANCH_COMPARE_UNIT(RV32I)
        port map (
            enable             => control_id.enable_branch,
            select_function    => "0" & WORK.RV32I.to_INSTRUCTION(source_0.data_instruction).funct_3,
            source_1           => data_source_1,
            source_2           => data_source_2,
            forward            => forward,
            data_source_1      => forward_source_1,
            destination        => enable_branch
        );

end architecture;
