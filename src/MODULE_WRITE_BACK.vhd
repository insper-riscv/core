library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity MODULE_WRITE_BACK is

    generic (
        DATA_WIDTH  : natural := WORK.CPU.DATA_WIDTH
    );

    port (
        selector         : in  std_logic;
        source_memory    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_execution : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination      : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_WRITE_BACK is

    package G is new WORK.GENERICS
        generic map (
            DATA_WIDTH => WORK.RV32I.XLEN
        );

begin

    MUX_SOURCE : component G.GENERIC_MUX_2X1
        port map (
            selector    => selector,
            source_1    => source_memory,
            source_2    => source_execution,
            destination => destination
        );

end architecture;
