library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity TOP_LEVEL is

    generic (
        EXTERNAL_PROGRAM : boolean := FALSE;
        EXTERNAL_MEMORY  : boolean := FALSE
    );

    port (
        CLOCK           : in  std_logic                    := '0';
        DATA_PROGRAM    : in  t_DATA                       := (others => '0');
        DATA_MEMORY_IN  : in  t_DATA                       := (others => '0');
        SW              : in  std_logic_vector(3 downto 0) := (others => '0');
        DATA_MEMORY_OUT : out t_DATA;
        ADDRESS_PROGRAM : out t_DATA;
        ADDRESS_MEMORY  : out t_DATA;
        MEMORY_READ     : out std_logic;
        MEMORY_WRITE    : out std_logic;
        LED             : out std_logic_vector(7 downto 0) := (others => '0')
    );

end entity;

architecture RTL of TOP_LEVEL is

    signal control_if            : t_CONTROL_IF;
    signal signals_if_id         : t_SIGNALS_IF_ID;
    signal signals_id_ex         : t_SIGNALS_ID_EX;
    signal signals_ex_mem        : t_SIGNALS_EX_MEM;
    signal signals_mem_wb        : t_SIGNALS_MEM_WB;
    signal enable_destination       : std_logic;
    signal address_jump          : t_DATA;
    signal select_destination    : t_REGISTER;
    signal data_destination      : t_DATA;

    signal control_memory        : t_CONTROL_MEM;
    signal address_memory_0      : t_DATA;
    signal data_memory_in_0      : t_DATA;
    signal data_memory_out_0     : t_DATA;

    signal source_wb             : t_SIGNALS_MEM_WB;

begin

    LED(0) <= SW(1);
    LED(7 downto 1) <= (others => '0');

    STAGE_IF : entity WORK.STAGE_IF
        port map (
            clock           => CLOCK,
            enable          => '1',
            source          => control_if,
            address_jump    => address_jump,
            address_program => signals_if_id.address_program
        );

    ADDRESS_PROGRAM <= signals_if_id.address_program;

    PROGRAM_SOURCE : if EXTERNAL_PROGRAM = TRUE generate
        signals_if_id.data_instruction <= DATA_PROGRAM;
    else generate
        ROM : entity WORK.GENERIC_ROM
            port map (
                address     => signals_if_id.address_program,
                destination => signals_if_id.data_instruction
            );
    end generate;

    STAGE_ID : entity WORK.STAGE_ID
        port map (
            clock               => CLOCK,
            clear               => '0',
            enable              => '1',
            enable_destination  => enable_destination,
            source              => signals_if_id,
            select_destination  => select_destination,
            data_destination    => data_destination,
            address_jump        => address_jump,
            control_if          => control_if,
            signals_ex          => signals_id_ex
        );

    STAGE_EX : entity WORK.STAGE_EX
        port map (
            clock       => CLOCK,
            clear       => '0',
            enable      => '1',
            source      => signals_id_ex,
            destination => signals_ex_mem
        );

    STAGE_MEM : entity WORK.STAGE_MEM
        port map (
            clock          => CLOCK,
            clear          => '0',
            enable         => '1',
            source         => signals_ex_mem,
            control_memory => control_memory,
            address_memory => address_memory_0,
            data_memory    => data_memory_out_0,
            destination    => signals_mem_wb
        );

    ADDRESS_MEMORY  <= address_memory_0;
    DATA_MEMORY_OUT <= data_memory_out_0;
    MEMORY_READ     <= control_memory.enable_read;
    MEMORY_WRITE    <= control_memory.enable_write;

    MEMORY_SOURCE : if EXTERNAL_PROGRAM = TRUE generate
        data_memory_in_0 <= DATA_MEMORY_IN;
    else generate
        RAM : entity WORK.GENERIC_RAM
            port map (
                clock        => CLOCK,
                enable       => '1',      
                enable_read  => control_memory.enable_read,
                enable_write => control_memory.enable_write,
                address      => address_memory_0,
                source       => data_memory_out_0,
                destination  => data_memory_in_0 
            );
    end generate;

    source_wb.control_wb         <= signals_mem_wb.control_wb;
    source_wb.data_memory        <= data_memory_in_0;
    source_wb.data_destination   <= signals_mem_wb.data_destination;
    source_wb.select_destination <= signals_mem_wb.select_destination;

    STAGE_WB : entity WORK.STAGE_WB
        port map (
            clock              => CLOCK,
            clear              => '0',
            enable             => '1',
            enable_destination => enable_destination,
            source             => source_wb,
            select_destination => select_destination,
            destination        => data_destination
        );

end architecture;
