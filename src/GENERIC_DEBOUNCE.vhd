library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity GENERIC_DEBOUNCE is

    Port (
        clock  : in  std_logic;
        clear  : in  std_logic := '0';
        source : in  std_logic;
        state  : out std_logic
    );

end entity;

architecture RTL of GENERIC_DEBOUNCE is

    signal edge_detector_pulse_state_register_clock : std_logic;

begin

    EDGE_DETECTOR : entity WORK.EDGE_DETECTOR(RISING_DETECTOR)
        port map (
            clock  => clock,
            source => not(source),
            pulse  => edge_detector_pulse_state_register_clock
        );

    STATE_REGISTER: entity WORK.GENERIC_FLIP_FLOP
        port map (
            clock   => edge_detector_pulse_state_register_clock,
            enable  => '1',
            clear   => clear,
            source  => '1',
            destiny => state
        );

end architecture;
