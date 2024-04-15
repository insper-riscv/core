library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package RV32M is

    -- RV32M Standard Extension Set functions
    constant FUNCT3_MUL    : t_FUNCT3 := 3X"0";
    constant FUNCT3_MULH   : t_FUNCT3 := 3X"1";
    constant FUNCT3_MULHSU : t_FUNCT3 := 3X"2";
    constant FUNCT3_MULHU  : t_FUNCT3 := 3X"3";
    constant FUNCT3_DIV    : t_FUNCT3 := 3X"4";
    constant FUNCT3_DIVU   : t_FUNCT3 := 3X"5";
    constant FUNCT3_REM    : t_FUNCT3 := 3X"6";
    constant FUNCT3_REMU   : t_FUNCT3 := 3X"7";

    constant FUNCT7_MUL    : t_FUNCT7 := 7X"01";
    constant FUNCT7_MULH   : t_FUNCT7 := 7X"01";
    constant FUNCT7_MULHSU : t_FUNCT7 := 7X"01";
    constant FUNCT7_MULHU  : t_FUNCT7 := 7X"01";
    constant FUNCT7_DIV    : t_FUNCT7 := 7X"01";
    constant FUNCT7_DIVU   : t_FUNCT7 := 7X"01";
    constant FUNCT7_REM    : t_FUNCT7 := 7X"01";
    constant FUNCT7_REMU   : t_FUNCT7 := 7X"01";

end package;
