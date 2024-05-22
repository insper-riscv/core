library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_CARRY_LOOKAHEAD is

    generic(
        DATA_WIDTH : natural := 8
    );

    port (
        carry_in        : in  std_logic                                   := '0';
        carry_generate  : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        carry_propagate : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
        carry_out       : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of GENERIC_CARRY_LOOKAHEAD is

    signal carry : std_logic_vector(DATA_WIDTH downto 0);

begin

    carry(0)  <= carry_in;
    carry_out <= carry(DATA_WIDTH downto 1);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH - 1) generate
        carry(i + 1) <= (carry(i) AND carry_propagate(i)) OR carry_generate(i);
    end generate;

end architecture;
