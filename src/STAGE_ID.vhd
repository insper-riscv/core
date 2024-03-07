library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;
use WORK.TOP_LEVEL_CONSTANTS.ALL;

entity STAGE_ID is

    port (
        clock               : in  std_logic;
        enable              : in  std_logic := '0';
        address_destination : in  std_logic_vector(XLEN_RANGE);
        address_source_1    : in  std_logic_vector(XLEN_RANGE);
        address_source_2    : in  std_logic_vector(XLEN_RANGE);
        data_destination    : in  std_logic_vector(XLEN_RANGE);
        instruction         : in  std_logic_vector(XLEN_RANGE);
        pc_out              : in  std_logic_vector(XLEN_RANGE);
        source_id           : out std_logic_vector(XLEN_RANGE);
        immediate_source    : out std_logic_vector(XLEN_RANGE);
        data_source_1       : out std_logic_vector(XLEN_RANGE);
        data_source_2       : out std_logic_vector(XLEN_RANGE)
    );

end entity;

architecture RTL of STAGE_ID is

    -- No signals

begin

    MODULE_BANK_IMM : entity WORK.MODULE_BANK_IMM
        port map (
        clock               => clock,              
        enable              => enable,             
        address_destination => address_destination,
        address_source_1    => address_source_1,   
        address_source_2    => address_source_2,   
        data_destination    => data_destination,   
        instruction         => instruction,        
        pc_out              => pc_out,             
        source_id           => source_id,          
        immediate_source    => immediate_source,   
        data_source_1       => data_source_1,      
        data_source_2       => data_source_2      
    );

end architecture;
