library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity TOP_LEVEL is

    generic (
        EXTERNAL_PROGRAM : boolean := FALSE;
        EXTERNAL_MEMORY  : boolean := FALSE;
		  DEMONSTRATION  : boolean := TRUE
    );

    port (
        CLOCK           : in  std_logic                    := '0';
        -- DATA_PROGRAM    : in  t_DATA                       := (others => '0');
        -- DATA_MEMORY_IN  : in  t_DATA                       := (others => '0');
        -- SW              : in  std_logic_vector(9 downto 0);
		  LEDR  				: out std_logic_vector(9 downto 0) := (others => '0');
		  HEX0,HEX1, HEX2, HEX3, HEX4, HEX5 : out std_logic_vector(6 downto 0);
        DATA_MEMORY_OUT : out t_DATA;
        ADDRESS_PROGRAM : out t_DATA;
        ADDRESS_MEMORY  : out t_DATA;
        MEMORY_READ     : out std_logic;
        MEMORY_WRITE    : out std_logic
        -- LED             : out std_logic_vector(7 downto 0) := (others => '0')
    );

end entity;

architecture RTL of TOP_LEVEL is
	 
	 signal clock_processor      : std_logic := '0';
    signal control_if            : t_CONTROL_IF;
    signal signals_if_id         : t_SIGNALS_IF_ID;
    signal signals_id_ex         : t_SIGNALS_ID_EX;
    signal signals_ex_mem        : t_SIGNALS_EX_MEM;
    signal signals_mem_wb        : t_SIGNALS_MEM_WB;
    signal enable_destination    : std_logic;
    signal address_jump          : t_DATA;
    signal select_destination    : t_REGISTER;
    signal data_destination      : t_DATA;

    signal control_memory        : t_CONTROL_MEM;
    signal address_memory_0      : t_DATA;
    signal data_memory_in_0      : t_DATA;
    signal data_memory_out_0     : t_DATA;

    signal source_wb             : t_SIGNALS_MEM_WB;

begin
	CLOCK_DEMONSTRATION : if DEMONSTRATION = TRUE generate
    low_freq : entity work.GENERIC_LOW_FREQ
        generic map (n => 50000000) 
        port map (
            clock => CLOCK, 
            clock_out => clock_processor
        );
	 HEX5 <= "0001000";
	 HEX4 <= "1001111";
	 HEX3 <= "0010010";
	 HEX2 <= "1000110";
	 HEX1 <= "0111111";
	 HEX0 <= "1000001";
	 
	 
    LEDR(9) <= clock_processor;
	 else generate
		clock_processor <= CLOCK;
	end generate;

    STAGE_IF : entity WORK.STAGE_IF
        port map (
            clock           => clock_processor,
            enable          => '1',
            source          => control_if,
            address_jump    => address_jump,
            address_program => signals_if_id.address_program
        );

    ADDRESS_PROGRAM <= signals_if_id.address_program;

    -- PROGRAM_SOURCE : if EXTERNAL_PROGRAM = TRUE generate
        -- signals_if_id.data_instruction <= DATA_PROGRAM;
    -- else generate
	-- generate
        ROM : entity WORK.GENERIC_ROM
            port map (
                address     => signals_if_id.address_program,
                destination => signals_if_id.data_instruction
            );
    --end generate;

    STAGE_ID : entity WORK.STAGE_ID
        port map (
            clock               => clock_processor,
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
            clock                     => clock_processor,
            clear                     => '0',
            enable                    => '1',
            selector_forwarding_mem   => signals_mem_wb.select_destination,
            enable_mem                => signals_mem_wb.control_wb.enable_destination,
            selector_forwarding_wb    => select_destination,
            enable_wb                 => enable_destination,
            forwarding_mem_source     => signals_mem_wb.data_destination,
            forwarding_wb_source      => data_destination,
            source                    => signals_id_ex,
            destination               => signals_ex_mem
        );

    STAGE_MEM : entity WORK.STAGE_MEM
        port map (
            clock          => clock_processor,
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

    -- MEMORY_SOURCE : if EXTERNAL_PROGRAM = TRUE generate
        -- data_memory_in_0 <= DATA_MEMORY_IN;
    -- else generate
	 --generate
        RAM : entity WORK.GENERIC_RAM
            port map (
                clock        => clock_processor,
                enable       => '1',      
                enable_read  => control_memory.enable_read,
                enable_write => control_memory.enable_write,
                address      => address_memory_0,
                source       => data_memory_out_0,
                destination  => data_memory_in_0 
            );
    --end generate;

    source_wb.control_wb         <= signals_mem_wb.control_wb;
    source_wb.data_memory        <= data_memory_in_0;
    source_wb.data_destination   <= signals_mem_wb.data_destination;
    source_wb.select_destination <= signals_mem_wb.select_destination;

    STAGE_WB : entity WORK.STAGE_WB
        port map (
            clock              => clock_processor,
            clear              => '0',
            enable             => '1',
            enable_destination => enable_destination,
            source             => source_wb,
            select_destination => select_destination,
            destination        => data_destination
        );
	
		LEDR(0) <= data_destination(0);
		LEDR(1) <= data_destination(1);
		LEDR(2) <= data_destination(2);
		LEDR(3) <= data_destination(3);
		LEDR(4) <= data_destination(4);
		LEDR(5) <= data_destination(5);
		LEDR(6) <= data_destination(6);
		LEDR(7) <= data_destination(7);
		LEDR(8) <= data_destination(8);
	
end architecture;
