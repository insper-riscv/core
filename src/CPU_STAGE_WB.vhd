library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity CPU_STAGE_WB is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );

    port (
        clock              : in  std_logic;
        clear              : in  std_logic;
        enable             : in  std_logic;
        source             : in  WORK.CPU.t_SIGNALS_MEM_WB;
        enable_destination : out std_logic;
        select_destination : out WORK.CPU.t_REGISTER;
        destination        : out WORK.CPU.t_DATA
    );

end entity;

architecture RV32I of CPU_STAGE_WB is

    signal source_0 : WORK.CPU.t_SIGNALS_MEM_WB := WORK.CPU.NULL_SIGNALS_MEM_WB;

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(clock)
        begin
            if (rising_edge(clock)) then
                if (enable = '1') then
                    if (clear = '1') then
                        source_0 <= WORK.CPU.NULL_SIGNALS_MEM_WB;
                    else
                        source_0 <= source;
                    end if;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    WRITE_BACK : entity WORK.MODULE_WRITE_BACK(RV32I)
        port map (
            selector         => source_0.control_wb.select_destination,
            source_execution => source_0.data_destination,
            source_memory    => source_0.data_memory,
            destination      => destination
        );

    enable_destination <= source_0.control_wb.enable_destination;
    select_destination <= source_0.select_destination;

end architecture;
