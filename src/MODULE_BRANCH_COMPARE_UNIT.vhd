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
        enable             : in  std_ulogic;
        select_function    : in  std_ulogic_vector((FUNCTION_WIDTH - 1) downto 0);
        source_1           : in  std_ulogic_vector((DATA_WIDTH - 1) downto 0);
        source_2           : in  std_ulogic_vector((DATA_WIDTH - 1) downto 0);
        forward            : in  WORK.CPU.t_FORWARD_BRANCH;
        destination        : out std_ulogic
    );

end entity;

architecture RV32I of MODULE_BRANCH_COMPARE_UNIT is

    alias sign_1 : std_ulogic is source_1(WORK.RV32I.XLEN - 1);
    alias sign_2 : std_ulogic is source_2(WORK.RV32I.XLEN - 1);

    signal flag_branch   : std_ulogic;
    signal flag_equal    : std_ulogic;
    signal flag_less     : std_ulogic;
    signal flag_greather : std_ulogic;

    signal forward_source_1 : std_ulogic_vector((DATA_WIDTH - 1) downto 0);
    signal forward_source_2 : std_ulogic_vector((DATA_WIDTH - 1) downto 0);

begin

    destination <= enable AND flag_branch;

    MUX_FORWARD_SOURCE_1 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            selector    => forward.select_source_1,
            source_1    => source_1,
            source_2    => forward.source_mem,
            destination => forward_source_1
        );

    MUX_FORWARD_SOURCE_2 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            selector    => forward.select_source_2,
            source_1    => source_2,
            source_2    => forward.source_mem,
            destination => forward_source_2
        );

    COMPARATOR : entity WORK.GENERIC_COMPARATOR
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            source_1      => forward_source_1,
            source_2      => forward_source_2,
            flag_equal    => flag_equal,
            flag_less     => flag_less,
            flag_greather => flag_greather
        );

    CONTROLLER: entity WORK.RV32I_BRANCH_CONTROLLER
        port map (
            select_function => select_function(2 downto 0),
            flag_sign_1     => sign_1,
            flag_sign_2     => sign_2,
            flag_equal      => flag_equal,
            flag_less       => flag_less,
            flag_greather   => flag_greather,
            destination     => flag_branch
        );

end architecture;
