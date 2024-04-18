library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_STAGE_IF is

    port (
        clock           : in  std_logic;
        clear           : in  std_logic;
        enable          : in  std_logic;
        source          : in  WORK.CPU.t_CONTROL_IF;
        address_jump    : in  WORK.CPU.t_DATA;
        address_program : out WORK.CPU.t_DATA
    );

end entity;

architecture RV32I of CPU_STAGE_IF is

    signal enable_0 : std_logic;
    signal jump     : std_logic;

begin

    jump <= source.select_source XOR source.enable_jump;

    process(source.enable_stall) is
    begin
        enable_0 <= enable AND NOT source.enable_stall;
    end process;

    MODULE_PROGRAM_COUNTER : entity WORK.MODULE_PROGRAM_COUNTER(RV32I)
        port map (
            clock        => clock,
            clear        => clear,
            enable       => enable_0,
            selector     => source.select_source,
            source       => address_jump,
            destination  => address_program
        );

end architecture;
