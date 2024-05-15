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
        selector    : in  std_logic_vector(4 downto 0);
        source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_3    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_4    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_5    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_6    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_7    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_8    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_9    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_10   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_11   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_12   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_13   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_14   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_15   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_16   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_17   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_18   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_19   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_20   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_21   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_22   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_23   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_24   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_25   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_26   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_27   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_28   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_29   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_30   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_31   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_32   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_32X1 is

    signal source    : WORK.GENERICS.t_std_logic_array(31 downto 0)((DATA_WIDTH - 1) downto 0) := (others => (others => '0'));
    signal selectors : WORK.GENERICS.t_std_logic_array(31 downto 0)((DATA_WIDTH - 1) downto 0) := (others => (others => '0'));
    signal auxiliar  : WORK.GENERICS.t_std_logic_array(31 downto 0)((DATA_WIDTH - 1) downto 0) := (others => (others => '0'));

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

    -- ENCODE : for i in 31 downto 0 generate
    --     selectors(i) <= (others => is_equal(selector, std_logic_vector(to_unsigned(i, 5))));
    -- end generate;

    selectors( 0) <= (others => is_equal(selector, 5X"00"));
    selectors( 1) <= (others => is_equal(selector, 5X"01"));
    selectors( 2) <= (others => is_equal(selector, 5X"02"));
    selectors( 3) <= (others => is_equal(selector, 5X"03"));
    selectors( 4) <= (others => is_equal(selector, 5X"04"));
    selectors( 5) <= (others => is_equal(selector, 5X"05"));
    selectors( 6) <= (others => is_equal(selector, 5X"06"));
    selectors( 7) <= (others => is_equal(selector, 5X"07"));
    selectors( 8) <= (others => is_equal(selector, 5X"08"));
    selectors( 9) <= (others => is_equal(selector, 5X"09"));
    selectors(10) <= (others => is_equal(selector, 5X"0a"));
    selectors(11) <= (others => is_equal(selector, 5X"0b"));
    selectors(12) <= (others => is_equal(selector, 5X"0c"));
    selectors(13) <= (others => is_equal(selector, 5X"0d"));
    selectors(14) <= (others => is_equal(selector, 5X"0e"));
    selectors(15) <= (others => is_equal(selector, 5X"0f"));
    selectors(16) <= (others => is_equal(selector, 5X"10"));
    selectors(17) <= (others => is_equal(selector, 5X"11"));
    selectors(18) <= (others => is_equal(selector, 5X"12"));
    selectors(19) <= (others => is_equal(selector, 5X"13"));
    selectors(20) <= (others => is_equal(selector, 5X"14"));
    selectors(21) <= (others => is_equal(selector, 5X"15"));
    selectors(22) <= (others => is_equal(selector, 5X"16"));
    selectors(23) <= (others => is_equal(selector, 5X"17"));
    selectors(24) <= (others => is_equal(selector, 5X"18"));
    selectors(25) <= (others => is_equal(selector, 5X"19"));
    selectors(26) <= (others => is_equal(selector, 5X"1a"));
    selectors(27) <= (others => is_equal(selector, 5X"1b"));
    selectors(28) <= (others => is_equal(selector, 5X"1c"));
    selectors(29) <= (others => is_equal(selector, 5X"1d"));
    selectors(30) <= (others => is_equal(selector, 5X"1e"));
    selectors(31) <= (others => is_equal(selector, 5X"1f"));

    -- DECODE : for i in 31 downto 0 generate
    --     auxiliar(i) <= source(i) AND selectors(i);
    -- end generate;

    auxiliar( 0) <= source( 0) AND selectors( 0);
    auxiliar( 1) <= source( 1) AND selectors( 1);
    auxiliar( 2) <= source( 2) AND selectors( 2);
    auxiliar( 3) <= source( 3) AND selectors( 3);
    auxiliar( 4) <= source( 4) AND selectors( 4);
    auxiliar( 5) <= source( 5) AND selectors( 5);
    auxiliar( 6) <= source( 6) AND selectors( 6);
    auxiliar( 7) <= source( 7) AND selectors( 7);
    auxiliar( 8) <= source( 8) AND selectors( 8);
    auxiliar( 9) <= source( 9) AND selectors( 9);
    auxiliar(10) <= source(10) AND selectors(10);
    auxiliar(11) <= source(11) AND selectors(11);
    auxiliar(12) <= source(12) AND selectors(12);
    auxiliar(13) <= source(13) AND selectors(13);
    auxiliar(14) <= source(14) AND selectors(14);
    auxiliar(15) <= source(15) AND selectors(15);
    auxiliar(16) <= source(16) AND selectors(16);
    auxiliar(17) <= source(17) AND selectors(17);
    auxiliar(18) <= source(18) AND selectors(18);
    auxiliar(19) <= source(19) AND selectors(19);
    auxiliar(20) <= source(20) AND selectors(20);
    auxiliar(21) <= source(21) AND selectors(21);
    auxiliar(22) <= source(22) AND selectors(22);
    auxiliar(23) <= source(23) AND selectors(23);
    auxiliar(24) <= source(24) AND selectors(24);
    auxiliar(25) <= source(25) AND selectors(25);
    auxiliar(26) <= source(26) AND selectors(26);
    auxiliar(27) <= source(27) AND selectors(27);
    auxiliar(28) <= source(28) AND selectors(28);
    auxiliar(29) <= source(29) AND selectors(29);
    auxiliar(30) <= source(30) AND selectors(30);
    auxiliar(31) <= source(31) AND selectors(31);

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

    -- REDUCE : process(selector, source_1, source_2, source_3, source_4, source_5, source_6, source_7, source_8, source_9, source_10, source_11, source_12, source_13, source_14, source_15, source_16, source_17, source_18, source_19, source_20, source_21, source_22, source_23, source_24, source_25, source_26, source_27, source_28, source_29, source_30, source_31, source_32, source, selectors, auxiliar)
    --     variable result : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
    -- begin
    --     for i in 31 downto 0 loop
    --         result := result OR auxiliar(i);
    --     end loop;

    --     destination <= result;
    -- end process;

end architecture;
