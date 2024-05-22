library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_STAGE_IF is

    port (
        clock           : in  std_ulogic;
        clear           : in  std_ulogic;
        enable          : in  std_ulogic;
        source          : in  WORK.CPU.t_CONTROL_IF;
        address_jump    : in  WORK.CPU.t_DATA;
        address_program : out WORK.CPU.t_DATA
    );

end entity;

architecture RV32I of CPU_STAGE_IF is

    -- No signals

begin

    PROGRAM_COUNTER : entity WORK.MODULE_PROGRAM_COUNTER(RV32I)
        port map (
            clock        => clock,
            clear        => clear,
            enable       => enable, -- AND NOT(source.enable_stall),
            selector     => source.select_source,
            source       => address_jump,
            destination  => address_program
        );

end architecture;
