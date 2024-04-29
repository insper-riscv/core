library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_ALU is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );
  
    port (
        select_function : in  std_logic_vector(3 downto 0);
        source_1        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        overflow        : out std_logic;
        destination     : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_ALU is

    signal result               : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal result_extended      : std_logic;
    signal carry                : std_logic_vector((DATA_WIDTH) downto 0);
    signal carry_extended       : std_logic;
    signal overflow_auxiliar    : std_logic;
    signal slt                  : std_logic_vector((DATA_WIDTH - 1) downto 0)   := (others => '0');
    signal shift                : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    carry(0) <= '1' when (
                    select_function = "1000" or
                    select_function = "0010" or
                    select_function = "0011"
                ) else
                '0';

    overflow_auxiliar <=    carry_extended XOR carry(DATA_WIDTH) when (select_function(1 downto 0) = "11") else
                            carry(DATA_WIDTH) XOR carry(DATA_WIDTH - 1);

    overflow <= overflow_auxiliar;

    slt(0) <=   overflow_auxiliar XOR result_extended when (select_function(1 downto 0) = "11") else
                overflow_auxiliar XOR result(DATA_WIDTH - 1);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH - 1) generate
        FOR_BIT : entity WORK.RV32I_ALU_BIT
            port map (
                select_function => select_function,
                carry_in        => carry(i),
                source_1        => source_1(i),
                source_2        => source_2(i),
                destination     => result(i),
                carry_out       => carry(i + 1)
            );
    end generate;

    EXTENDED_SIGN_BIT : entity WORK.RV32I_ALU_BIT
        port map (
            select_function => select_function,
            carry_in        => carry(DATA_WIDTH),
            source_1        => '0',
            source_2        => '0',
            destination     => result_extended,
            carry_out       => carry_extended
        );

    SHIFTER : entity WORK.RV32I_ALU_SHIFTER
        generic map (
            DATA_WIDTH  => WORK.RV32I.XLEN
        )
        port map (
            select_function => select_function,
            shamt           => source_2(4 downto 0),
            source          => source_1,
            destination     => shift
        );

    destination <=  shift when (
                        select_function = "0001" or
                        select_function(2 downto 0) = "101"
                    ) else 
                    slt when (
                        select_function = "1010" or
                        select_function = "1011"
                    ) else
                    result;

end architecture;
