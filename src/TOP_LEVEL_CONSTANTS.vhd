library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package TOP_LEVEL_CONSTANTS is

    constant CLOCK_FREQUENCY : integer := 50_000_000; -- 50 MHz clock frequency
    constant DATA_WIDTH : integer := 32;

    subtype DATA_RANGE is natural range (DATA_WIDTH - 1) downto 0;

    subtype OPCODE_RANGE is natural range 6 downto 0;

    subtype FUNCTION_RANGE is natural range 2 downto 0;

    -- RV32I Base Instruction Set opcodes
    constant OPCODE_LUI     : std_logic_vector(OPCODE_RANGE) := "0110111";
    constant OPCODE_AUIPC   : std_logic_vector(OPCODE_RANGE) := "0010111";
    constant OPCODE_JAL     : std_logic_vector(OPCODE_RANGE) := "1101111";
    constant OPCODE_JALR    : std_logic_vector(OPCODE_RANGE) := "1100111";
    constant OPCODE_BEQ     : std_logic_vector(OPCODE_RANGE) := "1100011";
    constant OPCODE_BNE     : std_logic_vector(OPCODE_RANGE) := "1100011";
    constant OPCODE_BLT     : std_logic_vector(OPCODE_RANGE) := "1100011";
    constant OPCODE_BGE     : std_logic_vector(OPCODE_RANGE) := "1100011";
    constant OPCODE_BLTU    : std_logic_vector(OPCODE_RANGE) := "1100011";
    constant OPCODE_BGEU    : std_logic_vector(OPCODE_RANGE) := "1100011";
    constant OPCODE_LB      : std_logic_vector(OPCODE_RANGE) := "0000011";
    constant OPCODE_LH      : std_logic_vector(OPCODE_RANGE) := "0000011";
    constant OPCODE_LW      : std_logic_vector(OPCODE_RANGE) := "0000011";
    constant OPCODE_LBU     : std_logic_vector(OPCODE_RANGE) := "0000011";
    constant OPCODE_LHU     : std_logic_vector(OPCODE_RANGE) := "0000011";
    constant OPCODE_SB      : std_logic_vector(OPCODE_RANGE) := "0100011";
    constant OPCODE_SH      : std_logic_vector(OPCODE_RANGE) := "0100011";
    constant OPCODE_SW      : std_logic_vector(OPCODE_RANGE) := "0100011";
    constant OPCODE_ADDI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_SLTI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_SLTIU   : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_XORI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_ORI     : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_ANDI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_SLLI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_SRLI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_SRAI    : std_logic_vector(OPCODE_RANGE) := "0010011";
    constant OPCODE_ADD     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_SUB     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_SLL     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_SLT     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_SLTU    : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_XOR     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_SRL     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_SRA     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_OR      : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_AND     : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_FENCE   : std_logic_vector(OPCODE_RANGE) := "0001111";
    constant OPCODE_FENCE_I : std_logic_vector(OPCODE_RANGE) := "0001111";
    constant OPCODE_ECALL   : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_EBREAK  : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_CSRRW   : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_CSRRS   : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_CSRRC   : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_CSRRWI  : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_CSRRSI  : std_logic_vector(OPCODE_RANGE) := "1110011";
    constant OPCODE_CSRRCI  : std_logic_vector(OPCODE_RANGE) := "1110011";

    -- RV32M Standard Extension opcodes
    constant OPCODE_MUL    : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_MULH   : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_MULHSU : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_MULHU  : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_DIV    : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_DIVU   : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_REM    : std_logic_vector(OPCODE_RANGE) := "0110011";
    constant OPCODE_REMU   : std_logic_vector(OPCODE_RANGE) := "0110011";

    -- RV32I Base Instruction Set functions
    constant FUNCTION_JALR    : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_BEQ     : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_BNE     : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_BLT     : std_logic_vector(FUNCTION_RANGE) := "100";
    constant FUNCTION_BGE     : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_BLTU    : std_logic_vector(FUNCTION_RANGE) := "110";
    constant FUNCTION_BGEU    : std_logic_vector(FUNCTION_RANGE) := "111";
    constant FUNCTION_LB      : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_LH      : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_LW      : std_logic_vector(FUNCTION_RANGE) := "010";
    constant FUNCTION_LBU     : std_logic_vector(FUNCTION_RANGE) := "100";
    constant FUNCTION_LHU     : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_SB      : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_SH      : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_SW      : std_logic_vector(FUNCTION_RANGE) := "010";
    constant FUNCTION_ADDI    : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_SLTI    : std_logic_vector(FUNCTION_RANGE) := "010";
    constant FUNCTION_SLTIU   : std_logic_vector(FUNCTION_RANGE) := "011";
    constant FUNCTION_XORI    : std_logic_vector(FUNCTION_RANGE) := "100";
    constant FUNCTION_ORI     : std_logic_vector(FUNCTION_RANGE) := "110";
    constant FUNCTION_ANDI    : std_logic_vector(FUNCTION_RANGE) := "111";
    constant FUNCTION_SLLI    : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_SRLI    : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_SRAI    : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_ADD     : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_SUB     : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_SLL     : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_SLT     : std_logic_vector(FUNCTION_RANGE) := "010";
    constant FUNCTION_SLTU    : std_logic_vector(FUNCTION_RANGE) := "011";
    constant FUNCTION_XOR     : std_logic_vector(FUNCTION_RANGE) := "100";
    constant FUNCTION_SRL     : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_SRA     : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_OR      : std_logic_vector(FUNCTION_RANGE) := "110";
    constant FUNCTION_AND     : std_logic_vector(FUNCTION_RANGE) := "111";
    constant FUNCTION_FENCE   : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_FENCE_I : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_ECALL   : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_EBREAK  : std_logic_vector(FUNCTION_RANGE) := "000";
    constant FUNCTION_CSRRW   : std_logic_vector(FUNCTION_RANGE) := "001";
    constant FUNCTION_CSRRS   : std_logic_vector(FUNCTION_RANGE) := "010";
    constant FUNCTION_CSRRC   : std_logic_vector(FUNCTION_RANGE) := "011";
    constant FUNCTION_CSRRWI  : std_logic_vector(FUNCTION_RANGE) := "101";
    constant FUNCTION_CSRRSI  : std_logic_vector(FUNCTION_RANGE) := "110";
    constant FUNCTION_CSRRCI  : std_logic_vector(FUNCTION_RANGE) := "111";
  
end package;
