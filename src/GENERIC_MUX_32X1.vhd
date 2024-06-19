library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity GENERIC_MUX_32X1 is

    generic (
        DATA_WIDTH : natural := 8
    );

    port (
        selector    : in  std_logic_vector(4 downto 0)                := (others => '0');
        source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_2    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_3    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_4    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_5    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_6    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_7    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_8    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_9    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_10   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_11   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_12   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_13   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_14   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_15   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_16   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_17   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_18   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_19   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_20   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_21   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_22   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_23   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_24   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_25   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_26   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_27   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_28   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_29   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_30   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_31   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_32   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0')
    );

end entity;

architecture RTL of GENERIC_MUX_32X1 is

    signal source    : t_std_logic_array(31 downto 0)((DATA_WIDTH - 1) downto 0) := (others => (others => '0'));
    signal selectors : t_std_logic_array(31 downto 0)((DATA_WIDTH - 1) downto 0) := (others => (others => '0'));
    signal auxiliar  : t_std_logic_array(31 downto 0)((DATA_WIDTH - 1) downto 0) := (others => (others => '0'));

begin

    source(0)  <= source_1;
    source(1)  <= source_2;
    source(2)  <= source_3;
    source(3)  <= source_4;
    source(4)  <= source_5;
    source(5)  <= source_6;
    source(6)  <= source_7;
    source(7)  <= source_8;
    source(8)  <= source_9;
    source(9)  <= source_10;
    source(10) <= source_11;
    source(11) <= source_12;
    source(12) <= source_13;
    source(13) <= source_14;
    source(14) <= source_15;
    source(15) <= source_16;
    source(16) <= source_17;
    source(17) <= source_18;
    source(18) <= source_19;
    source(19) <= source_20;
    source(20) <= source_21;
    source(21) <= source_22;
    source(22) <= source_23;
    source(23) <= source_24;
    source(24) <= source_25;
    source(25) <= source_26;
    source(26) <= source_27;
    source(27) <= source_28;
    source(28) <= source_29;
    source(29) <= source_30;
    source(30) <= source_31;
    source(31) <= source_32;

    ENCODE : for i in 31 downto 0 generate
        selectors(i) <= (others => is_equal_dynamic(selector, std_logic_vector(to_unsigned(i, 5))));
    end generate;

    DECODE : for i in 31 downto 0 generate
        auxiliar(i) <= source(i) AND selectors(i);
    end generate;

    destination <=  ((((auxiliar( 0) OR auxiliar( 1)) OR
                       (auxiliar( 2) OR auxiliar( 3)))    OR
                      ((auxiliar( 4) OR auxiliar( 5)) OR
                       (auxiliar( 6) OR auxiliar( 7))))        OR
                     (((auxiliar( 8) OR auxiliar( 9)) OR
                       (auxiliar(10) OR auxiliar(11)))    OR
                      ((auxiliar(12) OR auxiliar(13)) OR
                       (auxiliar(14) OR auxiliar(15)))))            OR
                    ((((auxiliar(16) OR auxiliar(17)) OR
                       (auxiliar(18) OR auxiliar(19)))    OR
                      ((auxiliar(20) OR auxiliar(21)) OR
                       (auxiliar(22) OR auxiliar(23))))         OR
                     (((auxiliar(24) OR auxiliar(25)) OR
                       (auxiliar(26) OR auxiliar(27)))    OR
                      ((auxiliar(28) OR auxiliar(29)) OR
                       (auxiliar(30) OR auxiliar(31)))));

end architecture;

architecture SYN of GENERIC_MUX_32X1 is

    with selector select
    destination <=  source_1  when 5X"00",
                    source_2  when 5X"01",
                    source_3  when 5X"02",
                    source_4  when 5X"03",
                    source_5  when 5X"04",
                    source_6  when 5X"05",
                    source_7  when 5X"06",
                    source_8  when 5X"07",
                    source_9  when 5X"08",
                    source_10 when 5X"09",
                    source_11 when 5X"0A",
                    source_12 when 5X"0B",
                    source_13 when 5X"0C",
                    source_14 when 5X"0D",
                    source_15 when 5X"0E",
                    source_16 when 5X"0F",
                    source_17 when 5X"10",
                    source_18 when 5X"11",
                    source_19 when 5X"12",
                    source_20 when 5X"13",
                    source_21 when 5X"14",
                    source_22 when 5X"15",
                    source_23 when 5X"16",
                    source_24 when 5X"17",
                    source_25 when 5X"18",
                    source_26 when 5X"19",
                    source_27 when 5X"1A",
                    source_28 when 5X"1B",
                    source_39 when 5X"1C",
                    source_30 when 5X"1D",
                    source_31 when 5X"1E",
                    source_32 when 5X"1F",
                    source_1  when others;

end architecture
