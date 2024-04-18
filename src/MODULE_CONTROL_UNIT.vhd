library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library WORK;
use WORK.MODULES.ALL;
use G.GENERICS.all;

entity MODULE_CONTROL_UNIT is

    port (
        instruction : in  WORK.CPU.t_INSTRUCTION;
        immediate   : out WORK.CPU.t_DATA;
        control_if  : out WORK.CPU.t_CONTROL_IF;
        control_id  : out WORK.CPU.t_CONTROL_ID;
        control_ex  : out WORK.CPU.t_CONTROL_EX;
        control_mem : out WORK.CPU.t_CONTROL_MEM;
        control_wb  : out WORK.CPU.t_CONTROL_WB
    );

end entity;

architecture RV32I of MODULE_CONTROL_UNIT is

    -- No signals

begin

    process(instruction) is
        variable temp : WORK.RV32I.t_INSTRUCTION;
    begin
        temp := WORK.RV32I.to_instruction(instruction);

        case temp.encoding is
            when WORK.RV32I.INSTRUCTION_I_TYPE =>
                immediate <= temp.immediate_i;
            when WORK.RV32I.INSTRUCTION_S_TYPE =>
                immediate <= temp.immediate_s;
            when WORK.RV32I.INSTRUCTION_B_TYPE =>
                immediate <= temp.immediate_b;
            when WORK.RV32I.INSTRUCTION_U_TYPE =>
                immediate <= temp.immediate_u;
            when WORK.RV32I.INSTRUCTION_J_TYPE =>
                immediate <= temp.immediate_j;
            when others =>
                immediate <= (others => '0');
        end case;

        -- Instruction Fetch controls
        control_if.enable_stall <= '0';

        control_if.enable_flush <= '0';

        case temp.encoding is
            when WORK.RV32I.INSTRUCTION_J_TYPE =>
                control_if.enable_jump <= '1';
            when others =>
                control_if.enable_jump <= '0';
        end case;

        case temp.encoding is
            when WORK.RV32I.INSTRUCTION_J_TYPE =>
                control_if.select_source <= '1';
            when others =>
                control_if.select_source <= '0';
        end case;

        -- Instruction Decode controls
        control_id.select_jump <= '0';

        case temp.encoding is
            when WORK.RV32I.INSTRUCTION_J_TYPE =>
                control_if.enable_jump <= '1';
            when others =>
                control_if.enable_jump <= '0';
        end case;

        control_id.enable_flush_id <= '0';

        control_id.enable_flux_ex <= '0';

        -- Execute controls

        case temp.opcode is
            when    WORK.RV32I.OPCODE_AUIPC |
                    WORK.RV32I.OPCODE_JAL   =>
                control_ex.select_source_1 <= "01";
            when WORK.RV32I.OPCODE_LUI =>
                control_ex.select_source_1 <= "10";
            when others =>
                control_ex.select_source_1 <= "00";
        end case;

        case temp.encoding is
            when    WORK.RV32I.INSTRUCTION_I_TYPE   |
                    WORK.RV32I.INSTRUCTION_U_TYPE   |
                    WORK.RV32I.INSTRUCTION_S_TYPE   =>
                control_ex.select_source_2 <= "01";
            when others =>
                case temp.opcode is
                    when    WORK.RV32I.OPCODE_JAL   |
                            WORK.RV32I.OPCODE_JALR  =>
                        control_ex.select_source_2 <= "10";
                    when others =>
                        control_ex.select_source_2 <= "00";
                end case;
        end case;

        control_ex.select_operation <= (others => '0');


        -- Memory Access controls

        case temp.opcode is
            when WORK.RV32I.OPCODE_LOAD =>
                control_mem.enable_read <= '1';
            when others =>
                control_mem.enable_read <= '0';
        end case;

        case temp.encoding is
            when WORK.RV32I.INSTRUCTION_S_TYPE =>
                control_mem.enable_write <= '1';
            when others =>
                control_mem.enable_write <= '0';
        end case;

        -- Write Back controls
        case temp.encoding is
            when    WORK.RV32I.INSTRUCTION_R_TYPE   | 
                    WORK.RV32I.INSTRUCTION_I_TYPE   | 
                    WORK.RV32I.INSTRUCTION_U_TYPE   | 
                    WORK.RV32I.INSTRUCTION_J_TYPE   =>
                control_wb.enable_destination <= '1';
            when others =>
                control_wb.enable_destination <= '0';
        end case;

        case temp.opcode is
            when WORK.RV32I.OPCODE_LOAD =>
                control_wb.select_destination <= '1';
            when others =>
                control_wb.select_destination <= '0';
        end case;
    end process;
    
end architecture;
