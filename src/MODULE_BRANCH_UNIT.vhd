library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity MODULE_BRANCH_UNIT is

    port (
        source_program   : in  WORK.CPU.t_DATA;
        source_immediate : in  WORK.CPU.t_DATA;
        source_register  : in  WORK.CPU.t_DATA;
        destination      : out WORK.CPU.t_DATA
    );

end entity;

architecture RV32I of MODULE_BRANCH_UNIT is

    package G is new G.GENERICS
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        );

    signal program_plus_immediate  : WORK.RV32I.t_DATA;
    signal register_plus_immediate : WORK.RV32I.t_DATA;

begin

    ADDER_1 : entity G.GENERIC_ADDER
        port map (
            source_1    => source_program,
            source_2    => source_immediate,
            destination => program_plus_immediate
        );

    ADDER_2 : entity G.GENERIC_ADDER
        port map (
            source_1    => source_immediate,
            source_2    => source_register,
            destination => register_plus_immediate
        );

    MUX_1 : entity G.GENERIC_MUX_2X1
        port map (
            source_1    => program_plus_immediate,
            source_2    => register_plus_immediate,
            selector    => control_id.select_jump,
            destination => destination
        );

end architecture;
