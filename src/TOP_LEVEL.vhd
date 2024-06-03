library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity TOP_LEVEL is

    generic (
        PROGRAM_FILE   : string := "../data/mif/blink.mif";
		DEMONSTRATION  : boolean := FALSE;
		QUARTUS_MEMORY : boolean := FALSE
    );

    port (
        CLOCK           : in  std_logic                    := '0';
        --SW            : in  std_logic_vector(3 downto 0) := (others => '0');
        LEDR            : out std_logic_vector(0 downto 0) := (others => '0')
    );

end entity;

architecture RTL of TOP_LEVEL is

    signal data_program        : WORK.RV32I.t_PROGRAM;
    signal data_memory_in      : WORK.RV32I.t_DATA;
    signal data_memory_out     : WORK.RV32I.t_DATA;
    signal enable_memory_read  : std_logic;
    signal enable_memory_write : std_logic;
    signal address_program     : WORK.RV32I.t_DATA;
    signal address_memory      : WORK.RV32I.t_DATA;
    signal clock_processor     : std_logic := '0';

begin

    ROM : entity WORK.GENERIC_ROM
        generic map (
            DATA_WIDTH    => WORK.RV32I.XLEN,
            ADDRESS_WIDTH => WORK.RV32I.XLEN,
            INIT_FILE     => PROGRAM_FILE
        )
        port map (
            clock       => clock_processor,
            address     => std_logic_vector(address_program),
            destination => data_program
        );

    RAM : entity WORK.GENERIC_RAM
        generic map (
            DATA_WIDTH    => WORK.RV32I.XLEN,
            ADDRESS_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            clock        => clock_processor,
            enable       => '1',
            enable_read  => enable_memory_read,
            enable_write => enable_memory_write,
            address      => address_memory,
            source       => data_memory_out,
            destination  => data_memory_in
        );

    CPU : entity WORK.CPU_TOP_LEVEL(RV32I)
	     generic map (
            QUARTUS_MEMORY => QUARTUS_MEMORY
        )
        port map (
            clock           => clock_processor,
            clear           => '0',
            enable          => '1',
            memory_read     => enable_memory_read,
            memory_write    => enable_memory_write,
            data_program    => data_program,
            data_memory_in  => data_memory_in,
            data_memory_out => data_memory_out,
            address_program => address_program,
            address_memory  => address_memory
        );

    UPDATE_LED : entity WORK.GENERIC_REGISTER
        generic map (
            DATA_WIDTH    => 1
        )
        port map (
            clock        => clock_processor,
            clear        => '0',
            enable       => enable_memory_write AND WORK.GENERICS.is_equal_dynamic(address_memory, 32X"0080"),
            source       => data_memory_out(0 downto  0),
            destination  => LEDR(0 downto 0)
        );

    CLOCK_DEMONSTRATION : if DEMONSTRATION = TRUE generate
        low_freq : entity WORK.GENERIC_LOW_FREQ
            generic map (n => 100000000)
            port map (
                clock => CLOCK,
                clock_out => clock_processor
            );
            --LEDR(9) <= clock_processor;
            else generate
               clock_processor <= CLOCK;
           end generate;

end architecture;
