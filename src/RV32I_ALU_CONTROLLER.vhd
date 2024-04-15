library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.RV32I.ALL;

entity RV32I_ALU_CONTROLLER is
  
    port (
        opcode      : in t_OPCODE;
        function_3  : in t_FUNCTION3;
        function_7  : in t_FUNCTION7;
        destination : out std_logic_vector(4 downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_CONTROLLER is

    -- No signals

begin

    destination <= "00010" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_XOR  ) and (function_7 = "0000000") else
                   "00000" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_AND  ) and (function_7 = "0000000") else
                   "00001" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_OR   ) and (function_7 = "0000000") else
                   "00011" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_ADD  ) and (function_7 = "0000000") else
                   "01011" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SUB  ) and (function_7 = "0100000") else
                   "01111" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SLT  ) and (function_7 = "0000000") else
                   "00111" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SLTU ) and (function_7 = "0000000") else
                   "00100" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SLL  ) and (function_7 = "0000000") else
                   "00101" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SRL  ) and (function_7 = "0000000") else
                   "00110" when (opcode = OPCODE_OP(OPCODE_RANGE)    ) and(function_3 = FUNCTION_SRA  ) and (function_7 = "0100000") else
                   "00011" when (opcode = OPCODE_LOAD(OPCODE_RANGE)  ) and(function_3 = FUNCTION_LB   ) else
                   "00011" when (opcode = OPCODE_LOAD(OPCODE_RANGE)  ) and(function_3 = FUNCTION_LH   ) else
                   "00011" when (opcode = OPCODE_LOAD(OPCODE_RANGE)  ) and(function_3 = FUNCTION_LBU  ) else
                   "00011" when (opcode = OPCODE_LOAD(OPCODE_RANGE)  ) and(function_3 = FUNCTION_LHU  ) else
                   "00011" when (opcode = OPCODE_LOAD(OPCODE_RANGE)  ) and(function_3 = FUNCTION_LW   ) else
                   "00011" when (opcode = OPCODE_STORE(OPCODE_RANGE) ) and(function_3 = FUNCTION_SB   ) else
                   "00011" when (opcode = OPCODE_STORE(OPCODE_RANGE) ) and(function_3 = FUNCTION_SH   ) else
                   "00011" when (opcode = OPCODE_STORE(OPCODE_RANGE) ) and(function_3 = FUNCTION_SW   ) else
                   "00000" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_ANDI ) else
                   "00010" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_XORI ) else
                   "00001" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_ORI  ) else
                   "00011" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_ADDI ) else
                   "01111" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_SLTI ) else
                   "00111" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_SLTIU) else
                   "00100" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_SLLI ) and (function_7 = "0000000") else
                   "00101" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_SRLI ) and (function_7 = "0000000") else
                   "00110" when (opcode = OPCODE_OP_IMM(OPCODE_RANGE)) and(function_3 = FUNCTION_SRAI ) and (function_7 = "0100000") else
                   "00011" when (opcode = OPCODE_JAL(OPCODE_RANGE)   ) else
                   "00011" when (opcode = OPCODE_JALR(OPCODE_RANGE)  ) else
                   "00001" when (opcode = OPCODE_LUI(OPCODE_RANGE)   ) else
                   "00001" when (opcode = OPCODE_AUIPC(OPCODE_RANGE) ) else
                   "00000";

end architecture;
