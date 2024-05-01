---
title: Insper | Projeto Final de Engenharia
titleTemplate: Desenvolvimento de RISC-V para Uso Aeroespacial
description: Apêndice A - Pacote CPU
pageClass: printing-doc
editLink: false
---

# Apêndice A<br> Pacote CPU {style="font-size: 2em;"}
---

Os registros da arquitetura foram definidos no arquivo CPU.vhd, sendo que cada registro tem uma constante do tipo NULL correspondente que especifica o estado padrão do mesmo.

## t_CONTROL_IF

- Registro com sinais de controle da etapa IF.
- Constante NULL_CONTROL_IF define o seu estado padrão.

## t_CONTROL_ID

- Registro com sinais de controle da etapa ID.
- Constante NULL_CONTROL_ID define o seu estado padrão.

## t_CONTROL_EX

- Registro com sinais de controle da etapa EX.
- Constante NULL_CONTROL_EX define o seu estado padrão.

## t_CONTROL_MEM

- Registro com sinais de controle da etapa MEM.
- Constante NULL_CONTROL_MEM define o seu estado padrão.

## t_CONTROL_WB

- Registro com sinais de controle da etapa WB.
- Constante NULL_CONTROL_WB define o seu estado padrão.

## t_SIGNALS_IF_ID

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas IF e ID.
- Constante NULL_SIGNALS_IF_ID define o seu estado padrão.

## t_SIGNALS_ID_EX

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas ID e EX.
- Constante NULL_SIGNALS_ID_EX define o seu estado padrão.

## t_SIGNALS_EX_MEM

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas EX e MEM.
- Constante NULL_SIGNALS_EX_MEM define o seu estado padrão.

## t_SIGNALS_MEM_WB

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas MEM e WB.
- Constante NULL_SIGNALS_MEM_WB define o seu estado padrão.
