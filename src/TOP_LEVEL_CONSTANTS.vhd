library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package TOP_LEVEL_CONSTANTS is

    constant CLOCK_FREQUENCY : integer := 50_000_000; -- 50 MHz clock frequency
    constant DATA_WIDTH      : integer := 32;

    subtype DATA_RANGE is natural range (DATA_WIDTH - 1) downto 0;

    subtype INSTRUCTION_RANGE is natural range 31 downto 0;
    type RV32I_INSTRUCTION_TYPE is (
        RV32I_INSTRUCTION_R_TYPE,
        RV32I_INSTRUCTION_I_TYPE,
        RV32I_INSTRUCTION_S_TYPE,
        RV32I_INSTRUCTION_B_TYPE,
        RV32I_INSTRUCTION_U_TYPE,
        RV32I_INSTRUCTION_J_TYPE
    );

    subtype FUNCTION_RANGE is natural range 2 downto 0;
    subtype t_FUNCTION is std_logic_vector(FUNCTION_RANGE);

    subtype OPCODE_RANGE is natural range 6 downto 0;
    subtype t_OPCODE is std_logic_vector(OPCODE_RANGE);

    type t_RV32I_INSTRUCTION is record
        funct_3     : t_FUNCTION;
        funct_7     : std_logic_vector( 6 downto 0);
        source_2    : std_logic_vector( 4 downto 0);
        source_1    : std_logic_vector( 4 downto 0);
        destination : std_logic_vector( 4 downto 0);
        immediate_i : std_logic_vector(31 downto 0);
        immediate_s : std_logic_vector(31 downto 0);
        immediate_b : std_logic_vector(31 downto 0);
        immediate_u : std_logic_vector(31 downto 0);
        immediate_j : std_logic_vector(31 downto 0);
        shamt       : std_logic_vector(31 downto 0);
        opcode      : t_OPCODE;
        encoding    : RV32I_INSTRUCTION_TYPE;
    end record;

    function to_RV32I_INSTRUCTION(in_vec: std_logic_vector(INSTRUCTION_RANGE)) return t_RV32I_INSTRUCTION;

    -- RV32I Base Instruction Set functions
    constant FUNCTION_JALR    : t_FUNCTION := "000";
    constant FUNCTION_BEQ     : t_FUNCTION := "000";
    constant FUNCTION_BNE     : t_FUNCTION := "001";
    constant FUNCTION_BLT     : t_FUNCTION := "100";
    constant FUNCTION_BGE     : t_FUNCTION := "101";
    constant FUNCTION_BLTU    : t_FUNCTION := "110";
    constant FUNCTION_BGEU    : t_FUNCTION := "111";
    constant FUNCTION_LB      : t_FUNCTION := "000";
    constant FUNCTION_LH      : t_FUNCTION := "001";
    constant FUNCTION_LW      : t_FUNCTION := "010";
    constant FUNCTION_LBU     : t_FUNCTION := "100";
    constant FUNCTION_LHU     : t_FUNCTION := "101";
    constant FUNCTION_SB      : t_FUNCTION := "000";
    constant FUNCTION_SH      : t_FUNCTION := "001";
    constant FUNCTION_SW      : t_FUNCTION := "010";
    constant FUNCTION_ADDI    : t_FUNCTION := "000";
    constant FUNCTION_SLTI    : t_FUNCTION := "010";
    constant FUNCTION_SLTIU   : t_FUNCTION := "011";
    constant FUNCTION_XORI    : t_FUNCTION := "100";
    constant FUNCTION_ORI     : t_FUNCTION := "110";
    constant FUNCTION_ANDI    : t_FUNCTION := "111";
    constant FUNCTION_SLLI    : t_FUNCTION := "001";
    constant FUNCTION_SRLI    : t_FUNCTION := "101";
    constant FUNCTION_SRAI    : t_FUNCTION := "101";
    constant FUNCTION_ADD     : t_FUNCTION := "000";
    constant FUNCTION_SUB     : t_FUNCTION := "000";
    constant FUNCTION_SLL     : t_FUNCTION := "001";
    constant FUNCTION_SLT     : t_FUNCTION := "010";
    constant FUNCTION_SLTU    : t_FUNCTION := "011";
    constant FUNCTION_XOR     : t_FUNCTION := "100";
    constant FUNCTION_SRL     : t_FUNCTION := "101";
    constant FUNCTION_SRA     : t_FUNCTION := "101";
    constant FUNCTION_OR      : t_FUNCTION := "110";
    constant FUNCTION_AND     : t_FUNCTION := "111";
    constant FUNCTION_FENCE   : t_FUNCTION := "000";
    constant FUNCTION_FENCE_I : t_FUNCTION := "001";
    constant FUNCTION_ECALL   : t_FUNCTION := "000";
    constant FUNCTION_EBREAK  : t_FUNCTION := "000";
    constant FUNCTION_CSRRW   : t_FUNCTION := "001";
    constant FUNCTION_CSRRS   : t_FUNCTION := "010";
    constant FUNCTION_CSRRC   : t_FUNCTION := "011";
    constant FUNCTION_CSRRWI  : t_FUNCTION := "101";
    constant FUNCTION_CSRRSI  : t_FUNCTION := "110";
    constant FUNCTION_CSRRCI  : t_FUNCTION := "111";

    -- RV32M Standard Extension Set functions
    constant FUNCTION_MUL    : t_FUNCTION := "000";
    constant FUNCTION_MULH   : t_FUNCTION := "001";
    constant FUNCTION_MULHSU : t_FUNCTION := "010";
    constant FUNCTION_MULHU  : t_FUNCTION := "011";
    constant FUNCTION_DIV    : t_FUNCTION := "100";
    constant FUNCTION_DIVU   : t_FUNCTION := "101";
    constant FUNCTION_REM    : t_FUNCTION := "110";
    constant FUNCTION_REMU   : t_FUNCTION := "111";

    -- RV32I Base Instruction Set opcodes
    constant OPCODE_OP     : t_OPCODE := "0110011";
    constant OPCODE_OP_IMM : t_OPCODE := "0010011";
    constant OPCODE_BRANCH : t_OPCODE := "1100011";
    constant OPCODE_LOAD   : t_OPCODE := "0000011";
    constant OPCODE_STORE  : t_OPCODE := "0100011";
    constant OPCODE_SYSTEM : t_OPCODE := "1110011";
    constant OPCODE_SYNCH  : t_OPCODE := "0001111";
    constant OPCODE_LUI    : t_OPCODE := "0110111";
    constant OPCODE_AUIPC  : t_OPCODE := "0010111";
    constant OPCODE_JAL    : t_OPCODE := "1101111";
    constant OPCODE_JALR   : t_OPCODE := "1100111";

end package;

package body TOP_LEVEL_CONSTANTS is

    function to_RV32I_INSTRUCTION(in_vec: std_logic_vector(INSTRUCTION_RANGE) := (others => '0')) return t_RV32I_INSTRUCTION is
        variable out_vec: t_RV32I_INSTRUCTION;
        variable immediate_i: std_logic_vector(31 downto 0) := (others => '0');
        variable immediate_s: std_logic_vector(31 downto 0) := (others => '0');
        variable immediate_b: std_logic_vector(31 downto 0) := (others => '0');
        variable immediate_u: std_logic_vector(31 downto 0) := (others => '0');
        variable immediate_j: std_logic_vector(31 downto 0) := (others => '0');
    begin
        immediate_i(11 downto  0) := in_vec(31 downto 20);
        immediate_s(11 downto  5) := in_vec(11 downto 5);
        immediate_s( 4 downto  0) := in_vec(11 downto 7);
        immediate_b(12)           := in_vec(31);
        immediate_b(10 downto  5) := in_vec(10 downto 5);
        immediate_b( 4 downto  1) := in_vec( 4 downto 1);
        immediate_b(11)           := in_vec(11);
        immediate_u(31 downto 12) := in_vec(31 downto 12);
        immediate_j(20)           := in_vec(31);
        immediate_j(10 downto  1) := in_vec(30 downto 21);
        immediate_j(11)           := in_vec(20);
        immediate_j(19 downto 12) := in_vec(19 downto 12);

        out_vec.funct_3     := in_vec(FUNCTION_RANGE);
        out_vec.funct_7     := in_vec(31 downto 25);
        out_vec.source_2    := in_vec(24 downto 20);
        out_vec.source_1    := in_vec(19 downto 15);
        out_vec.destination := in_vec(11 downto  7);
        out_vec.immediate_i := immediate_i;
        out_vec.immediate_s := immediate_s;
        out_vec.immediate_b := immediate_b;
        out_vec.immediate_u := immediate_u;
        out_vec.immediate_j := immediate_j;
        out_vec.opcode      := in_vec(OPCODE_RANGE);

        if out_vec.opcode = OPCODE_AND then
            out_vec.encoding := RV32I_INSTRUCTION_R_TYPE;
        end if;

        if (
            out_vec.opcode = OPCODE_OP_IMM or
            out_vec.opcode = OPCODE_SYSTEM or
            out_vec.opcode = OPCODE_SYNCH or
            out_vec.opcode = OPCODE_LOAD or
            out_vec.opcode = OPCODE_JALR
        ) then
            out_vec.encoding := RV32I_INSTRUCTION_I_TYPE;
        end if;

        if (
            out_vec.opcode = OPCODE_LOAD or
            out_vec.opcode = OPCODE_AUIPC
        ) then
            out_vec.encoding := RV32I_INSTRUCTION_U_TYPE;
        end if;

        if out_vec.opcode = OPCODE_BRANCH then
            out_vec.encoding := RV32I_INSTRUCTION_B_TYPE;
        end if;

        if out_vec.opcode = OPCODE_JAL then
            out_vec.encoding := RV32I_INSTRUCTION_J_TYPE;
        end if;

        if out_vec.opcode = OPCODE_STORE then
            out_vec.encoding := RV32I_INSTRUCTION_S_TYPE;
        end if;

        -- case out_vec.opcode is
        --     when OPCODE_AND =>
        --         out_vec.encoding := RV32I_INSTRUCTION_R_TYPE;
        --     when OPCODE_ANDI | OPCODE_JALR | OPCODE_FENCE | OPCODE_ECALL | OPCODE_LW =>
        --         out_vec.encoding := RV32I_INSTRUCTION_I_TYPE;
        --     when OPCODE_LUI | OPCODE_AUIPC =>
        --         out_vec.encoding := RV32I_INSTRUCTION_U_TYPE;
        --     when OPCODE_BEQ =>
        --         out_vec.encoding := RV32I_INSTRUCTION_B_TYPE;
        --     when OPCODE_JAL =>
        --         out_vec.encoding := RV32I_INSTRUCTION_J_TYPE;
        --     when OPCODE_SW =>
        --         out_vec.encoding := RV32I_INSTRUCTION_S_TYPE;
        --     when others =>
        --         out_vec.encoding := RV32I_INSTRUCTION_R_TYPE;
        -- end case;

        return out_vec;
    end function;

end package body;
