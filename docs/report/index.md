---
title: Insper | Projeto Final de Engenharia
titleTemplate: Desenvolvimento de RISC-V para Uso Aeroespacial
description: Relatório Versão Intermediária do Projeto Final de Engenharia
pageClass: printing-doc
editLink: false
---

## Capa { style="position: absolute; visibility: hidden;"}

**Desenvolvimento de RISC-V para Uso Aeroespacial**
{style="text-align: center; padding-top: 11em; padding-bottom: 6em;"}

<br/>

**Giancarlo Vanoni Ruggiero (giancarlovr@al.insper.edu.br)**  
**Luciano Felix Dias (lucianofd@al.insper.edu.br)**  
**Tiago Vitorino Seixas (tiagovs1@al.insper.edu.br)**
{style="text-align: center; padding-bottom: 5em;"}

<br/>

**Trabalho de Conclusão de Curso**
{style="text-align: center; padding-bottom: 5em;"}

<br/>

**Relatório**  
**Versão Intermediária**  
**do Projeto Final de Engenharia**
{style="text-align: center; padding-bottom: 6em;"}

<br/>

**São Paulo-SP**  
**Março 2024**
{style="text-align: center;"}

--- {class="break-page"}

**Giancarlo Vanoni Ruggiero**  
**Luciano Felix Dias**  
**Tiago Vitorino Seixas**
{style="text-align: center; padding-top: 9em; padding-bottom: 6em;"}

<br/>

# Desenvolvimento de RISC-V para Uso Aeroespacial  {style="text-align: center;"}

<br/>

**Relatório Versão Intermediária do Projeto Final de Engenharia**
{style="text-align: center; padding-bottom: 5em;"}

<br/>

Relatório apresentado ao curso de Engenharia, como requisito para o Trabalho de Conclusão de Curso.<br/><br/>
Professor Orientador: Prof. Rafael Corsi Ferrão<br/><br/>
Mentor na Empresa: Saulo Finco<br/><br/>
Coordenador TCC/PFE: Prof. Dr. Luciano Pereira Soares
{style="margin-left: 33%; padding-bottom: 11em;"}

<br/>

**São Paulo - SP**  
**Março 2024**
{style="text-align: center;"}

## Sumário {style="text-align: center;"}

[[toc]]

<!--@include: @/report/.resumo.md-->
<!--@include: @/report/.abstract.md-->

<section class="printing-doc--columns-section">

<!--@include: @/report/.introducao.md-->
<!--@include: @/report/.metodologia.md-->
<!--@include: @/report/.resultados.md-->
<!--@include: @/report/.conclusao.md-->

</section>

## Referências

<style>
    .printing-doc {
        p,
        li {
            text-align: justify;
        }

        .break-page,
        h2 {
            page-break-before : always;
        }

        hr {
            margin: 32px 0;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            font-size: 12pt;
        }

        li {
            break-inside: avoid-column;
        }

        p, table {
            break-inside: avoid-page;
        }

        table {
            column-span: all;
        }

        h1, h2, h3, h4, h5, h6, img, svg, figure {
            column-span: all;
            break-inside: avoid-column;
        }

        figure {
            margin: 16px 0;
        }

        .table-of-contents {
            ul {
                list-style: none;
            }

            li:nth-child(1),
            li:nth-child(2) {
                display: none;
            }
        }

        .footnotes-sep,
        .footnote-backref {
            display: none;
        }

        @media print {
            font-size: 12pt;
            font-family: "Times New Roman";

            a {
                color: currentcolor;
                font: inherit;
                text-decoration: none;
            }

            h2 {
                padding-top: 0;
                border-top: none;
            }

            p {
                line-height: 14pt;
            }

            hr.break-page {
                opacity: 0;
            }

            .printing-doc--columns-section {
                columns: 2;
            }

            .VPNav,
            .VPLocalNav,
            .VPFooter,
            .VPDocFooter,
            .header-anchor {
                display: none;
            }
        }
    }
</style>