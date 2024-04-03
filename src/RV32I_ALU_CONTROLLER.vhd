library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_ALU_CONTROLLER is
  
    port (
        opcode      : in t_OPCODE;
        function_3  : in t_FUNCTION;
        function_7  : in std_logic_vector(6 downto 0);
        destination : out std_logic_vector(3 downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_CONTROLLER is

    -- No signals

begin

    destination <= "0000" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_AND ) and (function_7 = "0000000") else
                   "0001" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_OR  ) and (function_7 = "0000000") else
                   "0010" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_ADD ) and (function_7 = "0000000") else
                   "0110" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SUB ) and (function_7 = "0100000") else
                   "0111" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SLT ) and (function_7 = "0000000") else
                   "0010" when (opcode = OPCODE_LOAD(OPCODE_RANGE)  ) and(function_3 = FUNCTION_LW  ) else
                   "0010" when (opcode = OPCODE_STORE(OPCODE_RANGE) ) and(function_3 = FUNCTION_SW  ) else
                   "0000" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_ANDI) else
                   "0001" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_ORI ) else
                   "0010" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_ADDI) else
                   "0001" when (opcode = OPCODE_LUI(OPCODE_RANGE)   ) else
                   "0001" when (opcode = OPCODE_AUIPC(OPCODE_RANGE)   ) else
                   "0000";

end architecture;
