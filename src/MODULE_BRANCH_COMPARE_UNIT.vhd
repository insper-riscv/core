library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_BRANCH_COMPARE_UNIT is

    port (
        source_1        : in  WORK.CPU.t_DATA;
        source_2        : in  WORK.CPU.t_DATA;
        select_function : in  WORK.CPU.t_FUNCTION;
        destination     : out std_logic
    );

end entity;

architecture RV32I of MODULE_BRANCH_COMPARE_UNIT is

    package G is new WORK.GENERICS
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        );

    alias  sign_1 : std_logic is source_1(WORK.RV32I.XLEN - 1);
    alias  sign_2 : std_logic is source_2(WORK.RV32I.XLEN - 1);

    signal flag_equal    : std_logic;
    signal flag_less     : std_logic;
    signal flag_greather : std_logic;

begin

    COMPARE: process (select_function)
    begin
        case select_function(2 downto 0) is
            when
                    WORK.RV32I.FUNCT3_BEQ |
                    WORK.RV32I.FUNCT3_BNE =>
                destination <= flag_equal;
            when
                    WORK.RV32I.FUNCT3_BLT |
                    WORK.RV32I.FUNCT3_BGE =>
                destination <= (flag_less and not sign_1) OR (flag_greather and sign_1 and sign_2);
            when
                    WORK.RV32I.FUNCT3_BLTU |
                    WORK.RV32I.FUNCT3_BGEU =>
                destination <= flag_less;
            when
                    others =>
                destination <= '0';
        end case;
    end process;

    COMPARATOR : component G.GENERIC_COMPARATOR
        port map (
            source_1      => source_1,
            source_2      => source_2,
            flag_equal    => flag_equal,
            flag_less     => flag_less,
            flag_greather => flag_greather
        );

end architecture;
