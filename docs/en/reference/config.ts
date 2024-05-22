import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/en/reference/': [
            {
                text: 'Organization',
                link: '/en/reference/components/',
                collapsed: false,
                items: [
                    {
                        text: 'Data Structures',
                    }, {
                        text: 'Global Constants',
                    }, {
                        text: 'Top Level',
                        link: '/en/reference/components/',
                    }, {
                        text: 'Stages',
                        collapsed: true,
                        items: [
                            {
                                text: 'IF - Instruction Fetch',
                                link: '/en/reference/components/stage_if',
                            }, {
                                text: 'ID - Instruction Decode',
                                link: '/en/reference/components/stage_id',
                            }, {
                                text: 'EX - Execute',
                                link: '/en/reference/components/stage_ex',
                            }, {
                                text: 'MEM - Memory Access',
                                link: '/en/reference/components/stage_mem',
                            }, {
                                text: 'WB - Write Back',
                                link: '/en/reference/components/stage_wb',
                            },
                        ],
                    },  {
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
                                text: 'Execution Unit',
                                link: '/en/reference/components/module_execution_unit',
                            }, {
                                text: 'Execution Control Unit',
                                link: '/en/reference/components/module_execution_control_unit',
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
                                text: 'ALU bit',
                                link: '/en/reference/components/rv32i_alu_bit',
                            }, {
                                text: 'Arithmetic and Logical Unit',
                                link: '/en/reference/components/rv32i_alu',
                            }, {
                                text: 'ALU Controller',
                                link: '/en/reference/components/rv32i_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Generics',
                        collapsed: true,
                        items: [
                            {
                                text: 'Adder',
                                link: '/en/reference/components/generic_adder',
                            }, {
                                text: 'Mux 2x1',
                                link: '/en/reference/components/generic_mux_2x1',
                            }, {
                                text: 'Mux 4x1',
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
                            }, //{
                            //    text: 'Signal extender',
                            //    link: '/en/reference/components/generic_signal_extender',
                            //}, {
                            //    text: 'Flip Flop',
                            //    link: '/en/reference/components/generic_flip_flop',
                            //}, {
                            //    text: 'Debounce',
                            //    link: '/en/reference/components/generic_debounce',
                            //}, {
                            //    text: 'Edge Detector',
                            //    link: '/en/reference/components/generic_edge_detector',
                            //}, {
                            //    text: 'Counter',
                            //    link: '/en/reference/components/generic_counter',
                            //},
                        ],
                    },
                ],
            }, {
                text: 'Specification',
                items: [
                    {
                        text: 'instruction Set Architecture',
                        link: '/en/reference/isa/',
                    }, {
                        text: 'Pseudo-Instructions',
                        link: '/en/reference/isa/pseudo',
                    },
                ],
            }, {
                text: 'Tests',
                items: [
                    {
                        text: 'Structure',
                    }, {
                        text: 'Utils',
                    },
                ],
            },
        ],
    },
} satisfies DefaultTheme.Config
