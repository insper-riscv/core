library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.all;

--! Realiza operações aritmética de comparação entre dois inteiros positivos codificados em vetores booleanos
entity GENERIC_COMPARATOR is

    generic (
        --! Largura dos vetores de dados
        DATA_WIDTH : natural := 8
    );

    port (
        --! Vetor de dados primário
        source_1      : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados secundário
        source_2      : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Resultado da comparação `source_1 = source_2`
        flag_equal    : out std_logic;
        --! Resultado da comparação `source_1 < source_2`
        flag_less     : out std_logic;
        --! Resultado da comparação `source_1 > source_2`
        flag_greather : out std_logic
    );

end entity;

architecture RTL of GENERIC_COMPARATOR is

    signal a_and_not_b      : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal not_a_and_b      : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal a_xnor_b         : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal a_equal_b        : std_logic_vector((DATA_WIDTH - 2) downto 0);
    signal a_less_than_b    : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal a_greater_than_b : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    a_and_not_b <= source_1 AND NOT(source_2);
    not_a_and_b <= NOT(source_1) AND source_2;
    a_xnor_b <= a_and_not_b NOR not_a_and_b;

    a_equal_b(0) <= a_xnor_b(DATA_WIDTH - 1) AND a_xnor_b(DATA_WIDTH - 2);

    EQUALS: for i in 1 to (DATA_WIDTH - 2) generate
        a_equal_b(i) <= a_equal_b(i - 1) AND a_xnor_b(DATA_WIDTH - i - 2);
    end generate;

    a_less_than_b(0) <= not_a_and_b(DATA_WIDTH - 1);
    a_less_than_b(1) <= not_a_and_b(DATA_WIDTH - 2) AND a_xnor_b(DATA_WIDTH - 1);

    LESSES: for i in 2 to (DATA_WIDTH - 1) generate
        a_less_than_b(i) <= a_equal_b(i - 2) AND not_a_and_b(DATA_WIDTH - i - 1);
    end generate;

    a_greater_than_b(0) <= a_and_not_b(DATA_WIDTH - 1);
    a_greater_than_b(1) <= a_and_not_b(DATA_WIDTH - 2) AND a_xnor_b(DATA_WIDTH - 1);

    GREATERS: for i in 2 to (DATA_WIDTH - 1) generate
        a_greater_than_b(i) <= a_equal_b(i - 2) AND a_and_not_b(DATA_WIDTH - i - 1);
    end generate;

    flag_equal    <= a_equal_b(DATA_WIDTH - 2);
    flag_less     <= reduce_or(a_less_than_b);
    flag_greather <= reduce_or(a_greater_than_b);

end architecture;
