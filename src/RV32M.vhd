library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package RV32M is

    -- RV32M Standard Extension Set functions
    constant FUNCT3_MUL    : WORK.RV32I.t_FUNCT3 := 3X"0";
    constant FUNCT3_MULH   : WORK.RV32I.t_FUNCT3 := 3X"1";
    constant FUNCT3_MULHSU : WORK.RV32I.t_FUNCT3 := 3X"2";
    constant FUNCT3_MULHU  : WORK.RV32I.t_FUNCT3 := 3X"3";
    constant FUNCT3_DIV    : WORK.RV32I.t_FUNCT3 := 3X"4";
    constant FUNCT3_DIVU   : WORK.RV32I.t_FUNCT3 := 3X"5";
    constant FUNCT3_REM    : WORK.RV32I.t_FUNCT3 := 3X"6";
    constant FUNCT3_REMU   : WORK.RV32I.t_FUNCT3 := 3X"7";

    constant FUNCT7_MUL    : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_MULH   : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_MULHSU : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_MULHU  : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_DIV    : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_DIVU   : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_REM    : WORK.RV32I.t_FUNCT7 := 7X"01";
    constant FUNCT7_REMU   : WORK.RV32I.t_FUNCT7 := 7X"01";

end package;
