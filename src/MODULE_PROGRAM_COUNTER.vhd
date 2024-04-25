library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_PROGRAM_COUNTER is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );

    port (
        clock        : in  std_logic;
        clear        : in  std_logic;
        enable       : in  std_logic;
        selector     : in  std_logic;
        source       : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
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
            source_1    => source,
            source_2    => count_increment,
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
