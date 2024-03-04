library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_IF is

    generic (
        DATA_WIDTH_0  : natural := DATA_WIDTH
    );

    port (
        id_source   : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        selector    : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_IF is
        signal adder_out : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        signal mux_out   : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        signal pc_out    : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
begin   
    
    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_2X1
        port map (
            source_1 => id_source,
            source_2 => adder_out,
            selector => selector,
            destination => mux_out
        );
    
    PC : entity WORK.GENERIC_REGISTER
        port map (
            clear => clear,
            enable => enable,
            source => source,
            destination => pc_out
        );

    ADDER : entity WORK.GENERIC_ADDER
        port map (
            source_1 => pc_out,
            source_2 => (others => '0') & "100",
            destination => adder_out
        );


end architecture;