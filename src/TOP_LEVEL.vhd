library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity TOP_LEVEL is

    port (
        CLOCK : in  std_logic                    := '0';
        SW    : in  std_logic_vector(3 downto 0) := (others => '0');
        LED   : out std_logic_vector(7 downto 0) := (others => '0')
    );

end entity;

architecture RTL of TOP_LEVEL is

    signal data_program        : std_logic_vector(RV32I.INSTRUCTION_RANGE);
    signal data_memory_in      : CPU.t_DATA;
    signal data_memory_out     : CPU.t_DATA;
    signal enable_memory_read  : std_logic;
    signal enable_memory_write : std_logic;
    signal address_program     : CPU.t_DATA;
    signal address_memory      : t_DATA;

begin

    LED(0) <= SW(1);
    LED(7 downto 1) <= (others => '0');

    ROM : entity WORK.GENERIC_ROM
        port map (
            address     => address_program,
            destination => data_program
        );

    RAM : entity WORK.GENERIC_RAM
        port map (
            clock        => CLOCK,
            enable       => '1',      
            enable_read  => enable_memory_read,
            enable_write => enable_memory_write,
            address      => address_memory,
            source       => data_memory_out,
            destination  => data_memory_in 
        );

    CPU : entity WORK.CPU_TOP_LEVEL(RV32I)
        port map (
            clock           => CLOCK,
            clear           => '0',
            enable          => '1',
            data_program    => data_program,
            data_memory_in  => data_memory_in,
            memory_read     => enable_memory_read,
            memory_write    => enable_memory_write,
            data_memory_out => data_memory_out,
            address_program => address_program,
            address_memory  => address_memory
        );

end architecture;
