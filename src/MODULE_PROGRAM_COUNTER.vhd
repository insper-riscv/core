library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_PROGRAM_COUNTER is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );

    port (
        clock        : in  std_ulogic;
        clear        : in  std_ulogic;
        enable       : in  std_ulogic;
        selector     : in  std_ulogic;
        source       : in  std_ulogic_vector((DATA_WIDTH - 1) downto 0);
        destination  : out std_ulogic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_PROGRAM_COUNTER is

    signal count_source    : WORK.RV32I.t_DATA;
    signal count_current   : WORK.RV32I.t_DATA;
    signal count_increment : WORK.RV32I.t_DATA;

begin

    destination <= count_current;

    MUX_SOURCE : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            selector    => selector,
            source_1    => count_increment,
            source_2    => source,
            destination => count_source
        );

    COUNT_REGISTER : entity WORK.GENERIC_REGISTER
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            clock       => clock,
            clear       => clear,
            enable      => enable,
            source      => count_source,
            destination => count_current
        );

    COUNT_ADDER : entity WORK.GENERIC_ADDER
        generic map (
            DATA_WIDTH       => WORK.RV32I.XLEN,
            DEFAULT_SOURCE_2 => 4
        )
        port map (
            source_1    => count_current,
            destination => count_increment
        );

end architecture;
