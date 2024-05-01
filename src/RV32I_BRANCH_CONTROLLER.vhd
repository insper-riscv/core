library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_BRANCH_CONTROLLER is

    port (
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

    signal flag_less_signed : std_logic;
    signal cases            : std_logic_vector(5 downto 0);

begin

    flag_less_signed <= (flag_less AND NOT(flag_sign_1)) OR (flag_greather AND flag_sign_1 AND flag_sign_2);

    cases(0) <= flag_equal           when (select_function = WORK.RV32I.FUNCT3_BEQ)  else '0';
    cases(1) <= NOT flag_equal       when (select_function = WORK.RV32I.FUNCT3_BNE)  else '0';
    cases(2) <= flag_less_signed     when (select_function = WORK.RV32I.FUNCT3_BLT)  else '0';
    cases(3) <= NOT flag_less_signed when (select_function = WORK.RV32I.FUNCT3_BGE)  else '0';
    cases(4) <= flag_less            when (select_function = WORK.RV32I.FUNCT3_BLTU) else '0';
    cases(5) <= NOT flag_less        when (select_function = WORK.RV32I.FUNCT3_BGEU) else '0';

    destination <= WORK.GENERICS.reduce_or(cases);

end architecture;
