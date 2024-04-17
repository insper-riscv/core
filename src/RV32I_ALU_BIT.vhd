library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity RV32I_ALU_BIT is

    port (
        select_function : in  std_logic_vector(3 downto 0);
        carry_in        : in  std_logic;
        source_1        : in  std_logic;
        source_2        : in  std_logic;
        destination     : out std_logic;
        carry_out       : out std_logic
    );

end entity;

architecture RTL of RV32I_ALU_BIT is

    signal source_1_auxiliar : std_logic;
    signal source_2_auxiliar : std_logic;
    signal half_add          : std_logic;
    signal full_add          : std_logic;
    signal carry_auxiliar    : std_logic;

begin

    source_2_auxiliar <= source_2 XOR select_function(3);

    half_add <= source_1 XOR source_2_auxiliar;
    full_add <= half_add XOR carry_in;

    destination <=  source_1 AND source_2_auxiliar when (select_function(2 downto 0) = "111") else
                    source_1 OR  source_2_auxiliar when (select_function(2 downto 0) = "110") else
                    half_add when (select_function(2 downto 0) = "100") else
                    full_add;

    carry_auxiliar <= (source_1 AND source_2_auxiliar) OR (half_add AND carry_in);
    carry_out      <= carry_auxiliar;

end architecture;
