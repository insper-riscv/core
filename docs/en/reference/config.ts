import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/en/reference/': [
            {
                text: 'Components',
                link: '/en/reference/components/',
                collapsed: false,
                items: [
                    {
                        text: 'Generics',
                        collapsed: true,
                        items: [
                            {
                                text: 'Adder',
                                link: '/en/reference/components/generic_adder',
                            }, {
                                text: 'MUX 2:1',
                                link: '/en/reference/components/generic_mux_2x1',
                            }, {
                                text: 'MUX 4:1',
                                link: '/en/reference/components/generic_mux_4x1',
                            }, {
                                text: 'RAM',
                                link: '/en/reference/components/generic_ram',
                            }, {
                                text: 'ROM',
                                link: '/en/reference/components/generic_rom',
                            }, {
                                text: 'Register',
                                link: '/en/reference/components/generic_register',
                            }, 
                        ],
                    }, {
                        text: 'RV32I',
                        collapsed: true,
                        items: [
                            {
                                text: 'Instruction Decoder',
                                link: '/en/reference/components/rv32i_instruction_decoder',
                            }, {
                                text: 'Register File',
                                link: '/en/reference/components/rv32i_register_file',
                            }, {
                                text: 'ALU Bit',
                                link: '/en/reference/components/rv32i_alu_bit',
                            }, {
                                text: 'ALU',
                                link: '/en/reference/components/rv32i_alu',
                            }, {
                                text: 'ALU Controller',
                                link: '/en/reference/components/rv32i_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Modules',
                        collapsed: true,
                        items: [
                            {
                                text: 'Register File',
                                link: '/en/reference/components/module_register_file',
                            },{
                                text: 'Program Counter',
                                link: '/en/reference/components/module_program_counter',
                            }, {
                                text: 'Write Back',
                                link: '/en/reference/components/module_write_back',
                            }, {
                                text: 'Control Unit',
                                link: '/en/reference/components/module_control_unit',
                            }, {
                                text: 'ALU',
                                link: '/en/reference/components/module_alu',
                            }, {
                                text: 'ALU Controller',
                                link: '/en/reference/components/module_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Stages',
                        collapsed: true,
                        items: [
                            {
                                text: 'Instruction Fetch',
                                link: '/en/reference/components/stage_if',
                            }, {
                                text: 'Instruction Decode',
                                link: '/en/reference/components/stage_id',
                            }, {
                                text: 'Execute',
                                link: '/en/reference/components/stage_ex',
                            }, {
                                text: 'Memory Access',
                                link: '/en/reference/components/stage_mem',
                            }, {
                                text: 'Write Back',
                                link: '/en/reference/components/stage_wb',
                            },
                        ],
                    }, 
                ],
            }, {
                text: 'Instructions',
                link: '/en/reference/isa/',
            }, {
                text: 'Pseudo-instructions',
                link: '/en/reference/isa/pseudo',
            },
        ],
    },
} satisfies DefaultTheme.Config
