library IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity GENERIC_COUNTER is

    generic (
        DEFAULT_OVERFLOW : natural := 2**10
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

    signal overflow : std_logic_vector(31 downto 0) := std_logic_vector(to_unsigned(DEFAULT_OVERFLOW, 32));
    signal count    : std_logic_vector(31 downto 0) := (others => '0');

begin

    UPDATE_OVERFLOW : process(clock, update)
    begin
        if rising_edge(clock) AND (update = '1') then
            for i in 0 to 31 loop
                if (i = to_integer(unsigned(source))) then
                    overflow(i) <= '1';
                else
                    overflow(i) <= '0';
                end if;
            end loop;
        end if;
    end process;

    COUNTER : process(clock, update, count, overflow)
    begin
        if rising_edge(clock) then
            if (update = '1') then
                count(31 downto 1) <= (others => '0');
                count(0) <= '1';
                state <= '0';
            else
                CLEAR_STATE : if (clear = '1') then
                    state <= '0';
                end if;

                UPDATE_STATE : if (count = overflow) then
                    count(31 downto 1) <= (others => '0');
                    count(0) <= '1';
                    state <= '1';
                else
                    count <= std_logic_vector(unsigned(count) + 1);
                end if;
            end if;
        end if;
    end process;

end architecture;
