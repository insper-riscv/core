library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_MUX_4X1 is

    generic (
        DATA_WIDTH : natural := XLEN
    );

    port (
        source_1     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_2     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_3     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        source_4     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        selector     : in  std_logic_vector(1 downto 0);
        destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_MUX_4X1 is

    signal mux1_destination : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal mux2_destination : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    destination <= mux1_destination when (selector(1) = '0') else
                   mux2_destination;

    MUX_1 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            source_1     => source_1,
            source_2     => source_2,
            selector     => selector(0),
            destination  => mux1_destination
        );

    MUX_2 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => DATA_WIDTH
        )
        port map (
            source_1     => source_3,
            source_2     => source_4,
            selector     => selector(0),
            destination  => mux2_destination
        );

end architecture;
