# Desenvolvimento do Projeto

O projeto foi realizado utilizando a metodologia ágil, que é uma estrutura de
gerenciamento onde os projetos são divididos em etapas com tarefas a serem
realizadas, etapas estas denominadas de sprints. A metodologia foi aplicada por
meio de um mural Kanban no Github, que é uma abordagem visual onde as sprints
estão posicionadas em diferentes pontos do mural dependendo de como o grupo tem
progredido nelas.

![Mural Kanban](/images/mural_kanban.png)

## Ambiente de Desenvolvimento

A parte técnica do projeto foi desenvolvida no Visual Studio Code (VSCode), uma
ferramenta gratuita de edição de código, usando um contêiner docker. O Docker é
uma plataforma que facilita o desenvolvimento de código por meio de ambientes
isolados (contêineres) que contêm as especificações e configurações necessárias
para o desenvolvimento do projeto e podem ser utilizados independente do sistema
operacional da máquina do desenvolvedor.

O contêiner Docker também é utilizado em conjunto com o GitHub Actions para
realizar a validação com o Quartus. Além do [Dockerfile](https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/.devcontainer/Dockerfile) 
presente no repositório do GitHub,ele está disponível no [Docker Hub](https://hub.docker.com/repository/docker/gianvr/pfe/) 
podendo ser clonado com o comando:

```bash
$ docker push gianvr/pfe:latest
```


## Validação dos Componentes

Utilizou-se neste projeto pytest, uma ferramenta de estruturação de testes em
python. Através da biblioteca é possível executar todos os testes de uma vez, bem como por categoria,
sendo três categorias: tests cases, stress e synthesis. 

Além disso, como o processador foi desenvolvido em VHDL, 
fez-se uso do GHDL, um simulador de VHDL que realiza a síntese dos componentes, simulando a
sua compilação, e detecta se há algum erro de sintaxe ou de semântica na
programação dos mesmos. Após esse processo ser realizado, executam-se os testes dos componentes usando o cocotb,
que é uma biblioteca python feita para realizar testes em VHDL. 

Além dos testes em python, foram criados que realiza as seguintes etapas de 
compilação do Quartus: Synthesis, Elaboration, Fitter e Timing Analysis.

### Casos de Teste

Os casos de testes, ou testes unitários, são testes criados manualmente para verificar se um componente está funcionando corretamente para um conjunto limitado de entradas. Um exemplo de teste unitário para o componente ADDER é mostrado abaixo.

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ADDER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_ADDER.py &boxbox;" /></a>

```python
...

@GENERIC_ADDER.testcase
async def tb_GENERIC_ADDER_case_1(dut: GENERIC_ADDER, trace: utils.Trace):
    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000000")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000000")

    dut.source_1.value = BinaryValue("00000000000000000000000000000000")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000001")

    dut.source_1.value = BinaryValue("00000000000000000000000000000001")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")

    await trace.cycle()
    yield trace.check(dut.destination, "00000000000000000000000000000010")

    dut.source_1.value = BinaryValue("10101010101010101010101010101010")
    dut.source_2.value = BinaryValue("01010101010101010101010101010101")

    await trace.cycle()
    yield trace.check(dut.destination, "11111111111111111111111111111111")

    dut.source_1.value = BinaryValue("00101010101010101010101010101010")
    dut.source_2.value = BinaryValue("00101010101010101010101010101010")

    await trace.cycle()
    yield trace.check(dut.destination, "01010101010101010101010101010100")

    dut.source_1.value = BinaryValue("11111111111111111111111111111110")
    dut.source_2.value = BinaryValue("00000000000000000000000000000001")

...

```
:::



### Testes de Stress

Ao analisar testes unitários, é possível verificar se os componentes estão funcionando corretamente para um conjunto limitado de entradas. Entretanto, como mostra a figura abaixo, o espaço de teste que eles cobrem, representado pelo quadrado cinza, é limitado.

<p align="center">
    <img src="/images/unit_test.svg" width="300">
</p>

Uma maneira de validar os componentes, que foi solicitada pelo cliente, é o teste de stress ou teste exaustivo. Essa validação consiste em testar todas as possibilidades, ou um número bem grande delas. O espaço de teste que ele cobre, representado pela cor cinza na figura abaixo, é completo.

<p align="center">
    <img src="/images/exaustive.svg" width="300">
</p>

Caso fosse realizar testes exaustivos para encontrar todas as possíveis entradas seria algo inviável para 32 bits, a largura de dados do projeto, pois seria necessário multiplicar todas as possíveis entradas. Por exemplo, para um mux 2x1 de 32 bits, seriam necessários 2<sup>32</sup> * 2<sup>32</sup> * 2 = 2<sup>65</sup> casos de testes. Caso cada teste leve em torno de 1 ms, levariam cerca de 1169884 séculos, o que torna inviável. 

Para conseguir aumentar a chance de encontrar possíveis erros nos componentes, foi utilizada a estratégia Constraint Random Verification (CRV). Ela consiste em criar um número grande de testes aleatorizados, com algumas restrições, para conseguir cobrir uma quantidade maior de cenários. Como os testes são aleatórios, quanto mais testes forem realizados, maior a chance de encontrar um erro. Na figura abaixo, a cobertura dos testes feitos pelo CRV são representados pelas nuvens cinzas e quanto mais testes forem realizados, maior serão as chances de encontrar um erro.

<p align="center">
    <img src="/images/crv.svg" width="300">
</p>

A implementação do CRV foi feita utilizando um loop que executa uma certa quantidade de vezes, em conjunto com a biblioteca random, nativa do Python, que gera aleatoriamente os valores das entradas, sendo em alguns casos para todas elas. Enquanto para a validação, o comportamento esperado do componente é simulado no Python para verificar se a saída corresponde. Um exemplo para o componente ADDER é mostrado abaixo.

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ADDER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_ADDER.py &boxbox;" /></a>

```python
import random

...

@GENERIC_ADDER.testcase
async def tb_GENERIC_ADDER_stress(dut: "GENERIC_ADDER", trace: utils.Trace):
    for _ in range(1_000_000):
        source_1 = random.getrandbits(32)
        source_2 = random.getrandbits(32)
    
        dut.source_1.value = BinaryValue('{0:0{1}b}'.format(source_1, 32))
        dut.source_2.value = BinaryValue('{0:0{1}b}'.format(source_2, 32))
    
        await trace.cycle()

        message = f"source_1: {'{0:0{1}b}'.format(source_1, 32)}, source_2: {'{0:0{1}b}'.format(source_2, 32)}"

        yield trace.check(dut.destination, '{0:0{1}b}'.format(source_1+source_2, 32)[-32:], message)

...

```
:::

Outra estratégia utilizada foi para validar a lógica do componente utilizando uma largura de dados menor. Por meio dessa estratégia é possível conseguir realizar um teste exaustivo que consegue verificar todas as entradas possíveis. Novamente, utilizando o mux 2x1 como exemplo, ao reduzir a largura de dados de 32 bits para 5 bits, é possível atingir 2<sup>5</sup> * 2<sup>5</sup> * 2 = 2<sup>11</sup> = 2048 possibilidades, um número viável de testes. A implementação foi feita criando loops aninhados para cada entrada e depois comparando a saída com a simulação do modelo em Python. Um exemplo para o componente adder é mostrado abaixo.

::: details Código fonte <a href="https://github.com/pfeinsper/24a-CTI-RISCV/blob/main/test/test_GENERIC_ADDER.py" target="blank" style="float:right"><Badge type="tip" text="test_GENERIC_ADDER.py &boxbox;" /></a>

```python
...

@GENERIC_ADDER.testcase
async def tb_GENERIC_ADDER_stress_5_bits(dut: "GENERIC_ADDER", trace: utils.Trace):
    bits = 5
    for i in range(2**bits):
        for j in range(2**bits):
                source_1 = '{0:0{1}b}'.format(i, bits)
                source_2 = '{0:0{1}b}'.format(j, bits)

                dut.source_1.value = BinaryValue(source_1)
                dut.source_2.value = BinaryValue(source_2)

                message = f"source_1: {source_1}, source_2: {source_2}"
                
                await trace.cycle()
                yield trace.check(dut.destination, '{0:0{1}b}'.format(i+j, bits)[-bits:], message)

...

```
:::


Assim, as duas estratégias se complementam, pois como cada uma verifica uma largura de dados diferente, 
é possível observar se o comportamento muda conforme a sua variação. E com isso, foi possível atender a 
demanda do cliente em relação aos testes de stress.

#### Componentes cobertos

Os componentes cobertos são:

- [Generic Adder](/reference/components/generic_adder)
- [Generic Mux 2x1](/reference/components/generic_mux_2x1)
- [Generic Mux 4x1](/reference/components/generic_mux_4x1)
- [Generic Register](/reference/components/generic_register)


### Síntese e RTL

Uma maneira de validar os componentes é por meio do RTL. Através da ferramenta Yosis e do NetlistSVG é possível executar
a síntese e o RTL, que pode ser visto na figura abaixo para o componente `Generic Adder`:

![RTL view from somador](/images/reference/components/generic_adder_netlist.svg){.w-full .dark-invert}

### Waveform

Para visualizar o comportamento dos componentes, foi utilizado WaveDrom, que é uma ferramenta que permite a criação de
diagramas com base de tempo. Um exemplo de waveform para o componente `Generic Adder` é mostrado abaixo:


![Waveform from caso de teste 1 do somador](/images/reference/components/tb_generic_adder_case_1.svg){.w-full .dark-invert}

### Testes do Quartus

Através de comandos no terminal também é possível realizar testes do Quartus. Ele faz a compilação do projeto
especificamente para a FPGA utilizada, que é a Cyclone V, modelo 5CEBA4F23C7N. Os comando conseguem retornar 
logs sem a necessidade de abrir a interface gráfica do Quartus, permitindo automatizar o processo com o Github
Actions, como a figura abaixo que mostra um teste bem sucedido:

<p align="center">
    <img src="/images/quartus_actions.png" width="300">
</p>


Ou com a criação de botões no VS Code que permitem execução desses comandos, como mostrado abaixo em que 
alguns recursos do Quartus, incluindo a abertura da interface gráfica, podem ser executados diretamente na IDE:

<p align="center">
    <img src="/images/buttons_quartus.png" width="800">
</p>

### Testes na Placa

A fim de ter resultados mais concretos sobre o funcionamento do processador, foi
utilizada uma placa FPGA para testar o RISC-V desenvolvido. Para programar a
placa, foi utilizado o software Quartus, da Intel, que permite a compilação e
execução de designs de CPUs em placas FPGA.

## Github Actions

A implementação de um sistema de testes para o processador, com integração e
entrega contínuas (CI/CD), foi feita por meio do Github Actions, uma ferramenta
do Github que permite criar fluxos de trabalho para os eventos desejados, o que
permite automatizar a realização de testes em uma etapa prévia ao código ser
disponibilizado para ambiente de produção.

Nele é realizado o deploy do site da documentação, os casos de testes feitos em
Python e a validação do Quartus. Alguns workflows são executados automaticamente
após um push em determinadas pastas, como o deploy do site da documentação, casos
de testes mais simples e a validação do Quartus, e outros são executados manualmente, 
como os testes de stress, que são mais demorados. 

Um exemplo de workflow para os casos de teste dos componentes é mostrado abaixo:

<p align="center">
    <img src="/images/actions.png" width="300">
</p>



## Documentação

Este projeto foi documentado usando o vitepress, que é uma ferramenta que
permite construir sites usando arquivos Markdown, e hospedado no Github pelo
Github Pages.

## Referências


- CHIPVERIFY. Constraint Random Verification. Disponível em: 
<https://www.chipverify.com/verification/constraint-random-verification>. Acesso em: 19 abr. 2024.

- GREEN, M. Why Do Constrained Random Verification. Disponível em: <https://magreen.medium.com/why-do-constrained-random-verification-1b8bfe4717b4>. Acesso em: 25 abr. 2024.

- Laoyan, S. **What is Agile methodology? (A beginner’s guide)**. Asana, 15
  oct. 2022. Available at: https://asana.com/pt/resources/agile-methodology

