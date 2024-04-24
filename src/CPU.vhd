library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package CPU is

    generic (
        DATA_WIDTH              : natural := WORK.RV32I.XLEN;
        INSTRUCTION_WIDTH       : natural := WORK.RV32I.INSTRUCTION_WIDTH;
        OPCODE_WIDTH            : natural := WORK.RV32I.OPCODE_WIDTH;
        REGISTER_ADDRESS_WIDTH  : natural := 5;
        EXECUTION_CONTROL_WIDTH : natural := 4
    );

    subtype DATA_RANGE              is natural range (DATA_WIDTH              - 1) downto 0;
    subtype INSTRUCTION_RANGE       is natural range (INSTRUCTION_WIDTH       - 1) downto 0;
    subtype OPCODE_RANGE            is natural range (OPCODE_WIDTH            - 1) downto 0;
    subtype REGISTER_ADDRESS_RANGE  is natural range (REGISTER_ADDRESS_WIDTH  - 1) downto 0;
    subtype FUNCTION_RANGE          is natural range (EXECUTION_CONTROL_WIDTH - 1) downto 0;

    subtype t_DATA        is std_logic_vector(DATA_RANGE);
    subtype t_INSTRUCTION is std_logic_vector(INSTRUCTION_RANGE);
    subtype t_OPCODE      is std_logic_vector(OPCODE_RANGE);
    subtype t_REGISTER    is std_logic_vector(REGISTER_ADDRESS_RANGE);
    subtype t_FUNCTION    is std_logic_vector(FUNCTION_RANGE);

    type t_CONTROL_IF is record
        enable_stall  : std_logic;
        enable_flush  : std_logic;
        enable_jump   : std_logic;
        select_source : std_logic;
    end record;

    type t_CONTROL_ID is record
        select_jump     : std_logic;
        enable_jump     : std_logic;
        enable_flush_id : std_logic;
        enable_flux_ex  : std_logic;
    end record;

    type t_CONTROL_EX is record
        select_source_1  : std_logic_vector(1 downto 0);
        select_source_2  : std_logic_vector(1 downto 0);
        select_operation : std_logic_vector(1 downto 0);
    end record;

    type t_CONTROL_MEM is record
        enable_read  : std_logic;
        enable_write : std_logic;
    end record;

    type t_CONTROL_WB is record
        enable_destination : std_logic;
        select_destination : std_logic;
    end record;

    type t_SIGNALS_IF_ID is record
        address_program  : t_DATA;
        data_instruction : t_DATA;
    end record;

    type t_SIGNALS_ID_EX is record
        control_ex         : t_CONTROL_EX;
        control_mem        : t_CONTROL_MEM;
        control_wb         : t_CONTROL_WB;
        address_program    : t_DATA;
        data_source_1      : t_DATA;
        data_source_2      : t_DATA;
        data_immediate     : t_DATA;
        funct_7            : WORK.RV32I.t_FUNCT7;
        funct_3            : WORK.RV32I.t_FUNCT3;
        opcode             : WORK.RV32I.t_OPCODE;
        select_destination : t_REGISTER;
        select_source_1    : t_REGISTER;
        select_source_2    : t_REGISTER;
    end record;

    type t_SIGNALS_MEM_WB is record
        control_wb         : t_CONTROL_WB;
        data_memory        : t_DATA;
        data_destination   : t_DATA;
        select_destination : t_REGISTER;
    end record;

    type t_SIGNALS_EX_MEM is record
        control_mem        : t_CONTROL_MEM;
        control_wb         : t_CONTROL_WB;
        address_pointer    : t_DATA;
        data_source_2      : t_DATA;
        select_destination : t_REGISTER;
        funct_3            : WORK.RV32I.t_FUNCT3;
    end record;

    constant NULL_CONTROL_IF : t_CONTROL_IF := (
        enable_stall  => '0',
        enable_flush  => '0',
        enable_jump   => '0',
        select_source => '0'
    );

    constant NULL_CONTROL_ID : t_CONTROL_ID := (
        select_jump     => '0',
        enable_jump     => '0',
        enable_flush_id => '0',
        enable_flux_ex  => '0'
    );

    constant NULL_CONTROL_EX : t_CONTROL_EX := (
        select_source_1  => (others => '0'),
        select_source_2  => (others => '0'),
        select_operation => (others => '0')
    );

    constant NULL_CONTROL_MEM : t_CONTROL_MEM := (
        enable_read  => '0',
        enable_write => '0'
    );

    constant NULL_CONTROL_WB : t_CONTROL_WB := (
        enable_destination => '0',
        select_destination => '1'
    );

    constant NULL_SIGNALS_IF_ID : t_SIGNALS_IF_ID := (
        address_program  => (others => '0'),
        data_instruction => (others => '0')
    );

    constant NULL_SIGNALS_ID_EX : t_SIGNALS_ID_EX := (
        control_ex         => NULL_CONTROL_EX,
        control_mem        => NULL_CONTROL_MEM,
        control_wb         => NULL_CONTROL_WB,
        address_program    => (others => '0'),
        data_source_1      => (others => '0'),
        data_source_2      => (others => '0'),
        data_immediate     => (others => '0'),
        funct_7            => (others => '0'),
        funct_3            => (others => '0'),
        opcode             => (others => '0'),
        select_destination => (others => '0'),
        select_source_1    => (others => '0'),
        select_source_2    => (others => '0')
    );

    constant NULL_SIGNALS_EX_MEM : t_SIGNALS_EX_MEM := (
        control_mem        => NULL_CONTROL_MEM,
        control_wb         => NULL_CONTROL_WB,
        address_pointer    => (others => '0'),
        data_source_2      => (others => '0'),
        select_destination => (others => '0'),
        funct_3            => (others => '0')
    );

    constant NULL_SIGNALS_MEM_WB : t_SIGNALS_MEM_WB := (
        control_wb         => NULL_CONTROL_WB,
        data_memory        => (others => '0'),
        data_destination   => (others => '0'),
        select_destination => (others => '0')
    );

end package;
