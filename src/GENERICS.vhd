library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package GENERICS is

    generic (
        DATA_WIDTH : natural := 8
    );

    component GENERIC_ADDER
        generic (
            DATA_WIDTH       : natural := DATA_WIDTH;
            DEFAULT_SOURCE_2 : integer := 1
        );
        port (
            source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            source_2    : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := std_logic_vector(to_signed(DEFAULT_SOURCE_2, DATA_WIDTH));
            destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component GENERIC_COMPARATOR
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            source_1      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            source_2      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            flag_equal    : out std_logic;
            flag_less     : out std_logic;
            flag_greather : out std_logic
        );
    end component;

    component GENERIC_DEBOUNCE
        Port (
            clock  : in  std_logic;
            clear  : in  std_logic := '0';
            source : in  std_logic;
            state  : out std_logic
        );
    end component;

    component GENERIC_EDGE_DETECTOR
        Port (
            clock  : in  std_logic;
            source : in  std_logic;
            pulse  : out std_logic
        );
    end component;

    component GENERIC_FLIP_FLOP
        port (
            clock  : in  std_logic;
            clear  : in  std_logic;
            enable : in  std_logic;
            source : in  std_logic;
            state  : out std_logic := '0'
        );
    end component;

    component GENERIC_MUX_2X1
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            source_2    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            selector    : in  std_logic;
            destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component GENERIC_MUX_4X1
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            source_1     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
            source_2     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
            source_3     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
            source_4     : in  std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0');
            selector     : in  std_logic_vector(1 downto 0);
            destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component GENERIC_RAM
        generic (
            DATA_WIDTH        : natural := DATA_WIDTH;
            ADDRESS_WIDTH     : natural := 8;
            ADDRESSABLE_WIDTH : natural := 7
        );
        port (
            clock        : in  std_logic;
            enable       : in  std_logic;
            enable_read  : in  std_logic;
            enable_write : in  std_logic;
            address      : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
            source       : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component GENERIC_REGISTER
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            clock       : in  std_logic;
            clear       : in  std_logic;
            enable      : in  std_logic;
            source      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            destination : out std_logic_vector((DATA_WIDTH - 1) downto 0) := (others => '0')
        );
    end component;

    component GENERIC_ROM
        generic (
            DATA_WIDTH        : natural := 8;
            ADDRESS_WIDTH     : natural := 8;
            ADDRESSABLE_WIDTH : natural := 7
        );
        port (
            address     : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
            destination : out std_logic_vector((DATA_WIDTH - 1) downto 0) 
        );
    end component;

    component GENERIC_SIGNAL_EXTENDER
        generic (
            SOURCE_WIDTH      : natural := 4;
            DESTINATION_WIDTH : natural := DATA_WIDTH
        );
        port (
            source          : in  std_logic_vector((SOURCE_WIDTH - 1) downto 0);
            enable_unsigned : in  std_logic := '0';
            destination     : out std_logic_vector((DESTINATION_WIDTH - 1) downto 0)
        );
    end component;

end package;
