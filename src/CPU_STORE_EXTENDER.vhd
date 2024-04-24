library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity CPU_STORE_EXTENDER is
 
    port (
        source      : in  WORK.RV32I.t_DATA;
        selector    : in  WORK.RV32I.t_FUNCT3;
        destination : out WORK.RV32I.t_DATA
    );

end entity;

architecture RTL of CPU_STORE_EXTENDER is

    constant LOW_MEMORY   : std_logic_vector((WORK.CPU.DATA_WIDTH - 1) downto 8) := (others => '0');

begin

    destination <= LOW_MEMORY((WORK.CPU.DATA_WIDTH - 1) downto  8) & source( 7 downto 0) when selector = "000" else
                   LOW_MEMORY((WORK.CPU.DATA_WIDTH - 1) downto 16) & source(15 downto 0) when selector = "001" else
                   source;    

end architecture;
