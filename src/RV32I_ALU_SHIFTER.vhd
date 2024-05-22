library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity RV32I_ALU_SHIFTER is

    generic (
        DATA_WIDTH  : natural := WORK.RV32I.XLEN;
        SHAMT_WIDTH : natural := 5
    );

    port (
        select_function : in  std_logic_vector(3 downto 0);
        shamt           : in  std_logic_vector((SHAMT_WIDTH - 1) downto 0);
        source          : in  std_logic_vector((DATA_WIDTH  - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH  - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_SHIFTER is

    signal data                 : t_std_logic_array(0 to (DATA_WIDTH - 1))((DATA_WIDTH - 1) downto 0);
    signal msb_vector           : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal source_auxiliar      : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal reversed_source      : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal destination_auxiliar : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal reversed_destination : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    reversed_source <= reverse_vector(source);

    reversed_destination <= reverse_vector(destination_auxiliar);

    BUILD : for i in 0 to (DATA_WIDTH - 1) generate
        BUILD_ROW : if (i = 0) generate
            data(i) <= source_auxiliar;
        elsif (i = DATA_WIDTH - 1) generate
            data(i) <= msb_vector;
        else generate
            data(i) <= source_auxiliar((DATA_WIDTH - i - 1) downto 0) & msb_vector((i - 1) downto 0);
        end generate;
    end generate;

    MUX_MSB_VECTOR: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => select_function(3),
            source_1    => (others => '0'),
            source_2    => (others => source(DATA_WIDTH - 1)),
            destination => msb_vector
        );

    MUX_source_auxiliar: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => select_function(2),
            source_1    => source,
            source_2    => reversed_source,
            destination => source_auxiliar
        );

    MUX_DATA : entity WORK.GENERIC_MUX_32X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => shamt,
            source_1    => data(0),
            source_2    => data(1),
            source_3    => data(2),
            source_4    => data(3),
            source_5    => data(4),
            source_6    => data(5),
            source_7    => data(6),
            source_8    => data(7),
            source_9    => data(8),
            source_10   => data(9),
            source_11   => data(10),
            source_12   => data(11),
            source_13   => data(12),
            source_14   => data(13),
            source_15   => data(14),
            source_16   => data(15),
            source_17   => data(16),
            source_18   => data(17),
            source_19   => data(18),
            source_20   => data(19),
            source_21   => data(20),
            source_22   => data(21),
            source_23   => data(22),
            source_24   => data(23),
            source_25   => data(24),
            source_26   => data(25),
            source_27   => data(26),
            source_28   => data(27),
            source_29   => data(28),
            source_30   => data(29),
            source_31   => data(30),
            source_32   => data(31),
            destination => destination_auxiliar
        );

    MUX_DESTINATION: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => select_function(2),
            source_1    => destination_auxiliar,
            source_2    => reversed_destination,
            destination => destination
        );

end architecture;
