library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_INSTRUCTION_DECODER is
  
    port (
        instruction : in  std_logic_vector(INSTRUCTION_RANGE);
        control_if  : out t_IF_SIGNALS;
        control_id  : out t_ID_SIGNALS;
        control_ex  : out t_EX_SIGNALS;
        control_mem : out t_MEM_SIGNALS;
        control_wb  : out t_WB_SIGNALS;
        immediate   : out std_logic_vector(INSTRUCTION_RANGE) := (others => '0')
    );

end entity;

architecture RTL of RV32I_INSTRUCTION_DECODER is

    shared variable rv32i_instruction : t_RV32I_INSTRUCTION := to_RV32I_INSTRUCTION(instruction);

begin

    --control_if.enable_flush     <= ;
    control_if.enable_jump      <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_J_TYPE) else
                                   '0';
    --control_if.select_source_pc <= ;

    control_id.enable_jump     <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_J_TYPE) else
                                  '0';
    --control_id.select_jump     <= ;
    --control_id.enable_flush_id <= ;
    --control_id.enable_flux_ex  <= ;

    control_ex.select_source_1  <= "01" when (rv32i_instruction.opcode = OPCODE_AUIPC) else
                                   "00";
    control_ex.select_source_2  <= "01" when (rv32i_instruction.encoding = RV32I_INSTRUCTION_I_TYPE) else
                                   "00";
    --control_ex.select_operation <= ;


    control_mem.enable_read  <= '1' when (rv32i_instruction.opcode = OPCODE_LOAD) else
                                '0';
    control_mem.enable_write <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_R_TYPE) else
                                '0';

    control_wb.enable_registers   <= '1' when (rv32i_instruction.encoding = RV32I_INSTRUCTION_R_TYPE) else
                                     '0';
    control_wb.select_destination <= '1' when (rv32i_instruction.opcode = OPCODE_LOAD) else
                                     '0';

end architecture;
