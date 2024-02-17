library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use IEEE.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_ALU is
  
    port (
        invert_source   : in  std_logic;
        invert_target   : in  std_logic;
        select_function : in  std_logic_vector(1 downto 0);
        source          : in  std_logic_vector(DATA_RANGE);
        target          : in  std_logic_vector(DATA_RANGE);
        destiny         : out std_logic_vector(DATA_RANGE);
        flag_z          : out std_logic
    );

end entity;

architecture CPU of RV32I_ALU is

    constant ZERO : std_logic_vector(DATA_RANGE) := (others => '0');

    signal result : std_logic_vector(DATA_RANGE);
    signal carry : std_logic_vector((DATA_RANGE'right + 1) downto 0);
    signal slt : std_logic_vector(DATA_RANGE) := (others => '0');
    signal overflow : std_logic_vector(DATA_RANGE);

begin

    carry(0) <= invert_source XOR invert_target;
    slt(0)   <= overflow(DATA_WIDTH - 1);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH - 1) generate
        FOR_BIT : entity WORK.RV32I_ALU_BIT
            port map (
                invert_source   => invert_source,
                invert_target   => invert_target,
                select_function => select_function,
                carry_in        => carry(i),
                slt             => slt(i),
                source          => source(i),
                target          => target(i),
                destiny         => result(i),
                carry_out       => carry(i+1),
                overflow        => overflow(i)
            );
    end generate;

    destiny <= result;

    flag_z  <= '1' when (result = ZERO) else
               '0';

end architecture;
