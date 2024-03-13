library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity MODULE_ALU_CONTROLLER is

    generic (
        DATA_WIDTH : natural := XLEN
    );
  
    port (
        opcode                 : in t_OPCODE;
        function_3             : in t_FUNCTION;
        function_7             : in std_logic_vector(6 downto 0);
        destination            : out std_logic_vector(3 downto 0)
    );

end entity;

architecture RTL of MODULE_ALU_CONTROLLER is

begin

    ALU_CONTROLLER : entity WORK.RV32I_ALU_CONTROLLER
        port map (
            opcode      => opcode,
            function_3  => function_3,
            function_7  => function_7,
            destination => destination
        );
end architecture;
