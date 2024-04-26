library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_BRANCH_CONTROLLER is

    port (
        enable          : in  std_logic;
        select_function : in  WORK.RV32I.t_FUNCT3;
        flag_sign_1     : in  std_logic;
        flag_sign_2     : in  std_logic;
        flag_equal      : in  std_logic;
        flag_less       : in  std_logic;
        flag_greather   : in  std_logic;
        destination     : out std_logic
    );

end entity;

architecture RV32I of RV32I_BRANCH_CONTROLLER is

    --No signals

begin

    DECODE: process(select_function, flag_equal, flag_less, flag_greather, flag_sign_1, flag_sign_2, enable)
        variable tmp_destination : std_logic;
    begin
        case select_function is
            when WORK.RV32I.FUNCT3_BEQ =>
                tmp_destination := flag_equal;
            when WORK.RV32I.FUNCT3_BNE =>
                tmp_destination := NOT flag_equal;
            when WORK.RV32I.FUNCT3_BLT =>
                tmp_destination := (flag_less and not flag_sign_1) OR (flag_greather and flag_sign_1 and flag_sign_2);
            when WORK.RV32I.FUNCT3_BGE =>
                tmp_destination := NOT ((flag_less and not flag_sign_1) OR (flag_greather and flag_sign_1 and flag_sign_2));
            when WORK.RV32I.FUNCT3_BLTU =>
                tmp_destination := flag_less;
            when WORK.RV32I.FUNCT3_BGEU =>
                tmp_destination := flag_greather;
            when    others =>
                tmp_destination := '0';
        end case;
        destination <= tmp_destination AND enable;
    end process;

end architecture;
