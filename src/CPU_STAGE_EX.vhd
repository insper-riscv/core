library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.CPU.ALL;

entity CPU_STAGE_EX is

    generic (
        GENERATE_REGISTERS : boolean := TRUE
    );
  
    port (
        clock                   : in  std_logic;
        clear                   : in  std_logic;
        enable                  : in  std_logic;
        selector_forwarding_mem : in  RV32I.t_REGISTER;
        enable_mem              : in  std_logic;
        selector_forwarding_wb  : in  RV32I.t_REGISTER;
        enable_wb               : in  std_logic;
        forwarding_mem_source   : in  t_DATA;
        forwarding_wb_source    : in  t_DATA;
        source                  : in  t_SIGNALS_ID_EX;
        destination             : out t_SIGNALS_EX_MEM
    );

end entity;

architecture RTL of CPU_STAGE_EX is

    signal source_0           : t_SIGNALS_ID_EX := NULL_SIGNALS_ID_EX;
    signal select_function    : std_logic_vector(4 downto 0);
    signal forward_register_1 : t_DATA;
    signal forward_register_2 : t_DATA;
    signal selector_forward_1 : std_logic_vector(1 downto 0);
    signal selector_forward_2 : std_logic_vector(1 downto 0);

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

    MODULE_EXECUTION_UNIT_CONTROLLER : entity WORK.MODULE_EXECUTION_UNIT_CONTROLLER
        port map (
            opcode      => source_0.opcode,
            function_3  => source_0.funct_3,
            function_7  => source_0.funct_7,
            destination => select_function
        );

    CPU_EXECUTION_FOWARDING_UNIT : entity WORK.CPU_EXECUTION_FOWARDING_UNIT
        port map (
            stage_ex_select_source_1     => source_0.select_source_1,
            stage_ex_select_source_2     => source_0.select_source_2,
            stage_mem_enable_destination => selector_forwarding_mem,
            stage_mem_select_destination => enable_mem,
            stage_wb_enable_destination  => selector_forwarding_wb,
            stage_wb_select_destination  => enable_wb,
            stage_id_select_source_1     => selector_forward_1,
            stage_id_select_source_2     => selector_forward_2
        );

    MODULE_EXECUTION_UNIT : entity WORK.MODULE_EXECUTION_UNIT
        port map (
            select_forward_1      => selector_forward_1,
            select_forward_2      => selector_forward_2,
            select_source_1       => source_0.control_ex.select_source_1,
            select_source_2       => source_0.control_ex.select_source_2,
            address_program       => source_0.address_program,
            forwarding_mem_source => forwarding_mem_source,
            forwarding_wb_source  => forwarding_wb_source,
            data_source_1         => source_0.data_source_1,
            data_source_2         => source_0.data_source_2,
            data_immediate        => source_0.data_immediate,
            select_function       => select_function,
            destination           => destination.address_pointer
        );

    destination.control_mem        <= source_0.control_mem;
    destination.control_wb         <= source_0.control_wb;
    destination.data_source_2      <= source_0.data_source_2;
    destination.select_destination <= source_0.select_destination;

end architecture;
