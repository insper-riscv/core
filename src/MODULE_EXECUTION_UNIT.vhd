library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_EXECUTION_UNIT is

    generic (
        FUNCTION_WIDTH : natural := 4;
        DATA_WIDTH     : natural := WORK.RV32I.XLEN
    );

    port (
        select_forward_1 : in  std_logic_vector(1 downto 0);
        select_forward_2 : in  std_logic_vector(1 downto 0);
        select_source_1  : in  std_logic_vector(1 downto 0);
        select_source_2  : in  std_logic_vector(1 downto 0);
        select_function  : in  std_logic_vector((FUNCTION_WIDTH - 1) downto 0);
        address_program  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_mem       : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_wb        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_1         : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2         : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        immediate        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination      : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_EXECUTION_UNIT is

    package G is new WORK.GENERICS
            generic map (
                DATA_WIDTH => WORK.RV32I.XLEN
            );

    signal forward_source_1 : WORK.RV32I.t_DATA;
    signal forward_source_2 : WORK.RV32I.t_DATA;
    signal alu_source_1     : WORK.RV32I.t_DATA;
    signal alu_source_2     : WORK.RV32I.t_DATA;

begin

    MUX_FORWARD_SOURCE_1 : component G.GENERIC_MUX_4X1
        port map (
            selector    => select_forward_1,
            source_1    => source_1,
            source_2    => source_wb,
            source_3    => source_mem,
            source_4    => (others => '0'),
            destination => forward_source_1
        );

    MUX_FORWARD_SOURCE_2 : component G.GENERIC_MUX_4X1
        port map (
            selector    => select_forward_2,
            source_1    => source_2,
            source_2    => source_wb,
            source_3    => source_mem,
            source_4    => (others => '0'),
            destination => forward_source_2
        );

    MUX_ALU_SOURCE_1 : component G.GENERIC_MUX_4X1
        port map (
            selector    => select_source_1,
            source_1    => forward_source_1,
            source_2    => address_program,
            source_3    => std_logic_vector(to_unsigned(0, DATA_WIDTH)),
            source_4    => (others => '0'),
            destination => alu_source_1
        );

    MUX_ALU_SOURCE_2 : component G.GENERIC_MUX_4X1
        port map (
            selector    => select_source_2,
            source_1    => forward_source_2,
            source_2    => immediate,
            source_3    => std_logic_vector(to_unsigned(4, DATA_WIDTH)),
            source_4    => (others => '0'),
            destination => alu_source_2
        );

    ALU : entity WORK.RV32I_ALU
        port map (
            select_function => select_function,
            source_1        => alu_source_1,
            source_2        => alu_source_2,
            destination     => destination
        );

end architecture;
