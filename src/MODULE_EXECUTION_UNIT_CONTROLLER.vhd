library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.GENERICS.ALL;

entity MODULE_EXECUTION_UNIT_CONTROLLER is

    generic (
        OPCODE_WIDTH : natural := WORK.RV32I.OPCODE_WIDTH;
        DATA_WIDTH   : natural := 4
    );

    port (
        opcode      : in  std_ulogic_vector((OPCODE_WIDTH - 1) downto 0);
        funct_3     : in  std_ulogic_vector(2 downto 0);
        funct_7     : in  std_ulogic_vector(6 downto 0);
        destination : out std_ulogic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_EXECUTION_UNIT_CONTROLLER is

    -- No signals

begin

    destination <=  '1' & funct_3 when (
                        (
                            is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP) OR
                            is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP_IMM)
                        ) AND (
                            is_equal_dynamic(funct_3, WORK.RV32I.FUNCT3_SLT) OR
                            is_equal_dynamic(funct_3, WORK.RV32I.FUNCT3_SLTU)
                        )
                    ) else
                    funct_7(5) & funct_3 when (
                        is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP) OR
                        (
                            is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP_IMM) AND
                            (
                                is_equal_dynamic(funct_3, WORK.RV32I.FUNCT3_SLL) OR
                                is_equal_dynamic(funct_3, WORK.RV32I.FUNCT3_SRL)
                            )
                        )
                    ) else
                    '0' & funct_3 when (
                        is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP_IMM) OR
                        is_equal_dynamic(opcode, WORK.RV32I.OPCODE_JALR)
                    ) else
                    '0' & WORK.RV32I.FUNCT3_ADD when (
                        is_equal_dynamic(opcode, WORK.RV32I.OPCODE_SYSTEM) OR
                        is_equal_dynamic(opcode, WORK.RV32I.OPCODE_LOAD) OR
                        is_equal_dynamic(opcode, WORK.RV32I.OPCODE_STORE)
                    ) else
                    '0' & WORK.RV32I.FUNCT3_OR;

end architecture;
