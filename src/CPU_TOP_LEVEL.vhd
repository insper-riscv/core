library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_TOP_LEVEL is

    port (
        clock           : in  std_logic := '0';
        clear           : in  std_logic := '0';
        enable          : in  std_logic := '1';
        memory_read     : out std_logic;
        memory_write    : out std_logic;
        data_program    : in  WORK.CPU.t_PROGRAM := (others => '0');
        data_memory_in  : in  WORK.CPU.t_DATA := (others => '0');
        data_memory_out : out WORK.CPU.t_DATA;
        address_program : out WORK.CPU.t_DATA;
        address_memory  : out WORK.CPU.t_DATA
    );

end entity;

architecture RV32I of CPU_TOP_LEVEL is

    signal control_if            : WORK.CPU.t_CONTROL_IF := WORK.CPU.NULL_CONTROL_IF;
    signal signals_if_id         : WORK.CPU.t_SIGNALS_IF_ID;
    signal signals_id_ex         : WORK.CPU.t_SIGNALS_ID_EX;
    signal signals_ex_mem        : WORK.CPU.t_SIGNALS_EX_MEM;
    signal signals_mem_wb        : WORK.CPU.t_SIGNALS_MEM_WB;
    signal enable_destination    : std_logic;
    signal address_jump          : WORK.RV32I.t_DATA;
    signal select_destination    : WORK.RV32I.t_REGISTER;
    signal data_destination      : WORK.RV32I.t_DATA;

    signal control_memory        : WORK.CPU.t_CONTROL_MEM;
    signal address_memory_0      : WORK.RV32I.t_DATA;
    signal data_memory_in_0      : WORK.RV32I.t_DATA;
    signal data_memory_out_0     : WORK.RV32I.t_DATA;

    signal source_wb             : WORK.CPU.t_SIGNALS_MEM_WB;

    signal branch                : std_logic;
    signal enable_read           : std_logic;
    signal flag_stall            : std_logic;

begin

    INSTRUCTION_FETCH : entity WORK.CPU_STAGE_IF(RV32I)
        port map (
            branch          => branch,
            clock           => clock,
            clear           => clear,
            enable          => enable,
            stall           => flag_stall,
            source          => control_if,
            address_jump    => address_jump,
            address_program => signals_if_id.address_program
        );

    address_program <= signals_if_id.address_program;
    signals_if_id.data_instruction <= data_program;

    INSTRUCTION_DECODE : entity WORK.CPU_STAGE_ID(RV32I)
        port map (
            clock               => clock,
            clear               => '0',
            enable              => enable,
            enable_destination  => enable_destination,
            source              => signals_if_id,
            select_destination  => select_destination,
            data_destination    => data_destination,
            enable_read         => enable_read,
            hazzard_register    => signals_ex_mem.select_destination,
            flag_stall          => flag_stall,
            branch              => branch,
            address_jump        => address_jump,
            control_if          => control_if,
            signals_ex          => signals_id_ex
        );

    EXECUTE : entity WORK.CPU_STAGE_EX(RV32I)
        port map (
            clock                     => clock,
            clear                     => clear,
            enable                    => enable,
            selector_forwarding_mem   => signals_mem_wb.select_destination,
            enable_mem                => signals_mem_wb.control_wb.enable_destination,
            selector_forwarding_wb    => select_destination,
            enable_wb                 => enable_destination,
            forwarding_mem_source     => signals_mem_wb.data_destination,
            forwarding_wb_source      => data_destination,
            source                    => signals_id_ex,
            enable_read               => enable_read,
            destination               => signals_ex_mem
        );

    MEMORY_ACCESS : entity WORK.CPU_STAGE_MEM(RV32I)
        port map (
            clock           => clock,
            clear           => clear,
            enable          => enable,
            source          => signals_ex_mem,
            data_memory_in  => data_memory_in_0,
            control_memory  => control_memory,
            address_memory  => address_memory_0,
            data_memory_out => data_memory_out_0,
            destination     => signals_mem_wb
        );

    address_memory   <= address_memory_0;
    data_memory_out  <= data_memory_out_0;
    memory_read      <= control_memory.enable_read;
    memory_write     <= control_memory.enable_write;
    data_memory_in_0 <= data_memory_in;

    source_wb.control_wb         <= signals_mem_wb.control_wb;
    source_wb.data_memory        <= signals_mem_wb.data_memory;
    source_wb.data_destination   <= signals_mem_wb.data_destination;
    source_wb.select_destination <= signals_mem_wb.select_destination;

    WRITE_BACK : entity WORK.CPU_STAGE_WB(RV32I)
        port map (
            clock              => clock,
            clear              => clear,
            enable             => enable,
            enable_destination => enable_destination,
            source             => source_wb,
            select_destination => select_destination,
            destination        => data_destination
        );

end architecture;
