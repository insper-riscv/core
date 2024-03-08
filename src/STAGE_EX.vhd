library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_EX is
  
    port (
        source : in t_ID_EX_SIGNALS;
        destination : out t_EX_MEM_SIGNALS
    );

end entity;

architecture RTL of STAGE_EX is

    -- No signals

begin

    MODULE_ALU : entity WORK.MODULE_ALU
        port map (
            select_source_1        => source.ex_signals.select_source_1,
            select_source_2        => source.ex_signals.select_source_2,
            source_pc              => source.pc,
            source_register_1      => source.source_1,
            source_register_2      => source.source_2,
            source_immediate       => source.immediate,
            opcode                 => source.opcode,
            function_3             => source.funct_3,
            function_7             => source.funct_7,
            source_register_2_out  => destination.source_2,
            destination            => destination.pointer
        );

    destination.mem_signals <= source.mem_signals;
    destination.wb_signals <= source.wb_signals;
    destination.select_destination <= source.select_destination;

end architecture;
