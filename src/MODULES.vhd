library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

package MODULES is

    generic (
        DATA_WIDTH    : natural := WORK.CPU.t_DATA'length;
        ADDRESS_WIDTH : natural := DATA_WIDTH
    );

    component MODULE_CONTROL_UNIT
        generic (
            DATA_WIDTH    : natural := DATA_WIDTH;
            ADDRESS_WIDTH : natural := WORK.CPU.t_REGISTER'length
        );
        port (
            instruction      : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            address_program  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            data_source_1    : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            jump_address     : out std_logic_vector((DATA_WIDTH - 1) downto 0);
            immediate_source : out std_logic_vector((DATA_WIDTH - 1) downto 0);
            control_if       : out WORK.CPU.t_CONTROL_IF;
            control_ex       : out WORK.CPU.t_CONTROL_EX;
            control_mem      : out WORK.CPU.t_CONTROL_MEM;
            control_wb       : out WORK.CPU.t_CONTROL_WB
        );
    end component;

    component MODULE_EXECUTION_UNIT_CONTROLLER
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            opcode                 : in  WORK.RV32I.t_OPCODE;
            function_3             : in  WORK.RV32I.t_FUNCT3;
            function_7             : in  WORK.RV32I.t_FUNCT7;
            destination            : out std_logic_vector(4 downto 0)
        );
    end component;

    component MODULE_EXECUTION_UNIT
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            select_forward_1       : in  std_logic_vector(1 downto 0);
            select_forward_2       : in  std_logic_vector(1 downto 0);
            select_source_1        : in  std_logic_vector(1 downto 0);
            select_source_2        : in  std_logic_vector(1 downto 0);
            address_program        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            forwarding_mem_source  : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            forwarding_wb_source   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            data_source_1          : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            data_source_2          : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            data_immediate         : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            select_function        : in  std_logic_vector(4 downto 0);
            destination            : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component MODULE_PROGRAM_COUNTER
        generic (
            DATA_WIDTH : natural := DATA_WIDTH
        );
        port (
            clock        : in  std_logic;
            jump_address : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            selector     : in  std_logic;
            enable       : in  std_logic;
            destination  : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component MODULE_REGISTER_FILE
        generic (
            DATA_WIDTH    : natural := DATA_WIDTH;
            ADDRESS_WIDTH : natural := 5
        );
        port (
            clock              : in  std_logic;
            enable             : in  std_logic := '0';
            select_destination : in  std_logic_vector((ADDRESS_WIDTH - 1) downto 0);
            data_destination   : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            instruction        : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            data_source_1      : out std_logic_vector((DATA_WIDTH - 1) downto 0);
            data_source_2      : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

    component MODULE_WRITE_BACK
        generic (
            DATA_WIDTH  : natural := DATA_WIDTH
        );
        port (
            source_memory : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            source_ex     : in  std_logic_vector((DATA_WIDTH - 1) downto 0);
            selector      : in  std_logic;
            destination   : out std_logic_vector((DATA_WIDTH - 1) downto 0)
        );
    end component;

end package;
