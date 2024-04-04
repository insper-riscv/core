library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU_REGISTER_SOURCE is

    generic (
        DATA_WIDTH  : natural := XLEN
    );
  
    port (
        register_source_1     : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        register_source_2     : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        forwarding_mem_source : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        forwarding_wb_source  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        select_source_1       : in  std_logic_vector(1 downto 0) := (others => '0');
        select_source_2       : in  std_logic_vector(1 downto 0) := (others => '0');
        data_source_1         : out  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_2         : out  std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of MODULE_ALU_REGISTER_SOURCE is

    -- No signals

begin

    MUX_REGISTER_ALU_1 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => register_source_1,
            source_2    => forwarding_wb_source,
            source_3    => forwarding_mem_source,
            source_4    => (others => '0'),
            selector    => select_source_1,
            destination => data_source_1
        );

    MUX_REGISTER_ALU_2 : entity WORK.GENERIC_MUX_4X1
        port map (
            source_1    => register_source_2,
            source_2    => forwarding_wb_source,
            source_3    => forwarding_mem_source,
            source_4    => (others => '0'),
            selector    => select_source_2,
            destination => data_source_2
        );

end architecture;
