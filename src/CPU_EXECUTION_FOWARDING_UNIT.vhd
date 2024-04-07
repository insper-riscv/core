library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity CPU_EXECUTION_FOWARDING_UNIT is

    generic (
        ADDRESS_WIDTH : natural := 5
    );

    port (
        register_source_1        : in  t_REGISTER;
        register_source_2        : in  t_REGISTER;
        register_destination_mem : in  t_REGISTER;
        enable_write_mem         : in  std_logic;
        register_destination_wb  : in  t_REGISTER;
        enable_write_wb          : in  std_logic;
        mux_control_1            : out  std_logic_vector(1 downto 0) := (others => '0');
        mux_control_2            : out  std_logic_vector(1 downto 0) := (others => '0')
    );

end entity;

architecture RTL of CPU_EXECUTION_FOWARDING_UNIT is

    -- No signals

begin

    
    mux_control_1 <= "10" when (enable_write_mem = '1' and register_source_1 = register_destination_mem and register_destination_mem /= "00000") else
                     "01" when (enable_write_wb = '1' and register_source_1 = register_destination_wb and register_destination_wb /= "00000") else
                     "00";

    mux_control_2 <= "10" when (enable_write_mem = '1' and register_source_2 = register_destination_mem and register_destination_mem /= "00000") else
                     "01" when (enable_write_wb = '1' and register_source_2 = register_destination_wb and register_destination_wb /= "00000") else
                     "00";

end architecture;
