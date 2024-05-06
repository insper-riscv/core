library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.MATH_REAL.ALL;

library WORK;

entity RV32I_ALU_SHIFTER is

    generic (
        DATA_WIDTH  : natural := 8;
        SHAMT_WIDTH : natural := natural(ceil(log2(real(WORK.RV32I.XLEN))))
    );

    port (
        select_function : in  std_logic_vector(3 downto 0);
        shamt           : in  std_logic_vector((SHAMT_WIDTH - 1) downto 0);
        source          : in  std_logic_vector((DATA_WIDTH  - 1) downto 0);
        destination     : out std_logic_vector((DATA_WIDTH  - 1) downto 0)
    );

end entity;

architecture RTL of RV32I_ALU_SHIFTER is

    type t_file is array (natural range <>) of std_logic_vector(DATA_WIDTH - 1 downto 0);
    signal data                 : t_file(0 to (DATA_WIDTH - 1));

    signal msb                  : std_logic := '0';
    signal msb_vector           : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal source_auxiliar      : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal reversed_source      : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal destination_auxiliar : std_logic_vector((DATA_WIDTH - 1) downto 0);
    signal reversed_destination : std_logic_vector((DATA_WIDTH - 1) downto 0);

    function reverse_vector (
        in_vec: in std_logic_vector
    ) return std_logic_vector is
        variable out_vec: std_logic_vector(in_vec'RANGE);
        alias auxiliar: std_logic_vector(in_vec'REVERSE_RANGE) is in_vec;
    begin
        for i in auxiliar'RANGE loop
            out_vec(i) := auxiliar(i);
        end loop;
        return out_vec;
    end function;

begin

    msb_vector <=   (others => source(DATA_WIDTH - 1)) when (select_function(3) = '1') else
                    (others => '0');

    reversed_source <= reverse_vector(source);

    source_auxiliar <=  reversed_source when (select_function(2) = '1') else
                        source;

    BUILD : for i in 0 to (DATA_WIDTH - 1) generate
        BUILD_ROW : if (i = 0) generate
            data(i) <= source_auxiliar;
        elsif (i = DATA_WIDTH - 1) generate
            data(i) <= msb_vector;
        else generate
            data(i) <= source_auxiliar((DATA_WIDTH - i - 1) downto 0) & msb_vector((i - 1) downto 0);
        end generate;
    end generate;

    destination_auxiliar <= data(to_integer(unsigned(shamt)));

    reversed_destination <= reverse_vector(destination_auxiliar);

    destination <=  reversed_destination when (select_function(2) = '1') else
                    destination_auxiliar;

end architecture;
