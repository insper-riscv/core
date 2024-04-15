library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_ALU is

    generic (
        DATA_WIDTH : natural := XLEN
    );
  
    port (
        invert_source_1 : in  std_logic;
        invert_source_2 : in  std_logic;
        select_function : in  std_logic_vector(2 downto 0);
        source_1        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_ALU is

    signal result            : std_logic_vector((DATA_WIDTH)     downto 0);
    signal carry             : std_logic_vector((DATA_WIDTH + 1) downto 0);
    signal slt               : std_logic_vector((DATA_WIDTH)     downto 0) := (others => '0');
    signal overflow          : std_logic_vector((DATA_WIDTH)     downto 0);
    signal shift             : std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
    signal invert_bit_2      : std_logic;
    signal extended_source_1 : std_logic_vector((DATA_WIDTH)     downto 0) := (others => '0');
    signal extended_source_2 : std_logic_vector((DATA_WIDTH)     downto 0) := (others => '0');

begin

    extended_source_1((DATA_WIDTH - 1) downto 0) <= source_1;
    extended_source_2((DATA_WIDTH - 1) downto 0) <= source_2;
    
    invert_bit_2 <= '1' when (select_function = "111" and invert_source_2 = '0') else
                    invert_source_2;

    carry(0) <= invert_source_1 XOR invert_bit_2;
    slt(0)   <= overflow(DATA_WIDTH - 1) when (select_function /= "111" or invert_source_2 /= '0') else 
                overflow(DATA_WIDTH);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH) generate
        FOR_BIT : entity WORK.RV32I_ALU_BIT
            port map (
                invert_source_1 => invert_source_1,
                invert_source_2 => invert_bit_2,
                select_function => select_function,
                carry_in        => carry(i),
                slt             => slt(i),
                source_1        => extended_source_1(i),
                source_2        => extended_source_2(i),
                destination     => result(i),
                carry_out       => carry(i + 1),
                overflow        => overflow(i)
            );
    end generate;

    GENERIC_SHIFTER : entity WORK.GENERIC_SHIFTER
            port map (
                source      => source_1,
                selector_1  => source_2(4 downto 0),
                selector_2  => select_function,
                destination => shift
            );

    destination <= shift when (
                       select_function = "100" or
                       select_function = "101" or
                       select_function = "110"
                    ) else 
                   result((DATA_WIDTH - 1) downto 0);

    --flag_z  <= '1' when (result = ZERO) else
    --           '0';

end architecture;
