library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_BRANCH_COMPARE_UNIT is

    generic (
        FUNCTION_WIDTH : natural := WORK.RV32I.FUNCT3_WIDTH + 1;
        DATA_WIDTH     : natural := WORK.RV32I.XLEN
    );

    port (
        enable          : in  std_logic;
        select_function : in  std_logic_vector((FUNCTION_WIDTH - 1) downto 0);
        source_1        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination     : out std_logic
    );

end entity;

architecture RV32I of MODULE_BRANCH_COMPARE_UNIT is

    alias sign_1 : std_logic is source_1(WORK.RV32I.XLEN - 1);
    alias sign_2 : std_logic is source_2(WORK.RV32I.XLEN - 1);

    signal flag_equal    : std_logic;
    signal flag_less     : std_logic;
    signal flag_greather : std_logic;

begin

    COMPARATOR : entity WORK.GENERIC_COMPARATOR
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            source_1      => source_1,
            source_2      => source_2,
            flag_equal    => flag_equal,
            flag_less     => flag_less,
            flag_greather => flag_greather
        );

    COMPARE: entity WORK.RV32I_BRANCH_CONTROLLER
        port map (
            enable          => enable,
            select_function => select_function(2 downto 0),
            flag_sign_1     => sign_1,
            flag_sign_2     => sign_2,
            flag_equal      => flag_equal,
            flag_less       => flag_less,
            flag_greather   => flag_greather,
            destination     => destination
        );

end architecture;
