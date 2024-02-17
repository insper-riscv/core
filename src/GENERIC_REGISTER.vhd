library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity GENERIC_REGISTER is

    generic (
        DATA_WIDTH : natural
    );

    port (
        clock   : in  std_logic;
        clear   : in  std_logic;
        enable  : in  std_logic;
        source  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
        destiny : out std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0')
    );

end entity;

architecture RTL of GENERIC_REGISTER is

    -- No signals

begin

    UPDATE : process(clear, clock, enable)
    begin
        if (rising_edge(clock)) then
            SET_RESET : if (enable = '1') then
                destiny <= source;
            elsif (clear = '1') then
                destiny <= (others => '0');
            end if;
        end if;
    end process;

end architecture;
