library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity CPU_BRANCH_COMPARE_UNIT_BIT is

    port (
        invert_source_1 : in  std_logic;
        invert_source_2 : in  std_logic;
        carry_in        : in  std_logic;
        slt             : in  std_logic;
        source_1        : in  std_logic;
        source_2        : in  std_logic;
        carry_out       : out std_logic;
        overflow        : out std_logic
    );

end entity;

architecture RTL of CPU_BRANCH_COMPARE_UNIT_BIT is

    signal source_1_auxiliar : std_logic;
    signal source_2_auxiliar : std_logic;
    signal half_add          : std_logic;
    signal full_add          : std_logic;
    signal carry_auxiliar    : std_logic;

begin

    source_1_auxiliar <= source_1 XOR invert_source_1;
    source_2_auxiliar <= source_2 XOR invert_source_2;

    half_add <= source_1_auxiliar XOR source_2_auxiliar;
    full_add <= half_add XOR carry_in;

    carry_auxiliar <= (source_1_auxiliar AND source_2_auxiliar) OR (half_add AND carry_in);
    carry_out      <= carry_auxiliar;
    overflow       <= carry_auxiliar XOR carry_in XOR full_add;

end architecture;
