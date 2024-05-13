library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

package GENERICS is

    type t_std_logic_array is array(natural range <>) of std_logic_vector;

    function reduce_or  (l : std_logic_vector) return std_logic;
    function reduce_and (l : std_logic_vector) return std_logic;
    function is_equal (l : std_logic_vector; r : std_logic_vector) return std_logic;
    function reverse_vector (l: in std_logic_vector) return std_logic_vector;

end package;

package body GENERICS is

    function reduce_or (l : std_logic_vector) return std_logic is
        variable result : std_logic := '0';
    begin
        for i in l'reverse_range loop
            result := result OR l(i);
        end loop;
        return result;
    end function;

    function reduce_and (l : std_logic_vector) return std_logic is
        variable result : std_logic := '1';
    begin
        for i in l'reverse_range loop
            result := result AND l(i);
        end loop;
        return result;
    end function;

    function is_equal (l : std_logic_vector; r : std_logic_vector) return std_logic is
        variable base   : std_logic_vector(r'range) := r;
        variable result : std_logic := '1';
    begin
        if r'ascending then
            base := reverse_vector(r);
        end if;

        for i in l'reverse_range loop
            if base(base'low + l'left - i) = '1' then
                result := result AND l(i);
            else
                result := result AND NOT(l(i));
            end if;
        end loop;
        return result;
    end function;

    function reverse_vector (l: in std_logic_vector) return std_logic_vector is
        variable result: std_logic_vector(l'range);
        alias auxiliar: std_logic_vector(l'reverse_range) is l;
    begin
        for i in auxiliar'range loop
            result(i) := auxiliar(i);
        end loop;
        return result;
    end function;

end package body;
