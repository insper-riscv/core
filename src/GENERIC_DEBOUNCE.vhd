library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

entity GENERIC_DEBOUNCE is

    Port (
        clock  : in  std_ulogic;
        clear  : in  std_ulogic := '0';
        source : in  std_ulogic;
        state  : out std_ulogic
    );

end entity;

architecture RTL of GENERIC_DEBOUNCE is

    signal edge_detector_pulse_state_register_clock : std_ulogic;
    signal not_source                               : std_ulogic;

begin

    EDGE_DETECTOR : entity WORK.GENERIC_EDGE_DETECTOR(RISING_DETECTOR)
        port map (
            clock  => clock,
            source => not_source,
            pulse  => edge_detector_pulse_state_register_clock
        );

    STATE_REGISTER: entity WORK.GENERIC_FLIP_FLOP
        port map (
            clock  => edge_detector_pulse_state_register_clock,
            enable => '1',
            clear  => clear,
            source => '1',
            state  => state
        );

    not_source <= not source;

end architecture;
