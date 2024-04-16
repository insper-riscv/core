library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.MATH_REAL.ALL;

library WORK;

entity RV32I_ALU_SHIFTER is

    generic (
        DATA_WIDTH  : natural   := WORK.RV32I.XLEN;
        SHAMT_WIDTH : natural   := natural(ceil(log2(real(DATA_WIDTH))))
    );

    port (
        select_function : in  std_logic_vector(4 downto 0);
        shamt           : in  std_logic_vector((SHAMT_WIDTH - 1) downto 0);
        source          : in  std_logic_vector((DATA_WIDTH  - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH  - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_SHIFTER is

    constant HIGH_SELECTOR  : std_logic_vector((SHAMT_WIDTH - 1) downto 0)  := (others => '1');
    constant LOW_SELECTOR   : std_logic_vector((SHAMT_WIDTH - 1) downto 0)  := (others => '0');
    constant ONE_SELECTOR   : std_logic_vector((SHAMT_WIDTH - 1) downto 0)  := std_logic_vector(to_unsigned(1, SHAMT_WIDTH));
    constant LOW_VEC        : std_logic_vector((DATA_WIDTH  - 1) downto 0)  := (others => '0');

    signal index                    : natural;
    signal sign_vec                 : std_logic_vector((DATA_WIDTH  - 1) downto 0);
    signal shift_left_logical       : std_logic_vector((DATA_WIDTH  - 1) downto 0);
    signal shift_right_logical      : std_logic_vector((DATA_WIDTH  - 1) downto 0);
    signal shift_right_arithmetical : std_logic_vector((DATA_WIDTH  - 1) downto 0);

    signal aaa : std_logic_vector((DATA_WIDTH  - 1) downto 0);
    signal bbb : std_logic_vector((DATA_WIDTH  - 1) downto 0);
    signal ccc : std_logic_vector((DATA_WIDTH  - 1) downto 0);

begin

    index <=    to_integer(unsigned(shamt));

    sign_vec <= (others => source(DATA_WIDTH - 1));

    process(source, index)
    begin
        aaa <= source;
        LEFT_LOGICAL : for i in 2 to (DATA_WIDTH - 2) loop
            if i = index then
                exit;
            end if;
            aaa <= aaa(DATA_WIDTH - 2 downto 0) & '0';
        end loop;

        bbb <= source;
        RIGHT_LOGICAL : for i in 2 to (DATA_WIDTH - 2) loop
            if i = index then
                exit;
            end if;
            bbb <= '0' & bbb(DATA_WIDTH - 1 downto 1);
        end loop;

        ccc <= source;
        RIGHT_ARITHMETICAL : for i in 2 to (DATA_WIDTH - 2) loop
            if i = index then
                exit;
            end if;
            ccc <= source(DATA_WIDTH - 1) & ccc(DATA_WIDTH - 1 downto 1);
        end loop;
    end process;

    shift_left_logical <=   source when (shamt = LOW_SELECTOR) else
                            source(0) & LOW_VEC((DATA_WIDTH - 2) downto 0) when (shamt = HIGH_SELECTOR) else
                            source((DATA_WIDTH - 2) downto 0) & '0' when (shamt = ONE_SELECTOR) else
                            aaa;

    shift_right_logical <=  source when (shamt = LOW_SELECTOR) else
                            LOW_VEC((DATA_WIDTH - 1) downto 1) & source(DATA_WIDTH - 1) when (shamt = HIGH_SELECTOR) else
                            '0' & source((DATA_WIDTH - 1) downto 1) when (shamt = ONE_SELECTOR) else
                            bbb;

    shift_right_arithmetical <= source when (shamt = LOW_SELECTOR) else
                                sign_vec((DATA_WIDTH - 1) downto 1) & source(DATA_WIDTH - 1) when (shamt = HIGH_SELECTOR) else
                                sign_vec(0) & source((DATA_WIDTH - 1) downto 1) when (shamt = ONE_SELECTOR) else
                                ccc;

    destination <=  shift_left_logical       when (select_function(2 downto 0) = "100") else
                    shift_right_logical      when (select_function(2 downto 0) = "101") else
                    shift_right_arithmetical when (select_function(2 downto 0) = "110") else
                    source;

end architecture;
