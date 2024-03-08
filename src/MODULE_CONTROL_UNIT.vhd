library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_CONTROL_UNIT is

    generic (
        DATA_WIDTH    : natural := XLEN;
        ADDRESS_WIDTH : natural := 5
    );

    port (
        instruction      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        pc_out           : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_1    : in std_logic_vector((DATA_WIDTH - 1) downto 0);
        source_id        : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        immediate_source : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        control_if       : out t_IF_SIGNALS;
        control_ex       : out t_EX_SIGNALS;
        control_mem      : out t_MEM_SIGNALS;
        control_wb       : out t_WB_SIGNALS
    );

end entity;

architecture RTL of MODULE_CONTROL_UNIT is

        signal immediate_tmp : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal adder_out_1   : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal adder_out_2   : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal control_id    : t_ID_SIGNALS;

begin

    CONTROL_UNIT : entity WORK.RV32I_INSTRUCTION_DECODER
        port map (
            instruction => instruction,
            control_if  => control_if,
            control_id  => control_id,
            control_ex  => control_ex,
            control_mem => control_mem,
            control_wb  => control_wb,
            immediate   => immediate_tmp
        );

    ADDER_1 : entity WORK.GENERIC_ADDER
        port map (
            source_1 => pc_out,
            source_2 => immediate_tmp,
            destination => adder_out_1
        );

    ADDER_2 : entity WORK.GENERIC_ADDER
        port map (
            source_1 => immediate_tmp,
            source_2 => data_source_1,
            destination => adder_out_2
        );

    MUX : entity WORK.GENERIC_MUX_2X1
        port map (
            source_1 => adder_out_1,
            source_2 => adder_out_2,
            selector => control_id.select_jump,
            destination => source_id
        );   

    immediate_source <= immediate_tmp;

end architecture;
