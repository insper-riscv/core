library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_BRANCH_CMP is

    generic (
        DATA_WIDTH       : natural := XLEN
    );

    port (
        source_1    : in  t_DATA;
        source_2    : in  t_DATA;
        selector    : in  std_logic_vector(2 downto 0);
        branch      : in  std_logic;
        destination : out std_logic
    );

end entity;

architecture RTL of RV32I_BRANCH_CMP is

begin

    destination <= '1' when (branch = '1' and (
                   (selector = "000" and source_1 = source_2) or
                   (selector = "001" and source_1 /= source_2)
                )) else
                '0';    

end architecture;