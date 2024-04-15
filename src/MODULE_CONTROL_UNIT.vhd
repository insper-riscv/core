library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity MODULE_CONTROL_UNIT is

    generic (
        DATA_WIDTH    : natural := XLEN
    );

    port (
        instruction      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        address_program  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        data_source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        jump_address     : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        immediate_source : out std_logic_vector((DATA_WIDTH - 1) downto 0);
        control_if       : out t_CONTROL_IF;
        control_ex       : out t_CONTROL_EX;
        control_mem      : out t_CONTROL_MEM;
        control_wb       : out t_CONTROL_WB
    );

end entity;

architecture RV32I of MODULE_CONTROL_UNIT is

        package G is new G.GENERICS
            generic map (
                DATA_WIDTH => 32
            );

        signal immediate_tmp : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal adder_out_1   : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal adder_out_2   : std_logic_vector((DATA_WIDTH - 1) downto 0);
        signal control_id    : t_CONTROL_ID;

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

    ADDER_1 : entity G.GENERIC_ADDER
        port map (
            source_1    => address_program,
            source_2    => immediate_tmp,
            destination => adder_out_1
        );

    ADDER_2 : entity G.GENERIC_ADDER
        port map (
            source_1    => immediate_tmp,
            source_2    => data_source_1,
            destination => adder_out_2
        );

    MUX : entity G.GENERIC_MUX_2X1
        port map (
            source_1    => adder_out_1,
            source_2    => adder_out_2,
            selector    => control_id.select_jump,
            destination => jump_address
        );   

    immediate_source <= immediate_tmp;

end architecture;
