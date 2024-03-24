# Project Development

The project was carried out using agile methodology, which is a management 
framework where projects are divided into stages with tasks to be completed,
these stages are called sprints. The methodology was applied through a Kanban
board on Github, which is a visual approach where the sprints are positioned
at different points on the board depending on how the group has progressed in them.

![Kanban Board](/images/mural_kanban.png)

## Development Environment

The technical part of the project was developed in Visual Studio Code (VSCode),
a free code editing tool, using a docker container. Docker is a platform that 
facilitates code development through isolated environments (containers) that 
have in them the specifications and configurations necessary for the project's 
development regardless of the developer's machine's operating system.

## Logical Tests

Pytest, a test structuring tool in Python, was used in this project. Additionally,
since the processor was developed in VHDL, GHDL was used, which is a VHDL 
that synthesizes the components, simulating their compilation, and detects any syntax
or semantic errors in their programming. After this process is done, the logic tests
of the components are executed using cocotb, which is a Python library designed to perform tests in VHDL.

## Board Testing

In order to have more concrete results about the processor's operation, an FPGA board
was used to test the developed RISC-V. To program the board, Quartus software from Intel
was used, which allows compilation and execution of CPU designs on FPGA boards.

## Github Actions

The implementation of a testing system for the processor, with continuous integration
and delivery (CI/CD), was done through Github Actions, a Github tool that allows 
creating workflows for desired events, which automates the testing process in a 
pre-production environment before the code is released.

## Documentation

This project was documented using Vitepress, which is a tool that allows building 
websites using Markdown files, and hosted on Github using Github Pages.

## References

- Laoyan, S. **What is Agile methodology? (A beginner’s guide)**. Asana, 15 oct. 2022. Available at: https://asana.com/pt/resources/agile-methodology

