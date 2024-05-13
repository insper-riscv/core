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

    signal source    : WORK.GENERICS.t_std_logic_array(0 to 31)((DATA_WIDTH - 1) downto 0);
    signal selectors : WORK.GENERICS.t_std_logic_array(0 to 31)((DATA_WIDTH - 1) downto 0);
    signal auxiliar  : WORK.GENERICS.t_std_logic_array(0 to 31)((DATA_WIDTH - 1) downto 0);

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

    ENCODE : for i in 0 to 31 generate
        selectors(i) <= (others => is_equal(selector, std_logic_vector(to_unsigned(i, 5))));
    end generate;

    DECODE : for i in 0 to 31 generate
        auxiliar(i) <= source(i) AND selectors(i);
    end generate;

    REDUCE : process(selector, source)
        variable result : std_logic_vector((DATA_WIDTH - 1) downto 0);
    begin
        for i in 0 to 31 loop
            result := result OR auxiliar(i);
        end loop;

        destination <= result;
    end process;

end architecture;
