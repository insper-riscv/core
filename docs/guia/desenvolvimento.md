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
ferramenta gratuita de edição de código, usando um contêiner docker. A Docker é
uma plataforma que facilita o desenvolvimento de código por meio de ambientes
isolados (contêineres) que contêm as especificações e configurações necessárias
para o desenvolvimento do projeto e podem ser utilizados independente do sistema
operacional da máquina do desenvolvedor.

## Testes Lógicos

Utilizou-se neste projeto o pytest, uma ferramenta de estruturação de testes em
python. Além disso, como o processador foi desenvolvido em VHDL, fez-se uso do
GHDL, um simulador de VHDL que realiza a síntese dos componentes, simulando a
sua compilação, e detecta se há algum erro de sintaxe ou de semântica na
programação dos mesmos. Após esse processo ser realizado, executam-se os testes
da lógica dos componentes usando o cocotb, que é uma biblioteca python feita
para realizar testes em VHDL.

## Testes na Placa

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

## Documentação

Este projeto foi documentado usando o vitepress, que é uma ferramenta que
permite construir sites usando arquivos Markdown, e hospedado no Github pelo
Github Pages.

## Referências

- Laoyan, S. **What is Agile methodology? (A beginner’s guide)**. Asana, 15
  oct. 2022. Available at: https://asana.com/pt/resources/agile-methodology
