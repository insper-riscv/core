library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library WORK;
use WORK.GENERICS.ALL;

entity MODULE_CONTROL_UNIT is

    generic (
        DATA_WIDTH        : natural := WORK.RV32I.XLEN;
        INSTRUCTION_WIDTH : natural := WORK.RV32I.INSTRUCTION_WIDTH
    );

    port (
        clear       : in std_logic;
        instruction : in  std_logic_vector((INSTRUCTION_WIDTH - 1) downto 0);
        immediate   : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        control_id  : out WORK.CPU.t_CONTROL_ID;
        control_ex  : out WORK.CPU.t_CONTROL_EX;
        control_mem : out WORK.CPU.t_CONTROL_MEM;
        control_wb  : out WORK.CPU.t_CONTROL_WB
    );

end entity;

architecture RV32I of MODULE_CONTROL_UNIT is

    alias opcode   is instruction(WORK.RV32I.OPCODE_RANGE);

    signal is_lui    : std_logic;
    signal is_auipc  : std_logic;
    signal is_jalr   : std_logic;
    signal is_load   : std_logic;
    signal r_type    : std_logic;
    signal i_type    : std_logic;
    signal s_type    : std_logic;
    signal b_type    : std_logic;
    signal u_type    : std_logic;
    signal j_type    : std_logic;

begin

    is_lui   <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_LUI);
    is_auipc <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_AUIPC);
    is_jalr  <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_JALR);
    is_load  <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_LOAD);
    r_type   <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP);
    i_type   <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_OP_IMM) OR is_equal_dynamic(opcode, WORK.RV32I.OPCODE_LOAD) OR is_equal_dynamic(opcode, WORK.RV32I.OPCODE_SYSTEM) OR is_jalr;
    s_type   <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_STORE);
    b_type   <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_BRANCH);
    u_type   <= is_lui OR is_auipc;
    j_type   <= is_equal_dynamic(opcode, WORK.RV32I.OPCODE_JAL);

    -- Stage Instruction Decode controls
    control_id.enable_branch <= b_type;

    control_id.enable_jump <= j_type OR is_jalr;

    control_id.select_jump <= is_jalr;

    -- Stage Execute controls
    control_ex.select_source_1(0) <= j_type OR is_jalr OR is_auipc;
    control_ex.select_source_1(1) <= is_lui;

    control_ex.select_source_2(0) <= (i_type OR u_type OR s_type) AND NOT is_jalr;
    control_ex.select_source_2(1) <= is_jalr;

    -- Stage Memory Access controls
    control_mem.enable_read <= is_load;

    control_mem.enable_write <= s_type;

    -- Write Back controls
    control_wb.enable_destination <= r_type OR i_type OR u_type OR j_type;

    control_wb.select_destination <= is_load;

    -- Immediate generating
    immediate(31) <= instruction(31);

    MUX_IMMEDIATE19_20 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 11
        )
        port map (
            selector    => u_type,
            source_1    => (others => instruction(31)),
            source_2    => instruction(30 downto 20),
            destination => immediate(30 downto 20)
        );

    MUX_IMMEDIATE_19_12 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 8
        )
        port map (
            selector    => u_type OR j_type,
            source_1    => (others => instruction(31)),
            source_2    => instruction(19 downto 12),
            destination => immediate(19 downto 12)
        );

    MUX_IMMEDIATE_11 : entity WORK.GENERIC_MUX_4X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => (u_type OR j_type) & (u_type OR b_type),
            source_1    => (others => instruction(31)),
            source_2    => instruction(7 downto 7),
            source_3    => instruction(20 downto 20),
            source_4    => (others => '0'),
            destination => immediate(11 downto 11)
        );

    MUX_IMMEDIATE_10_5 : entity WORK.GENERIC_MUX_2X1
        generic map (
            DATA_WIDTH => 6
        )
        port map (
            selector    => u_type,
            source_1    => instruction(30 downto 25),
            source_2    => (others => '0'),
            destination => immediate(10 downto 5)
        );

    MUX_IMMEDIATE_4_1 : entity WORK.GENERIC_MUX_4X1
        generic map (
            DATA_WIDTH => 4
        )
        port map (
            selector    => u_type & (s_type OR b_type),
            source_1    => instruction(24 downto 21),
            source_2    => instruction(11 downto 8),
            source_3    => (others => '0'),
            source_4    => (others => '0'),
            destination => immediate(4 downto 1)
        );

    MUX_IMMEDIATE_0 : entity WORK.GENERIC_MUX_4X1
        generic map (
            DATA_WIDTH => 1
        )
        port map (
            selector    => s_type & i_type,
            source_1    => (others => '0'),
            source_2    => instruction(20 downto 20),
            source_3    => instruction(7 downto 7),
            source_4    => (others => '0'),
            destination => immediate(0 downto 0)
        );

end architecture;
