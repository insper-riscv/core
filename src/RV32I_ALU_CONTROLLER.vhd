library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_ALU_CONTROLLER is
  
    port (
        opcode     : in std_logic_vector(OPCODE_RANGE);
        function_3 : in std_logic_vector(FUNCTION_RANGE);
        function_7 : in std_logic_vector(6 downto 0);
        destination   : out std_logic_vector(3 downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_CONTROLLER is

    -- No signals

begin

    destination <= "0000" when (function_3 = FUNCTION_AND)  and (opcode = OPCODE_OP) and (function_7 = "0000000") else
                   "0001" when (function_3 = FUNCTION_OR)   and (opcode = OPCODE_OP) and (function_7 = "0000000") else
                   "0010" when (function_3 = FUNCTION_ADD)  and (opcode = OPCODE_OP) and (function_7 = "0000000") else
                   "0110" when (function_3 = FUNCTION_SUB)  and (opcode = OPCODE_OP) and (function_7 = "0100000") else
                   "0111" when (function_3 = FUNCTION_SLT)  and (opcode = OPCODE_OP) and (function_7 = "0000000") else
                   "0010" when (function_3 = FUNCTION_LW)   and (opcode = OPCODE_LOAD) else
                   "0010" when (function_3 = FUNCTION_SW)   and (opcode = OPCODE_STORE) else
                   "0000" when (function_3 = FUNCTION_ANDI) and (opcode = OPCODE_OP_IMM) else
                   "0001" when (function_3 = FUNCTION_ORI)  and (opcode = OPCODE_OP_IMM) else
                   "0010" when (function_3 = FUNCTION_ADDI) and (opcode = OPCODE_OP_IMM) else
                   "0000";

end architecture;
