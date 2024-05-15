library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.MATH_REAL.ALL;

library WORK;

package RV32I is

    subtype XLEN_RANGE        is natural range 31 downto  0;
    subtype INSTRUCTION_RANGE is natural range 31 downto  0;
    subtype FUNCT3_RANGE      is natural range 14 downto 12;
    subtype FUNCT7_RANGE      is natural range 31 downto 25;
    subtype OPCODE_FULL_RANGE is natural range  6 downto  0;
    subtype OPCODE_RANGE      is natural range  6 downto  2;
    subtype REGISTER_RANGE    is natural range  4 downto  0;

    subtype t_DATA        is std_logic_vector(XLEN_RANGE);
    subtype t_PROGRAM     is std_logic_vector(INSTRUCTION_RANGE);
    subtype t_FUNCT3      is std_logic_vector(FUNCT3_RANGE);
    subtype t_FUNCT7      is std_logic_vector(FUNCT7_RANGE);
    subtype t_OPCODE_FULL is std_logic_vector(OPCODE_FULL_RANGE);
    subtype t_OPCODE      is std_logic_vector(OPCODE_RANGE);
    subtype t_REGISTER    is std_logic_vector(REGISTER_RANGE);

    type t_INSTRUCTION_TYPE is (
        INSTRUCTION_R_TYPE,
        INSTRUCTION_I_TYPE,
        INSTRUCTION_S_TYPE,
        INSTRUCTION_B_TYPE,
        INSTRUCTION_U_TYPE,
        INSTRUCTION_J_TYPE
    );

    type t_INSTRUCTION is record
        funct_3            : t_FUNCT3;
        funct_7            : t_FUNCT7;
        select_source_2    : t_REGISTER;
        select_source_1    : t_REGISTER;
        select_destination : t_REGISTER;
        immediate_i        : t_DATA;
        immediate_s        : t_DATA;
        immediate_b        : t_DATA;
        immediate_u        : t_DATA;
        immediate_j        : t_DATA;
        shamt              : std_logic_vector(4 downto 0);
        opcode             : t_OPCODE;
        encoding           : t_INSTRUCTION_TYPE;
    end record;

    constant XLEN              : natural := 32;
    constant INSTRUCTION_WIDTH : natural := 32;
    constant FUNCT3_WIDTH      : natural :=  3;
    constant FUNCT7_WIDTH      : natural :=  7;
    constant OPCODE_FULL_WIDTH : natural :=  7;
    constant OPCODE_WIDTH      : natural :=  5;
    constant REGISTER_WIDTH    : natural :=  5;

    -- RV32I Base Instruction Set opcodes
    constant OPCODE_FULL_OP     : t_OPCODE_FULL := 7X"33";
    constant OPCODE_FULL_OP_IMM : t_OPCODE_FULL := 7X"13";
    constant OPCODE_FULL_JALR   : t_OPCODE_FULL := 7X"67";
    constant OPCODE_FULL_SYNCH  : t_OPCODE_FULL := 7X"0F";
    constant OPCODE_FULL_SYSTEM : t_OPCODE_FULL := 7X"73";
    constant OPCODE_FULL_STORE  : t_OPCODE_FULL := 7X"23";
    constant OPCODE_FULL_LOAD   : t_OPCODE_FULL := 7X"03";
    constant OPCODE_FULL_BRANCH : t_OPCODE_FULL := 7X"63";
    constant OPCODE_FULL_LUI    : t_OPCODE_FULL := 7X"37";
    constant OPCODE_FULL_AUIPC  : t_OPCODE_FULL := 7X"17";
    constant OPCODE_FULL_JAL    : t_OPCODE_FULL := 7X"6F";

    -- RV32I Base Instruction Set opcodes (ignored 2 LSB)
    constant OPCODE_OP     : t_OPCODE := 5X"0C";
    constant OPCODE_OP_IMM : t_OPCODE := 5X"04";
    constant OPCODE_JALR   : t_OPCODE := 5X"19";
    constant OPCODE_SYNCH  : t_OPCODE := 5X"03";
    constant OPCODE_SYSTEM : t_OPCODE := 5X"1C";
    constant OPCODE_STORE  : t_OPCODE := 5X"08";
    constant OPCODE_LOAD   : t_OPCODE := 5X"00";
    constant OPCODE_BRANCH : t_OPCODE := 5X"18";
    constant OPCODE_LUI    : t_OPCODE := 5X"0D";
    constant OPCODE_AUIPC  : t_OPCODE := 5X"05";
    constant OPCODE_JAL    : t_OPCODE := 5X"1B";

    -- RV32I Base Instruction Set functions
    constant FUNCT3_JALR    : t_FUNCT3 := 3X"0";
    constant FUNCT3_BEQ     : t_FUNCT3 := 3X"0";
    constant FUNCT3_BNE     : t_FUNCT3 := 3X"1";
    constant FUNCT3_BLT     : t_FUNCT3 := 3X"4";
    constant FUNCT3_BGE     : t_FUNCT3 := 3X"5";
    constant FUNCT3_BLTU    : t_FUNCT3 := 3X"6";
    constant FUNCT3_BGEU    : t_FUNCT3 := 3X"7";
    constant FUNCT3_LB      : t_FUNCT3 := 3X"0";
    constant FUNCT3_LH      : t_FUNCT3 := 3X"1";
    constant FUNCT3_LW      : t_FUNCT3 := 3X"2";
    constant FUNCT3_LBU     : t_FUNCT3 := 3X"4";
    constant FUNCT3_LHU     : t_FUNCT3 := 3X"5";
    constant FUNCT3_SB      : t_FUNCT3 := 3X"0";
    constant FUNCT3_SH      : t_FUNCT3 := 3X"1";
    constant FUNCT3_SW      : t_FUNCT3 := 3X"2";
    constant FUNCT3_ADDI    : t_FUNCT3 := 3X"0";
    constant FUNCT3_SLTI    : t_FUNCT3 := 3X"2";
    constant FUNCT3_SLTIU   : t_FUNCT3 := 3X"3";
    constant FUNCT3_XORI    : t_FUNCT3 := 3X"4";
    constant FUNCT3_ORI     : t_FUNCT3 := 3X"6";
    constant FUNCT3_ANDI    : t_FUNCT3 := 3X"7";
    constant FUNCT3_SLLI    : t_FUNCT3 := 3X"1";
    constant FUNCT3_SRLI    : t_FUNCT3 := 3X"5";
    constant FUNCT3_SRAI    : t_FUNCT3 := 3X"5";
    constant FUNCT3_ADD     : t_FUNCT3 := 3X"0";
    constant FUNCT3_SUB     : t_FUNCT3 := 3X"0";
    constant FUNCT3_SLL     : t_FUNCT3 := 3X"1";
    constant FUNCT3_SLT     : t_FUNCT3 := 3X"2";
    constant FUNCT3_SLTU    : t_FUNCT3 := 3X"3";
    constant FUNCT3_XOR     : t_FUNCT3 := 3X"4";
    constant FUNCT3_SRL     : t_FUNCT3 := 3X"5";
    constant FUNCT3_SRA     : t_FUNCT3 := 3X"5";
    constant FUNCT3_OR      : t_FUNCT3 := 3X"6";
    constant FUNCT3_AND     : t_FUNCT3 := 3X"7";
    constant FUNCT3_FENCE   : t_FUNCT3 := 3X"0";
    constant FUNCT3_ECALL   : t_FUNCT3 := 3X"0";
    constant FUNCT3_EBREAK  : t_FUNCT3 := 3X"0";

    constant FUNCT7_SLLI : t_FUNCT7 := 7X"00";
    constant FUNCT7_SRLI : t_FUNCT7 := 7X"00";
    constant FUNCT7_SRAI : t_FUNCT7 := 7X"20";
    constant FUNCT7_ADD  : t_FUNCT7 := 7X"00";
    constant FUNCT7_SUB  : t_FUNCT7 := 7X"20";
    constant FUNCT7_SLL  : t_FUNCT7 := 7X"00";
    constant FUNCT7_SLT  : t_FUNCT7 := 7X"00";
    constant FUNCT7_SLTU : t_FUNCT7 := 7X"00";
    constant FUNCT7_XOR  : t_FUNCT7 := 7X"00";
    constant FUNCT7_SRL  : t_FUNCT7 := 7X"00";
    constant FUNCT7_SRA  : t_FUNCT7 := 7X"20";
    constant FUNCT7_OR   : t_FUNCT7 := 7X"00";
    constant FUNCT7_AND  : t_FUNCT7 := 7X"00";

    constant NULL_INSTRUCTION : t_PROGRAM := (
        FUNCT7_RANGE      => FUNCT7_ADD,
        FUNCT3_RANGE      => FUNCT3_ADDI,
        OPCODE_FULL_RANGE => OPCODE_FULL_OP_IMM,
        others            => '0'
    );

    function to_immediate_i(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA;

    function to_immediate_s(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA;

    function to_immediate_b(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA;

    function to_immediate_u(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA;

    function to_immediate_j(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA;

    function to_instruction_type(
        in_vec : t_OPCODE
    ) return t_INSTRUCTION_TYPE;

    function to_instruction(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_INSTRUCTION;

end package;

package body RV32I is

    function to_immediate_i(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA is
        variable out_vec : t_DATA;
    begin
        out_vec(31 downto 11) := (others => in_vec(31));
        out_vec(10 downto  0) := in_vec(30 downto 20);

        return out_vec;
    end function;

    function to_immediate_s(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA is
        variable out_vec : t_DATA;
    begin
        out_vec(31 downto 11) := (others => in_vec(31));
        out_vec(10 downto  0) := in_vec(30 downto 25) & in_vec(11 downto 7);

        return out_vec;
    end function;

    function to_immediate_b(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA is
        variable out_vec : t_DATA;
    begin
        out_vec(31 downto 12) := (others => in_vec(31));
        out_vec(11 downto  0) := in_vec(7) & in_vec(30 downto 25) & in_vec(11 downto 8) & '0';

        return out_vec;
    end function;

    function to_immediate_u(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA is
        variable out_vec : t_DATA;
    begin
        out_vec(31 downto  12) := in_vec(31 downto 12);
        out_vec(11 downto  0)  := (others => '0');

        return out_vec;
    end function;

    function to_immediate_j(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_DATA is
        variable out_vec : t_DATA;
    begin
        out_vec(31 downto 21) := (others => in_vec(31));
        out_vec(20 downto  0) := in_vec(31) & in_vec(19 downto 12) & in_vec(20) & in_vec(30 downto 21) & '0';

        return out_vec;
    end function;

    function to_instruction_type(
        in_vec : t_OPCODE
    ) return t_INSTRUCTION_TYPE is
        -- No variables
    begin
        case in_vec is
            when
                OPCODE_OP =>
                return INSTRUCTION_R_TYPE;
            when
                OPCODE_JALR   |
                OPCODE_LOAD   |
                OPCODE_OP_IMM |
                OPCODE_SYNCH  |
                OPCODE_SYSTEM =>
                return INSTRUCTION_I_TYPE;
            when
                OPCODE_STORE =>
                return INSTRUCTION_S_TYPE;
            when 
                OPCODE_BRANCH =>
                return INSTRUCTION_B_TYPE;
            when
                OPCODE_LUI   |
                OPCODE_AUIPC =>
                return INSTRUCTION_U_TYPE;
            when
                OPCODE_JAL =>
                return INSTRUCTION_J_TYPE;
            when
                others =>
                return INSTRUCTION_R_TYPE;
        end case;
    end function;

    function to_instruction(
        in_vec : std_logic_vector(INSTRUCTION_RANGE)
    ) return t_INSTRUCTION is
        variable out_vec : t_INSTRUCTION;
    begin
        out_vec.funct_3            := in_vec(FUNCT3_RANGE);
        out_vec.funct_7            := in_vec(FUNCT7_RANGE);
        out_vec.select_source_2    := in_vec(24 downto 20);
        out_vec.select_source_1    := in_vec(19 downto 15);
        out_vec.select_destination := in_vec(11 downto  7);
        out_vec.immediate_i        := to_immediate_i(in_vec);
        out_vec.immediate_s        := to_immediate_s(in_vec);
        out_vec.immediate_b        := to_immediate_b(in_vec);
        out_vec.immediate_u        := to_immediate_u(in_vec);
        out_vec.immediate_j        := to_immediate_j(in_vec);
        out_vec.shamt              := in_vec(24 downto 20);
        out_vec.opcode             := in_vec(OPCODE_RANGE);
        out_vec.encoding           := to_instruction_type(out_vec.opcode);

        return out_vec;
    end function;

end package body;
