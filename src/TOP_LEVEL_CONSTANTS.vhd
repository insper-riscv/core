library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package TOP_LEVEL_CONSTANTS is

    constant CLOCK_FREQUENCY : integer := 50_000_000; -- 50 MHz clock frequency

    constant XLEN : natural := 32;
    subtype XLEN_RANGE is natural range (XLEN - 1) downto 0;
    subtype t_DATA is std_logic_vector(XLEN_RANGE);

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

    subtype OPCODE_FULL_RANGE is natural range 6 downto 0;
    subtype t_OPCODE_FULL is std_logic_vector(OPCODE_FULL_RANGE);

    subtype OPCODE_RANGE is natural range 6 downto 2;
    subtype t_OPCODE is std_logic_vector(OPCODE_RANGE);

    subtype REGISTER_RANGE is natural range 4 downto 0;
    subtype t_REGISTER is std_logic_vector(REGISTER_RANGE);

    type t_RV32I_INSTRUCTION is record
        funct_3            : t_FUNCTION;
        funct_7            : std_logic_vector(6 downto 0);
        select_source_2    : t_REGISTER;
        select_source_1    : t_REGISTER;
        select_destination : t_REGISTER;
        immediate_i        : t_DATA;
        immediate_s        : t_DATA;
        immediate_b        : t_DATA;
        immediate_u        : t_DATA;
        immediate_j        : t_DATA;
        shamt              : t_DATA;
        opcode             : t_OPCODE;
        encoding           : RV32I_INSTRUCTION_TYPE;
    end record;

    function to_RV32I_INSTRUCTION(in_vec: std_logic_vector(INSTRUCTION_RANGE) := (others => '0')) return t_RV32I_INSTRUCTION;

    type t_CONTROL_CLK_CLR_EN is record
        clock  : std_logic;
        clear  : std_logic;
        enable : std_logic;
    end record;

    type t_CONTROL_IF is record
        enable_stall  : std_logic;
        enable_flush  : std_logic;
        enable_jump   : std_logic;
        select_source : std_logic;
    end record;

    type t_CONTROL_ID is record
        select_jump     : std_logic;
        enable_jump     : std_logic;
        enable_flush_id : std_logic;
        enable_flux_ex  : std_logic;
    end record;

    type t_CONTROL_EX is record
        select_source_1  : std_logic_vector(1 downto 0);
        select_source_2  : std_logic_vector(1 downto 0);
        select_operation : std_logic_vector(1 downto 0);
    end record;

    type t_CONTROL_MEM is record
        enable_read  : std_logic;
        enable_write : std_logic;
    end record;

    type t_CONTROL_WB is record
        enable_destination : std_logic;
        select_destination : std_logic;
    end record;

    type t_SIGNALS_IF_ID is record
        address_program  : t_DATA;
        data_instruction : t_DATA;
    end record;

    type t_SIGNALS_ID_EX is record
        control_ex         : t_CONTROL_EX;
        control_mem        : t_CONTROL_MEM;
        control_wb         : t_CONTROL_WB;
        address_program    : t_DATA;
        data_source_1      : t_DATA;
        data_source_2      : t_DATA;
        data_immediate     : t_DATA;
        funct_7            : std_logic_vector(6 downto 0);
        funct_3            : t_FUNCTION;
        opcode             : t_OPCODE;
        select_destination : t_REGISTER;
    end record;

    type t_SIGNALS_EX_MEM is record
        control_mem        : t_CONTROL_MEM;
        control_wb         : t_CONTROL_WB;
        address_pointer    : t_DATA;
        data_source_2      : t_DATA;
        select_destination : t_REGISTER;
    end record;

    type t_SIGNALS_MEM_WB is record
        control_wb         : t_CONTROL_WB;
        data_memory        : t_DATA;
        data_destination   : t_DATA;
        select_destination : t_REGISTER;
    end record;

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
    constant OPCODE_OP     : t_OPCODE_FULL := "0110011";
    constant OPCODE_OP_IMM : t_OPCODE_FULL := "0010011";
    constant OPCODE_JALR   : t_OPCODE_FULL := "1100111";
    constant OPCODE_SYNCH  : t_OPCODE_FULL := "0001111";
    constant OPCODE_SYSTEM : t_OPCODE_FULL := "1110011";
    constant OPCODE_STORE  : t_OPCODE_FULL := "0100011";
    constant OPCODE_LOAD   : t_OPCODE_FULL := "0000011";
    constant OPCODE_BRANCH : t_OPCODE_FULL := "1100011";
    constant OPCODE_LUI    : t_OPCODE_FULL := "0110111";
    constant OPCODE_AUIPC  : t_OPCODE_FULL := "0010111";
    constant OPCODE_JAL    : t_OPCODE_FULL := "1101111";

end package;

package body TOP_LEVEL_CONSTANTS is

    function to_RV32I_INSTRUCTION(in_vec: std_logic_vector(INSTRUCTION_RANGE) := (others => '0')) return t_RV32I_INSTRUCTION is
        variable out_vec: t_RV32I_INSTRUCTION;
        variable immediate_i: t_DATA;
        variable immediate_s: t_DATA;
        variable immediate_b: t_DATA;
        variable immediate_u: t_DATA;
        variable immediate_j: t_DATA;
    begin
        immediate_i(31 downto 11) := (others => in_vec(31));
        immediate_i(10 downto  0) := in_vec(30 downto 20);
        
        immediate_s(31 downto 11) := (others => in_vec(31));
        immediate_s(10 downto  0) := in_vec(30 downto 25) & in_vec(11 downto 7);

        immediate_b(31 downto 12) := (others => in_vec(31));
        immediate_b(11 downto  0) := in_vec(7) & in_vec(30 downto 25) & in_vec(11 downto 8) & '0';

        immediate_u(31 downto  12) := in_vec(31 downto 12);
        immediate_u(11 downto  0)  := (others => '0');

        immediate_j(31 downto 21) := (others => in_vec(31));
        immediate_j(20 downto  0) := in_vec(31) & in_vec(19 downto 12) & in_vec(20) & in_vec(30 downto 21) & '0';

        out_vec.funct_3            := in_vec(FUNCTION_RANGE);
        out_vec.funct_7            := in_vec(31 downto 25);
        out_vec.select_source_2    := in_vec(24 downto 20);
        out_vec.select_source_1    := in_vec(19 downto 15);
        out_vec.select_destination := in_vec(11 downto  7);
        out_vec.immediate_i        := immediate_i;
        out_vec.immediate_s        := immediate_s;
        out_vec.immediate_b        := immediate_b;
        out_vec.immediate_u        := immediate_u;
        out_vec.immediate_j        := immediate_j;
        out_vec.opcode             := in_vec(OPCODE_RANGE);

        if out_vec.opcode(OPCODE_RANGE) = OPCODE_OP(OPCODE_RANGE) then
            out_vec.encoding := RV32I_INSTRUCTION_R_TYPE;
        end if;

        if (
            out_vec.opcode(OPCODE_RANGE) = OPCODE_JALR(OPCODE_RANGE) or
            out_vec.opcode(OPCODE_RANGE) = OPCODE_LOAD(OPCODE_RANGE) or
            out_vec.opcode(OPCODE_RANGE) = OPCODE_OP_IMM(OPCODE_RANGE) or
            out_vec.opcode(OPCODE_RANGE) = OPCODE_SYNCH(OPCODE_RANGE) or
            out_vec.opcode(OPCODE_RANGE) = OPCODE_SYSTEM(OPCODE_RANGE)
        ) then
            out_vec.encoding := RV32I_INSTRUCTION_I_TYPE;
        end if;

        if out_vec.opcode(OPCODE_RANGE) = OPCODE_STORE(OPCODE_RANGE) then
            out_vec.encoding := RV32I_INSTRUCTION_S_TYPE;
        end if;

        if out_vec.opcode(OPCODE_RANGE) = OPCODE_BRANCH(OPCODE_RANGE) then
            out_vec.encoding := RV32I_INSTRUCTION_B_TYPE;
        end if;

        if (
            out_vec.opcode(OPCODE_RANGE) = OPCODE_LUI(OPCODE_RANGE) or
            out_vec.opcode(OPCODE_RANGE) = OPCODE_AUIPC(OPCODE_RANGE)
        ) then
            out_vec.encoding := RV32I_INSTRUCTION_U_TYPE;
        end if;

        if out_vec.opcode(OPCODE_RANGE) = OPCODE_JAL(OPCODE_RANGE) then
            out_vec.encoding := RV32I_INSTRUCTION_J_TYPE;
        end if;

        return out_vec;
    end function;

end package body;
