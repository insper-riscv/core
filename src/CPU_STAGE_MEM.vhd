library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity CPU_STAGE_MEM is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );

    port (
        clock           : in  std_logic;
        clear           : in  std_logic;
        enable          : in  std_logic;
        source          : in  WORK.CPU.t_SIGNALS_EX_MEM;
        data_memory_in  : in  WORK.CPU.t_DATA;
        control_memory  : out WORK.CPU.t_CONTROL_MEM;
        address_memory  : out WORK.CPU.t_DATA;
        data_memory_out : out WORK.CPU.t_DATA;
        destination     : out WORK.CPU.t_SIGNALS_MEM_WB
    );

end entity;

architecture RV32I of CPU_STAGE_MEM is

    signal source_0 : WORK.CPU.t_SIGNALS_EX_MEM := WORK.CPU.NULL_SIGNALS_EX_MEM;

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(clock)
        begin
            if (rising_edge(clock)) then
                if (enable = '1') then
                    if (clear = '1') then
                        source_0 <= WORK.CPU.NULL_SIGNALS_EX_MEM;
                    else
                        source_0 <= source;
                    end if;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    destination.control_wb         <= source_0.control_wb;

    control_memory.enable_read     <= source_0.control_mem.enable_read;
    control_memory.enable_write    <= source_0.control_mem.enable_write;

    address_memory                 <= source_0.data_destination;

    destination.data_destination   <= source_0.data_destination;
    destination.select_destination <= source_0.select_destination;

    MEM_INTERFACE: entity WORK.MODULE_MEMORY_INTERFACE(RV32I)
        generic map (
            FUNCTION_WIDTH => WORK.RV32I.FUNCT3_WIDTH,
            DATA_WIDTH     => WORK.RV32I.XLEN
        )
        port map (
            select_function      => source_0.funct_3,
            source_data_in       => data_memory_in,
            source_data_out      => source_0.data_source_2,
            destination_data_in  => destination.data_memory,
            destination_data_out => data_memory_out
        );

end architecture;
