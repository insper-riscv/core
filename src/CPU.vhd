library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package CPU is

    constant REGISTER_ADDERESS_WIDTH : natural := WORK.RV32I.REGISTER_WIDTH;

    subtype t_DATA     is WORK.RV32I.t_DATA;
    subtype t_REGISTER is WORK.RV32I.t_REGISTER;

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
        select_destination => (others => '0')
    );

    constant NULL_SIGNALS_MEM_WB : t_SIGNALS_MEM_WB := (
        control_wb         => NULL_CONTROL_WB,
        data_memory        => (others => '0'),
        data_destination   => (others => '0'),
        select_destination => (others => '0')
    );

    component CPU_TOP_LEVEL
        port (
            clock           : in  std_logic := '0';
            enable          : in  std_logic := '1';
            data_program    : in  CPU.t_DATA := (others => '0');
            data_memory_in  : in  CPU.t_DATA := (others => '0');
            memory_read     : out std_logic;
            memory_write    : out std_logic;
            data_memory_out : out CPU.t_DATA;
            address_program : out CPU.t_DATA;
            address_memory  : out CPU.t_DATA
        );
    end component;

    component CPU_STAGE_IF
        port (
            clock           : in  std_logic;
            enable          : in  std_logic;
            source          : in  t_CONTROL_IF;
            address_jump    : in  t_DATA;
            address_program : out t_DATA
        );
    end component;

    component CPU_STAGE_ID
        generic (
            GENERATE_REGISTERS : boolean := TRUE
        );
        port (
            clock              : in  std_logic;
            clear              : in  std_logic;
            enable             : in  std_logic;
            enable_destination : in  std_logic;
            source             : in  t_SIGNALS_IF_ID;
            select_destination : in  t_REGISTER;
            data_destination   : in  t_DATA;
            address_jump       : out t_DATA;
            control_if         : out t_CONTROL_IF;
            signals_ex         : out t_SIGNALS_ID_EX
        );
    end component;

    component CPU_STAGE_EX
        generic (
            GENERATE_REGISTERS : boolean := TRUE
        );
        port (
            clock                   : in  std_logic;
            clear                   : in  std_logic;
            enable                  : in  std_logic;
            selector_forwarding_mem : in  t_REGISTER;
            enable_mem              : in  std_logic;
            selector_forwarding_wb  : in  t_REGISTER;
            enable_wb               : in  std_logic;
            forwarding_mem_source   : in  t_DATA;
            forwarding_wb_source    : in  t_DATA;
            source                  : in  t_SIGNALS_ID_EX;
            destination             : out t_SIGNALS_EX_MEM
        );
    end component;

    component CPU_STAGE_MEM
        generic (
            GENERATE_REGISTERS : boolean := TRUE
        );
        port (
            clock          : in  std_logic;
            clear          : in  std_logic;
            enable         : in  std_logic;
            source         : in  t_SIGNALS_EX_MEM;
            control_memory : out t_CONTROL_MEM;
            address_memory : out t_DATA;
            data_memory    : out t_DATA;
            destination    : out t_SIGNALS_MEM_WB
        );
    end component;

    component CPU_STAGE_WB
        generic (
            GENERATE_REGISTERS : boolean := TRUE
        );
        port (
            clock              : in  std_logic;
            clear              : in  std_logic;
            enable             : in  std_logic;
            source             : in  t_SIGNALS_MEM_WB;
            enable_destination : out std_logic;
            select_destination : out t_REGISTER;
            destination        : out t_DATA
        );
    end component;

    component CPU_EXECUTION_FOWARDING_UNIT
        generic (
            ADDRESS_WIDTH : natural := REGISTER_ADDERESS_WIDTH
        );
        port (
            stage_ex_select_source_1     : in  t_REGISTER;
            stage_ex_select_source_2     : in  t_REGISTER;
            stage_mem_enable_destination : in  t_REGISTER;
            stage_mem_select_destination : in  std_logic;
            stage_wb_enable_destination  : in  t_REGISTER;
            stage_wb_select_destination  : in  std_logic;
            stage_id_select_source_1     : out std_logic_vector(1 downto 0);
            stage_id_select_source_2     : out std_logic_vector(1 downto 0)
        );
    end component;

end package;