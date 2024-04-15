library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

entity MODULE_EXECUTION_UNIT_CONTROLLER is

    generic (
        DATA_WIDTH : natural := XLEN
    );

    port (
        opcode                 : in  t_OPCODE;
        function_3             : in  t_FUNCTION3;
        function_7             : in  t_FUNCTION7;
        destination            : out std_logic_vector(4 downto 0)
    );

end entity;

architecture RV32I of MODULE_EXECUTION_UNIT_CONTROLLER is

begin

    ALU_CONTROLLER : entity WORK.RV32I_ALU_CONTROLLER
        port map (
            opcode      => opcode,
            function_3  => function_3,
            function_7  => function_7,
            destination => destination
        );

end architecture;
