library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity RV32I_FORWARDING_UNIT_ALU is

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
        mux_control_1            : out  std_logic_vector(1 downto 0);
        mux_control_2            : out  std_logic_vector(1 downto 0)
    );

end entity;

architecture RTL of RV32I_FORWARDING_UNIT_ALU is

    -- No signals

begin

    
    process(register_source_1, register_source_2, register_destination_mem, register_destination_wb)
    begin
        MUX_CONTROLLER_1 : if (enable_write_mem = '1' and register_source_1 = register_destination_mem) then
            mux_control_1 <= "10";
        elsif (enable_write_mem = '1' and register_source_1 = register_destination_wb) then
            mux_control_1 <= "01";
        else
            mux_control_1 <= "00";
        end if;
        MUX_CONTROLLER_2 : if (enable_write_mem = '1' and register_source_2 = register_destination_mem) then
            mux_control_2 <= "10";
        elsif (enable_write_mem = '1' and register_source_2 = register_destination_wb) then
            mux_control_2 <= "01";
        else
            mux_control_2 <= "00";
        end if;
    end process;

end architecture;
