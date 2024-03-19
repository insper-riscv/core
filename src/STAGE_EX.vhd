library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_EX is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );
  
    port (
        clock       : in  std_logic;
        clear       : in  std_logic;
        enable      : in  std_logic;
        source      : in  t_SIGNALS_ID_EX;
        destination : out t_SIGNALS_EX_MEM
    );

end entity;

architecture RTL of STAGE_EX is

    signal source_0        : t_SIGNALS_ID_EX := NULL_SIGNALS_ID_EX;
    signal select_function : std_logic_vector(3 downto 0);

begin

    PIPELINE : if (GENERATE_REGISTERS = TRUE) generate
        UPDATE : process(source, clear, clock, enable)
        begin
            if (rising_edge(clock)) then
                SET_RESET : if (enable = '1') then
                    source_0 <= source;
                elsif (clear = '1') then
                    source_0 <= NULL_SIGNALS_ID_EX;
                end if;
            end if;
        end process;
    else generate
        source_0 <= source;
    end generate;

    MODULE_ALU_CONTROLLER : entity WORK.MODULE_ALU_CONTROLLER
        port map (
            opcode      => source_0.opcode,
            function_3  => source_0.funct_3,
            function_7  => source_0.funct_7,
            destination => select_function
        );

    MODULE_ALU : entity WORK.MODULE_ALU
        port map (
            select_source_1 => source_0.control_ex.select_source_1,
            select_source_2 => source_0.control_ex.select_source_2,
            address_program => source_0.address_program,
            data_source_1   => source_0.data_source_1,
            data_source_2   => source_0.data_source_2,
            data_immediate  => source_0.data_immediate,
            select_function => select_function,
            destination     => destination.address_pointer
        );

    destination.control_mem        <= source_0.control_mem;
    destination.control_wb         <= source_0.control_wb;
    destination.data_source_2      <= source_0.data_source_2;
    destination.select_destination <= source_0.select_destination;

end architecture;
