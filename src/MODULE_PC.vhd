library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_PC is

    generic (
        DATA_WIDTH_0  : natural := DATA_WIDTH
    );

    port (
        clock       : in  std_logic;
        source_id   : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        selector    : in  std_logic;
        clear       : in  std_logic;
        enable      : in  std_logic;
        destination : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_PC is
        signal adder_out : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        signal mux_out   : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        signal pc_out    : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
begin   
    
    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_2X1
        port map (
            source_1 => source_id,
            source_2 => adder_out,
            selector => selector,
            destination => mux_out
        );
    
    PC : entity WORK.GENERIC_REGISTER
        port map (
            clock => clock,
            clear => clear,
            enable => enable,
            source => mux_out,
            destination => pc_out
        );

    ROM : entity WORK.GENERIC_ROM
        port map (
            address     => pc_out,
            destination => destination
        );

    ADDER : entity WORK.GENERIC_ADDER
        port map (
            source_1 => pc_out,
            source_2 => std_logic_vector(to_unsigned(4, 32)),
            destination => adder_out
        );


end architecture;