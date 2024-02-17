library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity RV32I_ALU_BIT is

    port (
        invert_source   : in  std_logic;
        invert_target   : in  std_logic;
        select_function : in  std_logic_vector(1 downto 0);
        carry_in        : in  std_logic;
        slt             : in  std_logic;
        source          : in  std_logic;
        target          : in  std_logic;
        destiny         : out std_logic;
        carry_out       : out std_logic;
        overflow        : out std_logic
    );

end entity;

architecture RTL of RV32I_ALU_BIT is

    signal source_auxiliar : std_logic;
    signal target_auxiliar : std_logic;
    signal half_add        : std_logic;
    signal full_add        : std_logic;
    signal carry_auxiliar  : std_logic;

begin

    source_auxiliar <= source XOR invert_source;
    target_auxiliar <= target XOR invert_target;

    half_add <= source_auxiliar XOR target_auxiliar;
    full_add <= half_add XOR carry_in;

    destiny <= source_auxiliar AND target_auxiliar when (select_function = "00") else
               source_auxiliar OR  target_auxiliar when (select_function = "01") else
               full_add when (select_function = "10") else
               slt;

    carry_auxiliar <= (source_auxiliar AND target_auxiliar) OR (half_add AND carry_in);
    carry_out      <= carry_auxiliar;
    overflow       <= carry_auxiliar XOR carry_in XOR full_add;

end architecture;
