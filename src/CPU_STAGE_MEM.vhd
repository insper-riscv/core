library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity CPU_STAGE_MEM is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );

    port (
        clock          : in  std_logic;
        clear          : in  std_logic;
        enable         : in  std_logic;
        source         : in  WORK.CPU.t_SIGNALS_EX_MEM;
        control_memory : out WORK.CPU.t_CONTROL_MEM;
        address_memory : out WORK.CPU.t_DATA;
        data_memory    : out WORK.CPU.t_DATA;
        destination    : out WORK.CPU.t_SIGNALS_MEM_WB
    );

end entity;

architecture RV32I of CPU_STAGE_MEM is

    signal source_0 : WORK.CPU.t_SIGNALS_EX_MEM := WORK.CPU.NULL_SIGNALS_EX_MEM;

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(source, clear, clock, enable)
        begin
            if (rising_edge(clock)) then
                SET_RESET : if (enable = '1') then
                    source_0 <= source;
                elsif (clear = '1') then
                    source_0 <= WORK.CPU.NULL_SIGNALS_EX_MEM;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    destination.control_wb         <= source_0.control_wb;

    control_memory.enable_read     <= source_0.control_mem.enable_read;
    control_memory.enable_write    <= source_0.control_mem.enable_write;

    address_memory                 <= source_0.address_pointer;
    data_memory                    <= source_0.data_source_2;
    funct_3                        <= source_0.control_mem.funct_3;
    store_byte                     <= source_0.control_mem.store_byte;
    store_halfword                 <= source_0.control_mem.store_halfword;

    destination.data_memory        <= (others => '-');
    destination.data_destination   <= source_0.address_pointer;
    destination.select_destination <= source_0.select_destination;

end architecture;
