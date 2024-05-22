library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity RV32I_TYPE_CONVERTER is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );
  
    port (
        select_type : in  std_ulogic_vector(2 downto 0);
        source      : in  std_ulogic_vector((DATA_WIDTH - 1) downto 0);
        destination : out std_ulogic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of RV32I_TYPE_CONVERTER is

    signal destination_byte     : WORK.RV32I.t_DATA;
    signal destination_halfword : WORK.RV32I.t_DATA;
    signal destination_auxiliar : WORK.RV32I.t_DATA;

begin

    EXTEND_BYTE: entity WORK.GENERIC_SIGNAL_EXTENDER
        generic map (
            SOURCE_WIDTH      => 8,
            DESTINATION_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            enable_unsigned => select_type(2),
            source          => source(7 downto 0),
            destination     => destination_byte
        );

    EXTEND_HALFWORD: entity WORK.GENERIC_SIGNAL_EXTENDER
        generic map (
            SOURCE_WIDTH      => 16,
            DESTINATION_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            enable_unsigned => select_type(2),
            source          => source(15 downto 0),
            destination     => destination_halfword
        );

    MUX_TYPE: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            selector    => select_type(0),
            source_1    => destination_byte,
            source_2    => destination_halfword,
            destination => destination_auxiliar
        );

    MUX_DESTINATION: entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        )
        port map (
            selector    => select_type(1),
            source_1    => destination_auxiliar,
            source_2    => source,
            destination => destination
        );

end architecture;
