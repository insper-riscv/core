library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_ID is

    port (
        clock                : in  std_logic;
        source               : in t_IF_ID_SIGNALS;
        enable               : in std_logic;
        address_destination  : in std_logic_vector(4 downto 0);
        data_destination     : in std_logic_vector(XLEN_RANGE);
        control_if           : out t_IF_SIGNALS;
        destination          : out t_ID_EX_SIGNALS
    );

end entity;

architecture RTL of STAGE_ID is

    signal data_source_1 : std_logic_vector(XLEN_RANGE);

begin

    MODULE_REGISTER_FILE : entity WORK.MODULE_REGISTER_FILE
        port map (
        clock               => clock,              
        enable              => enable,             
        address_destination => address_destination,
        data_destination    => data_destination,   
        instruction         => source.instruction,          
        data_source_1       => data_source_1,      
        data_source_2       => destination.source_2   
    );

    MODULE_CONTROL_UNIT : entity WORK.MODULE_CONTROL_UNIT
        port map (
            instruction      => source.instruction,
            pc_out           => source.pc,
            data_source_1    => data_source_1,
            immediate_source => destination.immediate,
            control_if       => control_if,
            control_ex       => destination.ex_signals,
            control_mem      => destination.mem_signals,
            control_wb       => destination.wb_signals
    );

    destination.source_1 <= data_source_1;

end architecture;
