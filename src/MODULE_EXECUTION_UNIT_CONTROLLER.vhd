library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_EXECUTION_UNIT_CONTROLLER is

    generic (
        OPCODE_WIDTH : natural := WORK.RV32I.OPCODE_WIDTH;
        DATA_WIDTH   : natural := 4
    );

    port (
        opcode      : in  std_logic_vector((OPCODE_WIDTH - 1) downto 0);
        funct_3     : in  std_logic_vector(2 downto 0);
        funct_7     : in  std_logic_vector(6 downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_EXECUTION_UNIT_CONTROLLER is

    -- No signals

begin

    destination <=  '1' & funct_3 when (
                        (opcode = WORK.RV32I.OPCODE_OP or
                        opcode = WORK.RV32I.OPCODE_OP_IMM) and
                        (funct_3 = WORK.RV32I.FUNCT3_SLT or
                        funct_3 = WORK.RV32I.FUNCT3_SLTU)
                    ) else
                    '0' & funct_3 when (
                        opcode = WORK.RV32I.OPCODE_OP_IMM or
                        opcode = WORK.RV32I.OPCODE_JALR
                    ) else
                    funct_7(5) & funct_3 when (
                        opcode = WORK.RV32I.OPCODE_OP
                    ) else
                    '0' & WORK.RV32I.FUNCT3_ADD when (
                        opcode = WORK.RV32I.OPCODE_SYSTEM or
                        opcode = WORK.RV32I.OPCODE_LOAD or
                        opcode = WORK.RV32I.OPCODE_STORE
                    ) else
                    '0' & WORK.RV32I.FUNCT3_OR;

end architecture;
