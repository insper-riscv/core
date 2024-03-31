import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/reference/': [
            {
                text: 'Componentes',
                link: '/reference/components/',
                collapsed: false,
                items: [
                    {
                        text: 'Estágios',
                        collapsed: true,
                        items: [
                            {
                                text: 'IF - Busca Instrução',
                                link: '/reference/components/stage_if',
                            }, {
                                text: 'ID - Decodifica Instrução',
                                link: '/reference/components/stage_id',
                            }, {
                                text: 'EX - Executa',
                                link: '/reference/components/stage_ex',
                            }, {
                                text: 'MEM - Acessa à Memória',
                                link: '/reference/components/stage_mem',
                            }, {
                                text: 'WB - Escreve o Retorno',
                                link: '/reference/components/stage_wb',
                            },
                        ],
                    },  {
                        text: 'Módulos',
                        collapsed: true,
                        items: [
                            {
                                text: 'Arquivo de Registradores',
                                link: '/reference/components/module_register_file',
                            },{
                                text: 'Contador de Programa',
                                link: '/reference/components/module_program_counter',
                            }, {
                                text: 'Escrita de Retorno',
                                link: '/reference/components/module_write_back',
                            }, {
                                text: 'Unidade de Controle',
                                link: '/reference/components/module_control_unit',
                            }, {
                                text: 'Unidade de Execução',
                                link: '/reference/components/module_execution_unit',
                            }, {
                                text: 'Unidade de Controle de execução',
                                link: '/reference/components/module_execution_control_unit',
                            },
                        ],
                    }, {
                        text: 'RV32I',
                        collapsed: true,
                        items: [
                            {
                                text: 'Decodificador de instruções',
                                link: '/reference/components/rv32i_instruction_decoder',
                            }, {
                                text: 'Arquivo de Registradores',
                                link: '/reference/components/rv32i_register_file',
                            }, {
                                text: 'Bit da ULA',
                                link: '/reference/components/rv32i_alu_bit',
                            }, {
                                text: 'ULA',
                                link: '/reference/components/rv32i_alu',
                            }, {
                                text: 'Controlador da ULA',
                                link: '/reference/components/rv32i_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Genéricos',
                        collapsed: true,
                        items: [
                            {
                                text: 'Somador',
                                link: '/reference/components/generic_adder',
                            }, {
                                text: 'Multiplexador 2x1',
                                link: '/reference/components/generic_mux_2x1',
                            }, {
                                text: 'Multiplexador 4x1',
                                link: '/reference/components/generic_mux_4x1',
                            }, {
                                text: 'RAM',
                                link: '/reference/components/generic_ram',
                            }, {
                                text: 'ROM',
                                link: '/reference/components/generic_rom',
                            }, {
                                text: 'Registrador',
                                link: '/reference/components/generic_register',
                            }, //{
                            //    text: 'Extensor de sinal',
                            //    link: '/reference/components/generic_signal_extender',
                            //}, {
                            //    text: 'Flip Flop',
                            //    link: '/reference/components/generic_flip_flop',
                            //}, {
                            //    text: 'Debounce',
                            //    link: '/reference/components/generic_debounce',
                            //}, {
                            //    text: 'Detector de borda',
                            //    link: '/reference/components/generic_edge_detector',
                            //}, {
                            //    text: 'Contador',
                            //    link: '/reference/components/generic_counter',
                            //},
                        ],
                    },
                ],
            }, {
                text: 'Instruções',
                link: '/reference/isa/',
            }, {
                text: 'Pseudo-instruções',
                link: '/reference/isa/pseudo',
            },
        ],
    },
} satisfies DefaultTheme.Config
