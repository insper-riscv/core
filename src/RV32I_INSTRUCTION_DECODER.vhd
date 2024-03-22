library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_INSTRUCTION_DECODER is

    port (
        instruction : in  std_logic_vector(INSTRUCTION_RANGE);
        control_if  : out t_CONTROL_IF;
        control_id  : out t_CONTROL_ID;
        control_ex  : out t_CONTROL_EX;
        control_mem : out t_CONTROL_MEM;
        control_wb  : out t_CONTROL_WB;
        immediate   : out std_logic_vector(INSTRUCTION_RANGE)
    );

end entity;

architecture RTL of RV32I_INSTRUCTION_DECODER is

    signal rv32i_instruction : t_RV32I_INSTRUCTION;

begin

    process(instruction, rv32i_instruction) is
    begin
        rv32i_instruction <= to_RV32I_INSTRUCTION(instruction);
    end process;

    control_if.enable_stall     <= '0';
    control_if.enable_flush     <= '0';
    control_if.enable_jump      <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_J_TYPE) else
                                   '0';
    control_if.select_source    <= '1';

    control_id.select_jump     <= '0';
    control_id.enable_jump     <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_J_TYPE) else
                                  '0';
    control_id.enable_flush_id <= '0';
    control_id.enable_flux_ex  <= '0';

    control_ex.select_source_1  <= "01" when (rv32i_instruction.opcode = OPCODE_AUIPC(OPCODE_RANGE)) else
                                   "10" when (rv32i_instruction.opcode = OPCODE_LUI(OPCODE_RANGE)) else
                                   "00";
    control_ex.select_source_2  <= "01" when (
                                       (rv32i_instruction.encoding = RV32I_INSTRUCTION_I_TYPE) or 
                                       (rv32i_instruction.opcode = OPCODE_LUI(OPCODE_RANGE))
                                   ) else
                                   "00";
    control_ex.select_operation <= (others => '0');


    control_mem.enable_read  <= '1' when (rv32i_instruction.opcode = OPCODE_LOAD(OPCODE_RANGE)) else
                                '0';
    control_mem.enable_write <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_R_TYPE) else
                                '0';

    control_wb.enable_destination <= '1' when (
                                         (rv32i_instruction.encoding = RV32I_INSTRUCTION_R_TYPE) or 
                                         (rv32i_instruction.opcode = OPCODE_LUI(OPCODE_RANGE))
                                     ) else
                                     '0';
    control_wb.select_destination <= '1' when rv32i_instruction.opcode = OPCODE_LUI(OPCODE_RANGE) else
                                     '0';

    immediate <= rv32i_instruction.immediate_i when (rv32i_instruction.encoding = RV32I_INSTRUCTION_I_TYPE) else
                 rv32i_instruction.immediate_s when (rv32i_instruction.encoding = RV32I_INSTRUCTION_S_TYPE) else
                 rv32i_instruction.immediate_b when (rv32i_instruction.encoding = RV32I_INSTRUCTION_B_TYPE) else
                 rv32i_instruction.immediate_u when (rv32i_instruction.encoding = RV32I_INSTRUCTION_U_TYPE) else
                 rv32i_instruction.immediate_j when (rv32i_instruction.encoding = RV32I_INSTRUCTION_J_TYPE) else
                 (others => '0');

end architecture;
