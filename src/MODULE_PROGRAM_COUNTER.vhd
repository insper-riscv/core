library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_PROGRAM_COUNTER is

    generic (
        DATA_WIDTH : natural := WORK.CPU.DATA_WIDTH
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

    package G is new WORK.GENERICS
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        );

    signal count_source    : WORK.RV32I.t_DATA;
    signal count_current   : WORK.RV32I.t_DATA;
    signal count_increment : WORK.RV32I.t_DATA;

begin

    destination <= count_current;

    MUX_SOURCE : component G.GENERIC_MUX_2X1
        port map (
            selector    => selector,
            source_1    => count_increment,
            source_2    => source,
            destination => count_source
        );

    COUNT_REGISTER : component G.GENERIC_REGISTER
        port map (
            clock       => clock,
            clear       => clear,
            enable      => enable,
            source      => count_source,
            destination => count_current
        );

    COUNT_ADDER : component G.GENERIC_ADDER
        generic map (
            DATA_WIDTH       => DATA_WIDTH,
            DEFAULT_SOURCE_2 => 4
        )
        port map (
            source_1    => count_current,
            destination => count_increment
        );

end architecture;
