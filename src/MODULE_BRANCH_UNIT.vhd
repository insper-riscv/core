library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity MODULE_BRANCH_UNIT is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );

    port (
        selector         : in  std_logic;
        source_program   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_immediate : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_register  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination      : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_BRANCH_UNIT is

    signal program_plus_immediate  : WORK.RV32I.t_DATA;
    signal register_plus_immediate : WORK.RV32I.t_DATA;

begin

    ADDER_1 : entity WORK.GENERIC_ADDER
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            source_1    => source_program,
            source_2    => source_immediate,
            destination => program_plus_immediate
        );

    ADDER_2 : entity WORK.GENERIC_ADDER
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            source_1    => source_immediate,
            source_2    => source_register,
            destination => register_plus_immediate
        );

    MUX_1 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            source_1    => program_plus_immediate,
            source_2    => register_plus_immediate,
            selector    => selector,
            destination => destination
        );

end architecture;
