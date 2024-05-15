library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

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

    destination <= reduce_or(cases);

    MUX_CASE_BEQ: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => is_equal(select_function, WORK.RV32I.FUNCT3_BEQ),
            source_1    => "0",
            source_2    => (0 => flag_equal),
            destination => cases(0 downto 0)
        );

    MUX_CASE_BNE: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => is_equal(select_function, WORK.RV32I.FUNCT3_BNE),
            source_1    => "0",
            source_2    => (0 => NOT(flag_equal)),
            destination => cases(1 downto 1)
        );

    MUX_CASE_BLT: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => is_equal(select_function, WORK.RV32I.FUNCT3_BLT),
            source_1    => "0",
            source_2    => (0 => flag_less_signed),
            destination => cases(2 downto 2)
        );

    MUX_CASE_BGE: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => is_equal(select_function, WORK.RV32I.FUNCT3_BGE),
            source_1    => "0",
            source_2    => (0 => NOT(flag_less_signed)),
            destination => cases(3 downto 3)
        );

    MUX_CASE_BLTU: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => is_equal(select_function, WORK.RV32I.FUNCT3_BLTU),
            source_1    => "0",
            source_2    => (0 => flag_less),
            destination => cases(4 downto 4)
        );

    MUX_CASE_BGEU: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => is_equal(select_function, WORK.RV32I.FUNCT3_BGEU),
            source_1    => "0",
            source_2    => (0 => NOT(flag_less)),
            destination => cases(5 downto 5)
        );

end architecture;
