library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity CPU_BRANCH_COMPARE_UNIT is

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

architecture RTL of CPU_BRANCH_COMPARE_UNIT is

    signal result            : std_logic_vector((DATA_WIDTH)     downto 0);
    signal carry             : std_logic_vector((DATA_WIDTH + 1) downto 0);
    signal slt               : std_logic_vector((DATA_WIDTH)     downto 0) := (others => '0');
    signal overflow          : std_logic_vector((DATA_WIDTH)     downto 0);
    signal extended_source_1 : std_logic_vector((DATA_WIDTH)     downto 0) := (others => '0');
    signal extended_source_2 : std_logic_vector((DATA_WIDTH)     downto 0) := (others => '0');

begin

    extended_source_1((DATA_WIDTH - 1) downto 0) <= source_1;
    extended_source_2((DATA_WIDTH - 1) downto 0) <= source_2;
    
    carry(0) <= '1';
    slt(0)   <= overflow(DATA_WIDTH - 1) when (selector = "100" or selector = "101") else
                overflow(DATA_WIDTH);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH) generate
        FOR_BIT : entity WORK.CPU_BRANCH_COMPARE_UNIT_BIT
            port map (
                invert_source_1 => '0',
                invert_source_2 => '1',
                carry_in        => carry(i),
                slt             => slt(i),
                source_1        => extended_source_1(i),
                source_2        => extended_source_2(i),
                carry_out       => carry(i + 1),
                overflow        => overflow(i)
            );
    end generate;

    destination <= '1' when (branch = '1' and (
                   (selector = "000" and source_1 =  source_2) or
                   (selector = "001" and source_1 /= source_2) or 
                   (selector = "100" and slt(0)   =  '1'     ) or
                   (selector = "101" and slt(0)   =  '0'     ) or
                   (selector = "110" and slt(0)   =  '1'     ) or
                   (selector = "111" and slt(0)   =  '0'     ) 
                )) else
                '0';    

end architecture;