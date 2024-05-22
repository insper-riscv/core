library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

library WORK;

package GENERICS is

    type t_std_ulogic_array is array(natural range <>) of std_ulogic_vector;

    function reverse_vector (l: in std_ulogic_vector) return std_ulogic_vector;
    function reduce_or  (l : std_ulogic_vector) return std_ulogic;
    function reduce_and (l : std_ulogic_vector) return std_ulogic;
    function is_equal (l : std_ulogic_vector; r : std_ulogic_vector) return std_ulogic;
    function is_equal_dynamic (l : std_ulogic_vector; r : std_ulogic_vector) return std_ulogic;

end package;

package body GENERICS is

    function reverse_vector (l: in std_ulogic_vector) return std_ulogic_vector is
        variable result : std_ulogic_vector(l'range);
        alias auxiliar  : std_ulogic_vector(l'reverse_range) is l;
    begin
        for i in auxiliar'range loop
            result(i) := auxiliar(i);
        end loop;
        return result;
    end function;

    function reduce_or (l : std_ulogic_vector) return std_ulogic is
        constant mid : integer := (l'high + l'low) / 2;
    begin
        if l'length = 1 then
            return l(l'low);
        elsif l'length = 2 then
            return l(l'low) OR l(l'high);
        elsif l'ascending then
            return reduce_or(l((mid + 1) to l'high)) OR reduce_or(l(l'low to mid));
        else
            return reduce_or(l(l'high downto (mid + 1))) OR reduce_or(l(mid downto l'low));
        end if;
    end function;

    function reduce_and (l : std_ulogic_vector) return std_ulogic is
        constant mid : integer := (l'high + l'low) / 2;
    begin
        if l'length = 1 then
            return l(l'low);
        elsif l'length = 2 then
            return l(l'low) AND l(l'high);
        elsif l'ascending then
            return reduce_and(l((mid + 1) to l'high)) AND reduce_and(l(l'low to mid));
        else
            return reduce_and(l(l'high downto (mid + 1))) AND reduce_and(l(mid downto l'low));
        end if;
    end function;

    function is_equal (l : std_ulogic_vector; r : std_ulogic_vector) return std_ulogic is
        variable base : std_ulogic_vector(r'range) := r;
        variable result : std_ulogic_vector(r'range);
    begin
        if r'ascending then
            base := reverse_vector(r);
        end if;

        for i in l'reverse_range loop
            if base(base'low + l'left - i) = '1' then
                result(i) := l(i);
            else
                result(i) := NOT(l(i));
            end if;
        end loop;

        return reduce_and(result);
    end function;

    function is_equal_dynamic (l : std_ulogic_vector; r : std_ulogic_vector) return std_ulogic is
    begin
        return reduce_and(l XNOR r);
    end function;

end package body;
