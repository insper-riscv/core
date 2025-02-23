library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

--! Atribui saída conforme entrada selecionada dentre trinda e duas
entity GENERIC_MUX_32X1 is
    
    generic (
        --! Largura dos vetores de dados
        DATA_WIDTH : natural := 8
    );
        
    port (
        --! Seletor dos vetores de dados
        selector    : in  std_logic_vector(4 downto 0)                := (others => '0');
        --! Vetor de dados 1
        source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 2
        source_2    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 3
        source_3    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 4
        source_4    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 5
        source_5    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 6
        source_6    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 7
        source_7    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 8
        source_8    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 9
        source_9    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 10
        source_10   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 11
        source_11   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 12
        source_12   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 13
        source_13   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 14
        source_14   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 15
        source_15   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 16
        source_16   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 17
        source_17   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 18
        source_18   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 19
        source_19   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 20
        source_20   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 21
        source_21   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 22
        source_22   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 23
        source_23   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 24
        source_24   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 25
        source_25   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 26
        source_26   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 27
        source_27   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 28
        source_28   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 29
        source_29   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 30
        source_30   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 31
        source_31   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados 32
        source_32   : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        --! Vetor de dados selecionado
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
