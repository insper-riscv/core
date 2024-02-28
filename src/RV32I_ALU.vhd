library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_ALU is

    generic (
        DATA_WIDTH_0 : natural := DATA_WIDTH
    );
  
    port (
        invert_source_1 : in  std_logic;
        invert_source_2 : in  std_logic;
        select_function : in  std_logic_vector(1 downto 0);
        source_1        : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        source_2        : in  std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
        flag_z          : out std_logic
    );

end entity;

architecture CPU of RV32I_ALU is

    constant ZERO : std_logic_vector((DATA_WIDTH_0 - 1) downto 0) := (others => '0');

    signal result   : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);
    signal carry    : std_logic_vector((DATA_RANGE'left + 1) downto 0);
    signal slt      : std_logic_vector((DATA_WIDTH_0 - 1) downto 0) := (others => '0');
    signal overflow : std_logic_vector((DATA_WIDTH_0 - 1) downto 0);

begin

    carry(0) <= invert_source_1 XOR invert_source_2;
    slt(0)   <= overflow(DATA_WIDTH - 1);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH - 1) generate
        FOR_BIT : entity WORK.RV32I_ALU_BIT
            port map (
                invert_source_1 => invert_source_1,
                invert_source_2 => invert_source_2,
                select_function => select_function,
                carry_in        => carry(i),
                slt             => slt(i),
                source_1        => source_1(i),
                source_2        => source_2(i),
                destination     => result(i),
                carry_out       => carry(i + 1),
                overflow        => overflow(i)
            );
    end generate;

    destination <= result;

    flag_z  <= '1' when (result = ZERO) else
               '0';

end architecture;
