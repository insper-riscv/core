[Rafael Corsi Ferrão](http://lattes.cnpq.br/4775677284462845). Projeto Final de Engenharia. [Insper](https://github.com/Insper), 2024.

# CTI RISCV

[![Deploy Docs](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/deploy-docs.yml)
[![VHD tests](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/vhd_tests.yml/badge.svg)](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/vhd_tests.yml)
[![VHD Coverage tests](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/vhd_tests_coverage.yml/badge.svg)](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/vhd_tests_coverage.yml)
[![Quartus Tests](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/quartus_tests.yml/badge.svg)](https://github.com/pfeinsper/24a-CTI-RISCV/actions/workflows/quartus_tests.yml)

O objetivo central deste projeto é o desenvolvimento de uma Propriedade
Intelectual (IP) de um processador baseado na arquitetura RISC-V,
especificamente para aplicações aeroespaciais. O design do hardware deve ser
modular, permitindo sua adaptação a uma variedade de cenários operacionais. O
processador será inicialmente testado em uma FPGA Intel. É crucial que o
processador seja capaz de suportar a execução de um sistema operacional de tempo
real, garantindo eficiência e confiabilidade em ambientes aeroespaciais. Além
disso, o projeto incluirá a realização de testes de unidade e integração
detalhados para assegurar a qualidade e a funcionalidade do processador em todas
as etapas de desenvolvimento.

## Rotina de testes

```bash
$ pytest -s
```
