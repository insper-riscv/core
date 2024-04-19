library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity RV32I_ALU_CONTROLLER is

    port (
        opcode      : in  WORK.RV32I.t_OPCODE;
        funct3      : in  WORK.RV32I.t_FUNCT3;
        funct7      : in  WORK.RV32I.t_FUNCT7;
        destination : out std_logic_vector(3 downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_CONTROLLER is

    -- No signals

begin

    destination <=  funct7(30) & funct3 when (
                        opcode = WORK.RV32I.OPCODE_OP or
                        opcode = WORK.RV32I.OPCODE_OP_IMM
                    ) else
                    '0' & WORK.RV32I.FUNCT3_ADDI when (
                        opcode = WORK.RV32I.OPCODE_SYSTEM
                    ) else
                    '0' & WORK.RV32I.FUNCT3_ADD when (
                        opcode = WORK.RV32I.OPCODE_LOAD or
                        opcode = WORK.RV32I.OPCODE_STORE
                    ) else
                    '0' & WORK.RV32I.FUNCT3_OR;

end architecture;
