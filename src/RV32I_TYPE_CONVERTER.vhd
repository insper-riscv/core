library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity RV32I_TYPE_CONVERTER is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );
  
    port (
        select_type : in  std_logic_vector(2 downto 0);
        source      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of RV32I_TYPE_CONVERTER is

    signal enable_unsigned      : std_logic;
    signal destination_byte     : WORK.RV32I.t_DATA;
    signal destination_halfword : WORK.RV32I.t_DATA;

begin

    destination <=  destination_halfword when (select_type(0) = '1') else
                    destination_byte when (select_type(1) = '0') else
                    source;

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

end architecture;
