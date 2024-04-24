library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_EXECUTION_UNIT_CONTROLLER is

    generic (
        OPCODE_WIDTH : natural := WORK.RV32I.OPCODE_WIDTH;
        DATA_WIDTH   : natural := 4
    );

    port (
        opcode      : in  std_logic_vector((OPCODE_WIDTH - 1) downto 0);
        funct_3     : in  std_logic_vector(2 downto 0);
        funct_7     : in  std_logic_vector(6 downto 0);
        destination : out std_logic_vector((DATA_WIDTH - 1) downto 0)
    );

end entity;

architecture RV32I of MODULE_EXECUTION_UNIT_CONTROLLER is

begin

    ALU_CONTROLLER : entity WORK.RV32I_ALU_CONTROLLER
        port map (
            opcode      => opcode,
            funct3      => funct_3,
            funct7      => funct_7,
            destination => destination
        );

end architecture;
