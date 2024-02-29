library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_INSTRUCTION_DECODER is
  
    port (
        instruction      : in  std_logic_vector(INSTRUCTION_RANGE);
        enable_registers : out std_logic;
        enable_immediate : out std_logic;
        enable_jump : out std_logic
    );

end entity;

architecture RTL of RV32I_INSTRUCTION_DECODER is

    shared variable rv32i_instruction : t_RV32I_INSTRUCTION := to_RV32I_INSTRUCTION(instruction);

begin

    enable_registers <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_R_TYPE) else
                        '0';

    enable_immediate <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_I_TYPE) else
                        '0';

    enable_jump <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_J_TYPE) else
                   '0';

end architecture;
