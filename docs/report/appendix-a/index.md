---
title: Insper | Projeto Final de Engenharia
titleTemplate: Desenvolvimento de RISC-V para Uso Aeroespacial
description: Apêndice B - Registros da Arquitetura
pageClass: printing-doc
editLink: false
---

# Apêndice B<br> Registros da Arquitetura {style="font-size: 2em;"}
---

Os registros da arquitetura foram definidos no arquivo TOP_LEVEL_CONSTANTS.vhd, que determina as constantes globais do projeto.

t_CONTROL_IF

- Registro com sinais de controle da etapa IF.

t_CONTROL_ID

- Registro com sinais de controle da etapa ID.

t_CONTROL_EX

- Registro com sinais de controle da etapa EX.

t_CONTROL_MEM

- Registro com sinais de controle da etapa MEM.

t_CONTROL_WB

- Registro com sinais de controle da etapa WB.

t_SIGNALS_IF_ID

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas IF e ID.

t_SIGNALS_ID_EX

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas ID e EX.

t_SIGNALS_EX_MEM

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas EX e MEM.

t_SIGNALS_MEM_WB

- Registro com sinais e/ou valores de entrada que são armazenados no registrador da pipeline que divide as etapas MEM e WB.
