library IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_COUNTER is

    generic (
        DEFAULT_OVERFLOW : natural := CLOCK_FREQUENCY  -- 1 second
    );

    port (
        clock  : in  std_logic;
        clear  : in  std_logic;
        update : in  std_logic;
        source : in  std_logic_vector(4 downto 0);
        state  : out std_logic := '0'
    );

end entity;

architecture RTL of GENERIC_COUNTER is

    -- No signals

begin

    COUNTER : process(clock, update)
        variable selector : integer;
        variable overflow : std_logic_vector(31 downto 0) := std_logic_vector(to_unsigned(DEFAULT_OVERFLOW, 32));
        variable count    : std_logic_vector(31 downto 0) := (others => '0');
    begin
        if rising_edge(clock) then
            count := std_logic_vector(unsigned(count) + 1);

            UPDATE_OVERFLOW : if (update = '1') then
                selector := to_integer(unsigned(source(4 downto 0)));
                overflow := (others =>'0');

                for i in 0 to 31 loop
                    if (i = selector) then
                        overflow(i) := '1';
                    end if;
                end loop;
            end if;

            UPDATE_STATE : if (count = overflow) then
                state <= '1';
                count := (others => '0');
            end if;

            CLEAR_STATE : if (clear = '1') then
                state <= '0';
            end if;
        end if;
    end process;

end architecture;
