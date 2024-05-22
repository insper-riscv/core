library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_ALU_ROW is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );

    port (
        invert_source_2 : in  std_logic;
        source_1        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        overflow        : out std_logic
    );

end entity;

architecture CPU of RV32I_ALU_ROW is

    signal source_2_auxiliar : std_logic;
    signal half_add          : std_logic;
    signal carry_auxiliar    : std_logic;
    signal result            : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal carry             : std_logic_vector( DATA_WIDTH      downto 0);

begin

    carry(0) <= invert_source_2;

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH - 1) generate
        FOR_BIT : entity WORK.RV32M_ALU_BIT
            port map (
                invert_source_2 => invert_source_2,
                carry_in        => carry(i),
                source_1        => source_1(i),
                source_2        => source_2(i),
                destination     => result(i),
                carry_out       => carry(i + 1)
            );
    end generate;

    source_2_auxiliar <= source_2(DATA_WIDTH - 1) XOR invert_source_2;
    half_add          <= source_1(DATA_WIDTH - 1) XOR source_2_auxiliar;
    carry_auxiliar    <= (source_1(DATA_WIDTH - 1) AND source_2_auxiliar) OR (half_add AND carry(DATA_WIDTH - 1));

    destination <= result;
    overflow    <= carry_auxiliar XOR carry(DATA_WIDTH - 1) XOR result(DATA_WIDTH - 1);

end architecture;
