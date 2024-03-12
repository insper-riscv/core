library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity TOP_LEVEL is

    port (
        CLOCK       : in  std_logic;
        SW          : in std_logic_vector(3 downto 0) := (others => '0');
        LED         : out std_logic_vector(7 downto 0) := (others => '0');
        destination : out std_logic_vector(XLEN_RANGE)
    );

end entity;

architecture RTL of TOP_LEVEL is

        signal control_if            : t_IF_SIGNALS;
        signal control_if_id         : t_IF_ID_SIGNALS;
        signal control_id_ex         : t_ID_EX_SIGNALS;
        signal control_ex_mem        : t_EX_MEM_SIGNALS;
        signal control_mem_wb        : t_MEM_WB_SIGNALS;
        signal enable_reg_file_write : std_logic;
        signal address_destination   : std_logic_vector(4 downto 0);
        signal data_destination      : std_logic_vector(XLEN_RANGE);


begin

    LED(0) <= SW(1);

    STAGE_IF : entity WORK.STAGE_IF
        port map (
            clock       => CLOCK,
            source      => control_if,
            destination => control_if_id
        );

    STAGE_ID : entity WORK.STAGE_ID
        port map (
            clock               => CLOCK,
            source              => control_if_id,
            enable              => enable_reg_file_write,
            address_destination => address_destination,
            data_destination    => data_destination,
            control_if          => control_if,
            destination         => control_id_ex
        );

    STAGE_EX : entity WORK.STAGE_EX
        port map (
            source      => control_id_ex,
            destination => control_ex_mem
        );

    STAGE_MEM : entity WORK.STAGE_MEM
        port map (
            clock       => CLOCK,
            source      => control_ex_mem,
            destination => control_mem_wb
        );

    STAGE_WB : entity WORK.STAGE_WB
        port map (
            source           => control_mem_wb,
            enable           => enable_reg_file_write,
            address_register => address_destination,
            destination      => data_destination

        );

    destination <= data_destination;

end architecture;
