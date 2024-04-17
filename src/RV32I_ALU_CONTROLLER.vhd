library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.RV32I.ALL;

entity RV32I_ALU_CONTROLLER is

    port (
        opcode      : in  WORK.RV32I.t_OPCODE;
        funct3      : in  WORK.RV32I.t_FUNCT3;
        funct7      : in  WORK.RV32I.t_FUNCT7;
        destination : out std_logic_vector(5 downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_CONTROLLER is

    -- No signals

begin

    destination <= "000010" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_XOR  ) and (funct7 = "0000000") else
                   "000000" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_AND  ) and (funct7 = "0000000") else
                   "000001" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_OR   ) and (funct7 = "0000000") else
                   "000011" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_ADD  ) and (funct7 = "0000000") else
                   "001011" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_SUB  ) and (funct7 = "0100000") else
                   "001111" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_SLT  ) and (funct7 = "0000000") else
                   "101111" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_SLTU ) and (funct7 = "0000000") else
                   "000100" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_SLL  ) and (funct7 = "0000000") else
                   "000101" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_SRL  ) and (funct7 = "0000000") else
                   "000110" when (opcode = WORK.RV32I.OPCODE_OP    ) and (funct3 = WORK.RV32I.FUNCT3_SRA  ) and (funct7 = "0100000") else
                   "000011" when (opcode = WORK.RV32I.OPCODE_LOAD  ) and (funct3 = WORK.RV32I.FUNCT3_LW   ) else
                   "000011" when (opcode = WORK.RV32I.OPCODE_STORE ) and (funct3 = WORK.RV32I.FUNCT3_SW   ) else
                   "000000" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_ANDI ) else
                   "000010" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_XORI ) else
                   "000001" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_ORI  ) else
                   "000011" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_ADDI ) else
                   "001111" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_SLTI ) else
                   "101111" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_SLTIU) else
                   "000100" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_SLLI ) and (funct7 = "0000000") else
                   "000101" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_SRLI ) and (funct7 = "0000000") else
                   "000110" when (opcode = WORK.RV32I.OPCODE_OP_IMM) and (funct3 = WORK.RV32I.FUNCT3_SRAI ) and (funct7 = "0100000") else
                   "000001" when (opcode = WORK.RV32I.OPCODE_LUI   ) else
                   "000001" when (opcode = WORK.RV32I.OPCODE_AUIPC ) else
                   "000000";

end architecture;
