library IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.TOP_LEVEL_CONSTANTS.ALL;

entity GENERIC_COUNTER is

    generic (
        DEFAULT_OVERFLOW : natural := CLOCK_FREQUENCY  -- 1 second
    );

    port (
        clock  : in  std_logic;
        clear  : in  std_logic;
        set    : in  std_logic;
        source : in  std_logic_vector(4 downto 0);
        state  : out std_logic
    );

end entity;

architecture RTL of GENERIC_COUNTER is

    -- No signals

begin

    COUNTER : process(clock, set)
        variable pow      : integer;
        variable overflow : std_logic_vector(31 downto 0) := std_logic_vector(to_unsigned(DEFAULT_OVERFLOW, 32));
        variable count    : std_logic_vector(31 downto 0) := (others => '0');
    begin
        if rising_edge(clock) then
            count := std_logic_vector(unsigned(count) + 1);

            SET_OVERFLOW : if (set = '1') then
                pow := to_integer(unsigned(source(4 downto 0)));
                overflow := std_logic_vector(to_unsigned(2 ** pow, 32));
            end if;

            SET_STATE : if (count = overflow) then
                state <= '1';
                count := (others => '0');
            end if;

            CLEAR_STATE : if (clear = '1') then
                state <= '0';
            end if;
        end if;
    end process;

end architecture;
