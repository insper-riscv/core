library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

library WORK;

--! Para a topologia, um conjunto de registros foi criado para definir o fluxo de
--! dados em alto nível. Isso possibilita simplificar a implementação de pipelining
--! e manter o código limpo. A partir dos seguintes registros é possível declarar
--! todos os pontos de controle e de dados de todo o fluxo de execução da arquitetura.
--! Além disso, também são especificados valores que caracterizem o comportamento
--! ocioso da arquitetura.
package CPU is

    --generic (
    --    GENERIC_DATA_WIDTH              : natural := WORK.RV32I.XLEN;
    --    GENERIC_INSTRUCTION_WIDTH       : natural := WORK.RV32I.INSTRUCTION_WIDTH;
    --    GENERIC_OPCODE_WIDTH            : natural := WORK.RV32I.OPCODE_WIDTH;
    --    GENERIC_REGISTER_ADDRESS_WIDTH  : natural := 5;
    --    GENERIC_EXECUTION_CONTROL_WIDTH : natural := 4
    --);

    --! Largura do vetor de dados
    constant DATA_WIDTH              : natural := WORK.RV32I.XLEN;
    --! Largura do vetor de programa
    constant INSTRUCTION_WIDTH       : natural := WORK.RV32I.INSTRUCTION_WIDTH;
    --! Largura do vetor de Opcode
    constant OPCODE_WIDTH            : natural := WORK.RV32I.OPCODE_WIDTH;
    --! Largura do vetor de seleção de registrador
    constant REGISTER_ADDRESS_WIDTH  : natural := 5;
    --! Largura do vetor de seleção de função
    constant EXECUTION_CONTROL_WIDTH : natural := 4;
    
    --! Faixa do vetor de dados
    subtype DATA_RANGE              is natural range (DATA_WIDTH              - 1) downto 0;
    --! Faixa do vetor de programa
    subtype INSTRUCTION_RANGE       is natural range (INSTRUCTION_WIDTH       - 1) downto 0;
    --! Faixa do vetor de Opcode
    subtype OPCODE_RANGE            is natural range (OPCODE_WIDTH            - 1) downto 0;
    --! Faixa do vetor de seleção de registrador
    subtype REGISTER_ADDRESS_RANGE  is natural range (REGISTER_ADDRESS_WIDTH  - 1) downto 0;
    --! Faixa do vetor de seleção de função
    subtype FUNCTION_RANGE          is natural range (EXECUTION_CONTROL_WIDTH - 1) downto 0;

    --! Vetor de dados
    subtype t_DATA        is std_logic_vector(DATA_RANGE);
    --! Vetor de programa
    subtype t_PROGRAM     is std_logic_vector(INSTRUCTION_RANGE);
    --! Vetor de Opcode
    subtype t_OPCODE      is std_logic_vector(OPCODE_RANGE);
    --! Vetor de seleção de registrador
    subtype t_REGISTER    is std_logic_vector(REGISTER_ADDRESS_RANGE);
    --! Vetor de seleção de função
    subtype t_FUNCTION    is std_logic_vector(FUNCTION_RANGE);

    --! Pontos de controle do estágio Busca Instrução (Instruction Fetch)
    type t_CONTROL_IF is record
        --! Trava a contagem do programa
        enable_stall  : std_logic;
        --! Seleciona a origem do contador de programa
        select_source : std_logic;
    end record;

    --! Pontos de controle do estágio Decodifica Instrução (Instruction Decode)
    type t_CONTROL_ID is record
        --! Indica que é uma instrução do tipo `B`
        enable_branch : std_logic;
        --! Indica que é uma instrução `JALR`
        enable_jalr   : std_logic;
        --! Indica que é uma instrução do tipo `J`
        enable_jump   : std_logic;
        --! Seleciona um endereço de desvio
        select_jump   : std_logic;
    end record;

    --! Pontos de controle do estágio Executa (Execute)
    type t_CONTROL_EX is record
        --! Seleciona a fonte da entrada `source_1`
        select_source_1  : std_logic_vector(1 downto 0);
        --! Seleciona a fonte da entrada `source_2`
        select_source_2  : std_logic_vector(1 downto 0);
    end record;

    --! Pontos de controle do estágio Acessa a Memória (Memory Access)
    type t_CONTROL_MEM is record
        --! Habilita a leitura da memória
        enable_read  : std_logic;
        --! Habilita a escrina na memória
        enable_write : std_logic;
    end record;

    --! Pontos de controle do estágio Escrita de Retorno (Write Back)
    type t_CONTROL_WB is record
        --! Habilita a escrita no Arquivo de Registradores
        enable_destination : std_logic;
        --! Seleciona a fonte da escrita no Arquivo de Registradores
        select_destination : std_logic;
    end record;

    --! Sinais passados do estágio Busca Instrução para o estágio Decodifica Instrução, contendo os dados e pontos de controle registrados no pipeline
    type t_SIGNALS_IF_ID is record
        --! Vetor do Contador de Programa
        address_program  : t_DATA;
        --! Valor de instrução
        data_instruction : t_DATA;
    end record;

    --! Sinais passados do estágio Decodifica Instrução para o estágio Executa, contendo os dados e pontos de controle registrados no pipeline
    type t_SIGNALS_ID_EX is record
        --! Pontos de controle do estágio Executa
        control_ex         : t_CONTROL_EX;
        --! Pontos de controle do estágio Acessa a memória
        control_mem        : t_CONTROL_MEM;
        --! Pontos de controle do estágio Escrita de Retorno
        control_wb         : t_CONTROL_WB;
        --! Vetor do Contador de Programa
        address_program    : t_DATA;
        --! Vetor `source_1` do arquivo de registradores
        data_source_1      : t_DATA;
        --! Vetor `source_2` do arquivo de registradores
        data_source_2      : t_DATA;
        --! Vetor do Imediato
        data_immediate     : t_DATA;
        --! Vetor do `funct_7`
        funct_7            : WORK.RV32I.t_FUNCT7;
        --! Vetor do `funct_3`
        funct_3            : WORK.RV32I.t_FUNCT3;
        --! Vetor do Opcode
        opcode             : WORK.RV32I.t_OPCODE;
        --! Vetor do seletor do `destination`
        select_destination : t_REGISTER;
        --! Vetor do seletor do `source_1`
        select_source_1    : t_REGISTER;
        --! Vetor do seletor do `source_2`
        select_source_2    : t_REGISTER;
    end record;

    --! Sinais passados do estágio Executa para o estágio Acessa a Memória, contendo os dados e pontos de controle registrados no pipeline
    type t_SIGNALS_EX_MEM is record
        --! Pontos de controle do estágio Acessa a memória
        control_mem        : t_CONTROL_MEM;
        --! Pontos de controle do estágio Escrita de Retorno
        control_wb         : t_CONTROL_WB;
        --! Vetor `destination` do Executa
        data_destination   : t_DATA;
        --! Vetor do seletor do `source_2`
        data_source_2      : t_DATA;
        --! Vetor do seletor do `destination`
        select_destination : t_REGISTER;
        --! Vetor do `funct_3`
        funct_3            : WORK.RV32I.t_FUNCT3;
    end record;

    --! Sinais passados do estágio Acessa a Memória para o estágio Escrita de Retorno, contendo os dados e pontos de controle registrados no pipeline
    type t_SIGNALS_MEM_WB is record
        --! Pontos de controle do estágio Escrita de Retorno
        control_wb         : t_CONTROL_WB;
        --! Vetor `destination` da Memória
        data_memory        : t_DATA;
        --! Vetor `destination` do Executa
        data_destination   : t_DATA;
        --! Vetor do seletor do `destination`
        select_destination : t_REGISTER;
    end record;

    --! Dados e pontos de controle de forwarding do comparador de desvio no estágio Decodifica Instrução
    type t_FORWARD_BRANCH is record
        --! Vetor do seletor de forwarding do `source_1`
        select_source_1 : std_logic;
        --! Vetor do seletor de forwarding do `source_2`
        select_source_2 : std_logic;
        --! Vetor `destination` do estágio Acessa a Memória
        source_mem      : WORK.RV32I.t_DATA;
    end record;

    --! Dados e pontos de controle de forwarding da Unidade Lógica e Aritmética no estágio Executa
    type t_FORWARD_EXECUTION is record
        --! Vetor do seletor de forwarding do `source_1`
        select_source_1 : std_logic_vector(1 downto 0);
        --! Vetor do seletor de forwarding do `source_2`
        select_source_2 : std_logic_vector(1 downto 0);
        --! Vetor `destination` do estágio Acessa a Memória
        source_mem      : WORK.RV32I.t_DATA;
        --! Vetor `destination` do estágio Escrita de Retorno
        source_wb       : WORK.RV32I.t_DATA;
    end record;

    --! Registro nulo de `t_CONTROL_IF`
    constant NULL_CONTROL_IF : t_CONTROL_IF := (
        enable_stall  => '0',
        select_source => '0'
    );

    --! Registro nulo de `NULL_CONTROL_ID`
    constant NULL_CONTROL_ID : t_CONTROL_ID := (
        enable_branch   => '0',
        enable_jalr     => '0',
        enable_jump     => '0',
        select_jump     => '0'
    );

    --! Registro nulo de `NULL_CONTROL_EX`
    constant NULL_CONTROL_EX : t_CONTROL_EX := (
        select_source_1  => (others => '0'),
        select_source_2  => (others => '0')
    );

    --! Registro nulo de `NULL_CONTROL_MEM`
    constant NULL_CONTROL_MEM : t_CONTROL_MEM := (
        enable_read  => '0',
        enable_write => '0'
    );

    --! Registro nulo de `NULL_CONTROL_WB`
    constant NULL_CONTROL_WB : t_CONTROL_WB := (
        enable_destination => '0',
        select_destination => '0'
    );

    --! Registro nulo de `NULL_SIGNALS_IF_ID`
    constant NULL_SIGNALS_IF_ID : t_SIGNALS_IF_ID := (
        address_program  => (others => '0'),
        data_instruction => WORK.RV32I.NULL_INSTRUCTION
    );

    --! Registro nulo de `NULL_SIGNALS_ID_EX`
    constant NULL_SIGNALS_ID_EX : t_SIGNALS_ID_EX := (
        control_ex         => NULL_CONTROL_EX,
        control_mem        => NULL_CONTROL_MEM,
        control_wb         => NULL_CONTROL_WB,
        address_program    => (others => '0'),
        data_source_1      => (others => '0'),
        data_source_2      => (others => '0'),
        data_immediate     => (others => '0'),
        funct_7            => WORK.RV32I.FUNCT7_ADD,
        funct_3            => WORK.RV32I.FUNCT3_ADDI,
        opcode             => WORK.RV32I.OPCODE_OP_IMM,
        select_source_1    => (others => '0'),
        select_source_2    => (others => '0'),
        select_destination => (others => '0')
    );

    --! Registro nulo de `NULL_SIGNALS_EX_MEM`
    constant NULL_SIGNALS_EX_MEM : t_SIGNALS_EX_MEM := (
        control_mem        => NULL_CONTROL_MEM,
        control_wb         => NULL_CONTROL_WB,
        data_destination   => (others => '0'),
        data_source_2      => (others => '0'),
        select_destination => (others => '0'),
        funct_3            => WORK.RV32I.FUNCT3_ADDI
    );

    --! Registro nulo de `NULL_SIGNALS_MEM_WB`
    constant NULL_SIGNALS_MEM_WB : t_SIGNALS_MEM_WB := (
        control_wb         => NULL_CONTROL_WB,
        data_memory        => (others => '0'),
        data_destination   => (others => '0'),
        select_destination => (others => '0')
    );

    --! Registro nulo de `NULL_FORWARD_BRANCH`
    constant NULL_FORWARD_BRANCH : t_FORWARD_BRANCH := (
        select_source_1 => '0',
        select_source_2 => '0',
        source_mem      => (others => '0')
    );

    --! Registro nulo de `NULL_FORWARD_EXECUTION`
    constant NULL_FORWARD_EXECUTION : t_FORWARD_EXECUTION := (
        select_source_1 => (others => '0'),
        select_source_2 => (others => '0'),
        source_mem      => (others => '0'),
        source_wb       => (others => '0')
    );

end package;
