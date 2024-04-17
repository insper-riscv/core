library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity CPU_LOAD_EXTENDER is

    generic (
        DATA_WIDTH     : natural := XLEN;
        HALFWORD_WIDTH : natural := 16;
        BYTE_WIDTH     : natural := 8;
        SELECTOR_WIDTH : natural := 3
    );
  
    port (
        source      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        selector  : in  std_logic_vector((SELECTOR_WIDTH - 1) downto 0);
        output_1 : out std_logic_vector((SELECTOR_WIDTH - 1) downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of CPU_LOAD_EXTENDER is

    constant LOW_MEMORY   : std_logic_vector((DATA_WIDTH - 1) downto BYTE_WIDTH) := (others => '0');

    signal halfword_tmp   : std_logic_vector((DATA_WIDTH - 1) downto HALFWORD_WIDTH) := (others => '0');
    signal byte_tmp       : std_logic_vector((DATA_WIDTH - 1) downto BYTE_WIDTH) := (others => '0');
    signal halfword       : std_logic_vector((HALFWORD_WIDTH - 1) downto 0) := (others => '0');
    signal byte           : std_logic_vector((BYTE_WIDTH - 1) downto 0) := (others => '0');

begin

    output_1 <= selector;

    halfword_tmp <= (others => source(HALFWORD_WIDTH - 1));
    byte_tmp <= (others => source(BYTE_WIDTH - 1));
    halfword <= source((HALFWORD_WIDTH - 1) downto 0);
    byte <= source((BYTE_WIDTH - 1) downto 0);

    destination <= byte_tmp & byte when selector = "000" else
                   halfword_tmp & halfword when selector = "001" else
                   LOW_MEMORY((DATA_WIDTH - 1) downto BYTE_WIDTH) & byte when selector = "100" else
                   LOW_MEMORY((DATA_WIDTH - 1) downto HALFWORD_WIDTH) & halfword when selector = "101" else
                   source;    

end architecture;
