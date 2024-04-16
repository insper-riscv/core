library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_ALU is

    generic (
        DATA_WIDTH : natural := WORK.RV32I.XLEN
    );
  
    port (
        select_function : in  std_logic_vector(4 downto 0);
        source_1        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_2        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_ALU is

    signal result           : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal result_extended  : std_logic;
    signal carry            : std_logic_vector((DATA_WIDTH) downto 0);
    signal carry_extended   : std_logic;
    signal slt              : std_logic_vector((DATA_WIDTH - 1) downto 0)   := (others => '0');
    signal overflow         : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal shift            : std_logic_vector((DATA_WIDTH - 1) downto 0);

begin

    carry(0) <= select_function(3) XOR select_function(4);

    slt(0) <=   carry_extended when (select_function = "00111") else 
                carry(DATA_WIDTH) XOR carry(DATA_WIDTH - 1) XOR result(DATA_WIDTH - 1);

    BIT_TO_BIT : for i in 0 to (DATA_WIDTH - 1) generate
        FOR_BIT : entity WORK.RV32I_ALU_BIT
            port map (
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

    EXTENDED_SIGN_BIT : entity WORK.RV32I_ALU_BIT
        port map (
            select_function => select_function,
            carry_in        => carry(DATA_WIDTH),
            slt             => '0',
            source_1        => '0',
            source_2        => '0',
            destination     => result_extended,
            carry_out       => carry_extended
        );

    SHIFTER : entity WORK.RV32I_ALU_SHIFTER
        generic map (
            DATA_WIDTH  => WORK.RV32I.XLEN,
            SHAMT_WIDTH => 5
        )
        port map (
            select_function => select_function,
            shamt           => source_2(4 downto 0),
            source          => source_1,
            destination     => shift
        );

    destination <=  shift when (
                        select_function = "00100" or
                        select_function = "00101" or
                        select_function = "00110"
                    ) else 
                    result;

end architecture;
