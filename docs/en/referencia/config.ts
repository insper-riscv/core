import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/en/referencia/': [
            {
                text: 'Components',
                link: '/en/referencia/componentes/',
                collapsed: false,
                items: [
                    {
                        text: 'Generic',
                        collapsed: true,
                        items: [
                            {
                                text: 'Adder',
                                link: '/en/referencia/componentes/generic_adder',
                            }, {
                                text: 'MUX 2:1',
                                link: '/en/referencia/componentes/generic_mux_2x1',
                            }, {
                                text: 'MUX 4:1',
                                link: '/en/referencia/componentes/generic_mux_4x1',
                            }, {
                                text: 'RAM',
                                link: '/en/referencia/componentes/generic_ram',
                            }, {
                                text: 'ROM',
                                link: '/en/referencia/componentes/generic_rom',
                            }, {
                                text: 'Register',
                                link: '/en/referencia/componentes/generic_register',
                            }, 
                        ],
                    }, {
                        text: 'RV32I',
                        collapsed: true,
                        items: [
                            {
                                text: 'Instruction Decoder',
                                link: '/en/referencia/componentes/rv32i_instruction_decoder',
                            }, {
                                text: 'Register File',
                                link: '/en/referencia/componentes/rv32i_register_file',
                            }, {
                                text: 'ALU Bit',
                                link: '/en/referencia/componentes/rv32i_alu_bit',
                            }, {
                                text: 'ALU',
                                link: '/en/referencia/componentes/rv32i_alu',
                            }, {
                                text: 'ALU Controller',
                                link: '/en/referencia/componentes/rv32i_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Modules',
                        collapsed: true,
                        items: [
                            {
                                text: 'Register File',
                                link: '/en/referencia/componentes/module_register_file',
                            },{
                                text: 'Program Counter',
                                link: '/en/referencia/componentes/module_program_counter',
                            }, {
                                text: 'Write Back',
                                link: '/en/referencia/componentes/module_write_back',
                            }, {
                                text: 'Control Unit',
                                link: '/en/referencia/componentes/module_control_unit',
                            }, {
                                text: 'ALU',
                                link: '/en/referencia/componentes/module_alu',
                            }, {
                                text: 'ALU Controller',
                                link: '/en/referencia/componentes/module_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Stages',
                        collapsed: true,
                        items: [
                            {
                                text: 'Instruction Fetch',
                                link: '/en/referencia/componentes/stage_if',
                            }, {
                                text: 'Instruction Decode',
                                link: '/en/referencia/componentes/stage_id',
                            }, {
                                text: 'Execute',
                                link: '/en/referencia/componentes/stage_ex',
                            }, {
                                text: 'Memory Access',
                                link: '/en/referencia/componentes/stage_mem',
                            }, {
                                text: 'Write Back',
                                link: '/en/referencia/componentes/stage_wb',
                            },
                        ],
                    }, 
                ],
            }, {
                text: 'Instructions',
                link: '/en/referencia/isa/',
            }, {
                text: 'Pseudo-instructions',
                link: '/en/referencia/isa/pseudo',
            },
        ],
    },
} satisfies DefaultTheme.Config
