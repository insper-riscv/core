---
title: Insper | Projeto Final de Engenharia
titleTemplate: Desenvolvimento de RISC-V para Uso Aeroespacial
description: Apêndice A - Pacote CPU
pageClass: printing-doc
editLink: false
---

## Apêndice A<br>Pacote WORK.CPU {style="font-size: 2em;"}

---

Para a topologia, um conjunto de registros foi criado para definir o fluxo de
dados em alto nível. Isso possibilita simplificar a implementação de pipelining
e manter o código limpo. A partir dos seguintes registros é possível declarar
todos os pontos de controle e de dados de todo o fluxo de execução da
arquitetura. Além disso, também são especificados valores que caracterizem o
comportamento ocioso da arquitetura.

### Controles do estágio Busca Instrução <Badge text="WORK.CPU.t_CONTROL_IF"/>

Este é o registro dos pontos de controle do estágio Busca Instrução. A partir do
qual é possível controlar os seguintes aspectos, respecitvamente:

- `enable_stall`: caso ativado, trava a contagem do programa;
- `select_source`: caso ativado, seleciona o endereço de desvio como origem do
  contador de programa.

```vhdl
type t_CONTROL_IF is record
    enable_stall  : std_logic;
    select_source : std_logic;
end record;

constant NULL_CONTROL_IF : t_CONTROL_IF := (
    enable_stall  => '0',
    select_source => '0'
);
```

### Controles do estágio Decodifica Instrução <Badge text="WORK.CPU.t_CONTROL_ID"/>

Este é o registro dos pontos de controle do estágio Decodifica Instrução. A
partir do qual é possível controlar os seguintes aspectos, respecitvamente:

- `enable_branch`: caso ativado, indica que a instrução é do tipo B;
- `enable_jump`: caso ativado, indica que a instrução é do tipo J;
- `select_jump`: caso ativado, seleciona o endereço de desvio
  `register + immediate`; caso contrário, `PC + immediate`.

```vhdl
type t_CONTROL_ID is record
    enable_branch : std_logic;
    enable_jump   : std_logic;
    select_jump   : std_logic;
end record;


constant NULL_CONTROL_ID : t_CONTROL_ID := (
    enable_branch   => '0',
    enable_jump     => '0',
    select_jump     => '0'
);
```

### Controles do estágio Executa <Badge text="WORK.CPU.t_CONTROL_EX"/>

Este é o registro dos pontos de controle do estágio Executa. A partir do qual é
possível controlar os seguintes aspectos, respecitvamente:

- `select_source_1`: Seleciona a fonte da entrada `source_1` entre,
  respecticamente, registrador, forwarding da saída do estágio Acessa a Memória,
  forwarding do saída do estágio Escrita de Retorno, e vetor nulo `00...00`;
- `select_source_2`: Seleciona a fonte da entrada `source_2` entre,
  respecticamente, registrador, forwarding da saída do estágio Acessa a Memória,
  forwarding do saída do estágio Escrita de Retorno, e vetor nulo `00...00`.

```vhdl
type t_CONTROL_EX is record
    select_source_1  : std_logic_vector(1 downto 0);
    select_source_2  : std_logic_vector(1 downto 0);
end record;

constant NULL_CONTROL_EX : t_CONTROL_EX := (
    select_source_1  => (others => '0'),
    select_source_2  => (others => '0')
);
```

### Controles do estágio Acessa a Memória <Badge text="WORK.CPU.t_CONTROL_MEM"/>

Este é o registro dos pontos de controle do estágio Acessa a Memória. A partir
do qual é possível controlar os seguintes aspectos, respecitvamente:

- `enable_read`: caso ativado, indica que o núcleo está realizando uma leitura
  da memória;
- `enable_write`: caso ativado, indica que o núcleo está realizando uma escrina
  na memória.

```vhdl
type t_CONTROL_MEM is record
    enable_read  : std_logic;
    enable_write : std_logic;
end record;

constant NULL_CONTROL_MEM : t_CONTROL_MEM := (
    enable_read  => '0',
    enable_write => '0'
);
```

### Controles do estágio Escrite de Retorno <Badge text="WORK.CPU.t_CONTROL_WB"/>

Este é o registro dos pontos de controle do estágio Escrite de Retorno. A partir
do qual é possível controlar os seguintes aspectos, respecitvamente:

- `enable_destination`: caso ativado, habilita a escrita no arquivo de
  registradores;
- `select_destination`: caso ativado, seleciona o retorno para a entrada de
  dados da memória; caso contrário, do resultado da unidade lógica e aritmética.

```vhdl
type t_CONTROL_WB is record
    enable_destination : std_logic;
    select_destination : std_logic;
end record;

constant NULL_CONTROL_WB : t_CONTROL_WB := (
    enable_destination => '0',
    select_destination => '0'
);
```

### Sinais do registrador de pipeline IF/ID <Badge text="WORK.CPU.t_SIGNALS_IF_ID"/>

Este é o registro dos sinais do estágio Decodifica instrução, que recebe os
sinais do Busca Instrução e os registra no pipeline. A partir do seguinte
registro é possível controlar os seguintes aspectos, respecitvamente:

- `address_program`: Valor de saída do contador de programa;
- `data_instruction`: Valor de saída da memória de programa.

```vhdl
type t_SIGNALS_IF_ID is record
    address_program  : t_DATA;
    data_instruction : t_DATA;
end record;

constant NULL_SIGNALS_IF_ID : t_SIGNALS_IF_ID := (
    address_program  => (others => '0'),
    data_instruction => WORK.RV32I.NULL_INSTRUCTION
);
```

### Sinais do registrador de pipeline ID/EX <Badge text="WORK.CPU.t_SIGNALS_ID_EX"/>

Este é o registro dos sinais do estágio Executa, que recebe os sinais do
Decodifica instrução e os registra no pipeline. A partir do seguinte registro é
possível controlar os seguintes aspectos, respecitvamente:

- `control_ex`: Pontos de controle do estágio Executa;
- `control_mem`: Pontos de controle do estágio Acessa a memória;
- `control_wb`: Pontos de controle do estágio Escrita de Retorno;
- `address_program`: Valor de saída do contador de programa;
- `data_source_1`: Vetor selecionado por `sr1` no arquivo de registradores;
- `data_source_2`: Vetor selecionado por `sr2` no arquivo de registradores;
- `data_immediate`: Vetor do imediato decodificado pela instrução;
- `funct_7`: Vetor da instrução segmentado pela região `funct_7`;
- `funct_3`: Vetor da instrução segmentado pela região `funct_3`;
- `opcode`: Vetor da instrução segmentado pela região `opcode`;
- `select_destination`: Vetor da instrução segmentado pela região `ds`;
- `select_source_1`: Vetor da instrução segmentado pela região `sr1`;
- `select_source_2`: Vetor da instrução segmentado pela região `sr2`.

```vhdl
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
```

### Sinais do registrador de pipeline EX/MEM <Badge text="WORK.CPU.t_SIGNALS_EX_MEM"/>

Este é o registro dos sinais do estágio Acesso a Memória, que recebe os sinais
do Executa e os registra no pipeline. A partir do seguinte registro é possível
controlar os seguintes aspectos, respecitvamente:

- `control_mem`: Pontos de controle do estágio Acessa a memória;
- `control_wb`: Pontos de controle do estágio Escrita de Retorno;
- `data_destination`: Vetor resultante da operação entre `data_source_1` e `data_source_2` na unidade lógica e aritmética pelo operando em `funct_7`, `funct_3`, `opcode`;
- `data_source_2`: Vetor selecionado por `sr2` no arquivo de registradores;
- `select_destination`: Vetor da instrução segmentado pela região `ds`;
- `funct_3`: Vetor da instrução segmentado pela região `funct_3`.

```vhdl
type t_SIGNALS_EX_MEM is record
    control_mem        : t_CONTROL_MEM;
    control_wb         : t_CONTROL_WB;
    data_destination   : t_DATA;
    data_source_2      : t_DATA;
    select_destination : t_REGISTER;
    funct_3            : WORK.RV32I.t_FUNCT3;
end record;

constant NULL_SIGNALS_EX_MEM : t_SIGNALS_EX_MEM := (
    control_mem        => NULL_CONTROL_MEM,
    control_wb         => NULL_CONTROL_WB,
    data_destination   => (others => '0'),
    data_source_2      => (others => '0'),
    select_destination => (others => '0'),
    funct_3            => WORK.RV32I.FUNCT3_ADDI
);
```

### Sinais do registrador de pipeline MEM/WB <Badge text="WORK.CPU.t_SIGNALS_MEM_WB"/>

Este é o registro dos sinais do estágio Escrita de Retorno, que recebe os sinais
do Acesso a Memória e os registra no pipeline. A partir do seguinte registro é
possível controlar os seguintes aspectos, respecitvamente:

- `control_wb`: Pontos de controle do estágio Escrita de Retorno;
- `data_memory`: Vetor resgatado na memória pelo endereço definido por `data_destination`;
- `data_destination`: Vetor resultante da operação entre `data_source_1` e `data_source_2` na unidade lógica e aritmética pelo operando em `funct_7`, `funct_3`, `opcode`;
- `select_destination`: Vetor da instrução segmentado pela região `ds`.

```vhdl
type t_SIGNALS_MEM_WB is record
    control_wb         : t_CONTROL_WB;
    data_memory        : t_DATA;
    data_destination   : t_DATA;
    select_destination : t_REGISTER;
end record;

constant NULL_SIGNALS_MEM_WB : t_SIGNALS_MEM_WB := (
    control_wb         => NULL_CONTROL_WB,
    data_memory        => (others => '0'),
    data_destination   => (others => '0'),
    select_destination => (others => '0')
);
```

### Sinais de forward de desvio <Badge text="WORK.CPU.t_SIGNALS_MEM_WB"/>

Este é o registro dos controles e sinais de forwarding do comparador de desvio
no estágio Decodifica Instrução. A partir do seguinte registro é possível
controlar os seguintes aspectos, respecitvamente:

- `select_source_1`: Seleciona a origem do vetor `data_source_1` na unidade de comparação de desvio, respectivamente, entre o arquivo de registradores, o forward do destino do estágio Executa, o forward do destino do estágio Acessa a Memória e o forward do destino do estágio Escrita de Retorno;
- `select_source_2`: Seleciona a origem do vetor `data_source_2` na unidade de comparação de desvio, respectivamente, entre o arquivo de registradores, o forward do destino do estágio Executa, o forward do destino do estágio Acessa a Memória e o forward do destino do estágio Escrita de Retorno;
- `source_ex`: Vetor de destino do estágio Executa;
- `source_mem`: Vetor de destino do estágio Acessa a Memória;
- `source_wb`: Vetor de destino do estágio Escrita de Retorno.

```vhdl
type t_FORWARD_BRANCH is record
    select_source_1 : std_logic_vector(1 downto 0);
    select_source_2 : std_logic_vector(1 downto 0);
    source_ex       : WORK.RV32I.t_DATA;
    source_mem      : WORK.RV32I.t_DATA;
    source_wb       : WORK.RV32I.t_DATA;
end record;
```

### Sinais do forward de execução <Badge text="WORK.CPU.t_SIGNALS_MEM_WB"/>

Este é o registro dos controles e sinais de forwarding da unidade lógica e aritmética
no estágio Executa. A partir do seguinte registro é possível
controlar os seguintes aspectos, respecitvamente:

- `select_source_1`: Seleciona a origem do vetor `data_source_1` na unidade de comparação de desvio, respectivamente, entre o arquivo de registradores no estágio Executa, o forward do destino do estágio Acessa a Memória e o forward destino do estágio Escrita de Retorno;
- `select_source_2`: Seleciona a origem do vetor `data_source_2` na unidade de comparação de desvio, respectivamente, entre o arquivo de registradores no estágio Executa, o forward do destino do estágio Acessa a Memória e o forward destino do estágio Escrita de Retorno;
- `source_mem`: Vetor de destino do estágio Acessa a Memória;
- `source_wb`: Vetor de destino do estágio Escrita de Retorno.

```vhdl
type t_FORWARD_EXECUTION is record
    select_source_1 : std_logic_vector(1 downto 0);
    select_source_2 : std_logic_vector(1 downto 0);
    source_mem      : WORK.RV32I.t_DATA;
    source_wb       : WORK.RV32I.t_DATA;
end record;
```
