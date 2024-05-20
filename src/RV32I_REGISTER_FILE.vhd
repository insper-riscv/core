library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity RV32I_REGISTER_FILE is

    generic (
        DATA_WIDTH    : natural := WORK.RV32I.XLEN;
        ADDRESS_WIDTH : natural := WORK.RV32I.REGISTER_WIDTH
    );

    port (
        clock               : in  std_logic;
        clear               : in  std_logic;
        enable              : in  std_logic := '0';
        address_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_1    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        address_source_2    : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
        data_destination    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_1       : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_2       : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_REGISTER_FILE is

    signal registers       : t_std_logic_array(1 to (2**ADDRESS_WIDTH - 1))((DATA_WIDTH - 1) downto 0);
    signal decode_source_1 : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal decode_source_2 : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal passthrough_1   : std_logic;
    signal passthrough_2   : std_logic;

begin

    process(address_source_1, address_source_2, address_destination)
    begin
        passthrough_1 <= is_equal_dynamic(address_source_1, address_destination) AND reduce_or(address_destination);
        passthrough_2 <= is_equal_dynamic(address_source_2, address_destination) AND reduce_or(address_destination);
    end process;

    GEN_REGISTERS : for i in registers'range generate
        REGISTER_I : entity WORK.GENERIC_REGISTER
            generic map (
                DATA_WIDTH => DATA_WIDTH
            )
            port map (
                clock       => clock,
                clear       => clear,
                enable      => enable AND is_equal(address_destination, std_logic_vector(to_unsigned(i, 5))),
                source      => data_destination,
                destination => registers(i)
            );
    end generate;

    MUX_DECODE_SOURCE_1 : entity WORK.GENERIC_MUX_32X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => address_source_1,
            source_1    => (others => '0'),
            source_2    => registers(1),
            source_3    => registers(2),
            source_4    => registers(3),
            source_5    => registers(4),
            source_6    => registers(5),
            source_7    => registers(6),
            source_8    => registers(7),
            source_9    => registers(8),
            source_10   => registers(9),
            source_11   => registers(10),
            source_12   => registers(11),
            source_13   => registers(12),
            source_14   => registers(13),
            source_15   => registers(14),
            source_16   => registers(15),
            source_17   => registers(16),
            source_18   => registers(17),
            source_19   => registers(18),
            source_20   => registers(19),
            source_21   => registers(20),
            source_22   => registers(21),
            source_23   => registers(22),
            source_24   => registers(23),
            source_25   => registers(24),
            source_26   => registers(25),
            source_27   => registers(26),
            source_28   => registers(27),
            source_29   => registers(28),
            source_30   => registers(29),
            source_31   => registers(30),
            source_32   => registers(31),
            destination => decode_source_1
        );

    MUX_DECODE_SOURCE_2 : entity WORK.GENERIC_MUX_32X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => address_source_2,
            source_1    => (others => '0'),
            source_2    => registers(1),
            source_3    => registers(2),
            source_4    => registers(3),
            source_5    => registers(4),
            source_6    => registers(5),
            source_7    => registers(6),
            source_8    => registers(7),
            source_9    => registers(8),
            source_10   => registers(9),
            source_11   => registers(10),
            source_12   => registers(11),
            source_13   => registers(12),
            source_14   => registers(13),
            source_15   => registers(14),
            source_16   => registers(15),
            source_17   => registers(16),
            source_18   => registers(17),
            source_19   => registers(18),
            source_20   => registers(19),
            source_21   => registers(20),
            source_22   => registers(21),
            source_23   => registers(22),
            source_24   => registers(23),
            source_25   => registers(24),
            source_26   => registers(25),
            source_27   => registers(26),
            source_28   => registers(27),
            source_29   => registers(28),
            source_30   => registers(29),
            source_31   => registers(30),
            source_32   => registers(31),
            destination => decode_source_2
        );

    MUX_SOURCE_1 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => passthrough_1,
            source_1    => decode_source_1,
            source_2    => data_destination,
            destination => data_source_1
        );

    MUX_SOURCE_2 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            selector    => passthrough_2,
            source_1    => decode_source_2,
            source_2    => data_destination,
            destination => data_source_2
        );

end architecture;
