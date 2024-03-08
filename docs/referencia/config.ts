import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/referencia/': [
            {
                text: 'Componentes',
                link: '/referencia/componentes/',
                collapsed: false,
                items: [
                    {
                        text: 'Top Level',
                        link: '/referencia/componentes/top_level'
                    }, {
                        text: 'Genéricos',
                        collapsed: true,
                        items: [
                            {
                                text: 'Somador',
                                link: '/referencia/componentes/generic_adder',
                            }, {
                                text: 'Contador',
                                link: '/referencia/componentes/generic_counter',
                            }, {
                                text: 'Debounce',
                                link: '/referencia/componentes/generic_debounce',
                            }, {
                                text: 'Detector de borda',
                                link: '/referencia/componentes/generic_edge_detector',
                            }, {
                                text: 'Flip Flop',
                                link: '/referencia/componentes/generic_flip_flop',
                            }, {
                                text: 'MUX 2x1',
                                link: '/referencia/componentes/generic_mux_2x1',
                            }, {
                                text: 'MUX 4x1',
                                link: '/referencia/componentes/generic_mux_4x1',
                            }, {
                                text: 'RAM',
                                link: '/referencia/componentes/generic_ram',
                            }, {
                                text: 'Registrador',
                                link: '/referencia/componentes/generic_register',
                            }, {
                                text: 'Banco de Registradores',
                                link: '/referencia/componentes/generic_registers_bank',
                            }, {
                                text: 'Extensor de sinal',
                                link: '/referencia/componentes/generic_signal_extender',
                            },
                        ],
                    }, {
                        text: 'RV32I',
                        collapsed: true,
                        items: [
                            {
                                text: 'Decodificador de instruções',
                                link: '/referencia/componentes/rv32i_instruction_decoder',
                            }, {
                                text: 'Bit da ULA',
                                link: '/referencia/componentes/rv32i_alu_bit',
                            }, {
                                text: 'ULA',
                                link: '/referencia/componentes/rv32i_alu',
                            }, {
                                text: 'Controlador da ULA',
                                link: '/referencia/componentes/rv32i_alu_controller',
                            },
                        ],
                    }, {
                        text: 'Módulos',
                        collapsed: true,
                        items: [
                        ],
                    }, {
                        text: 'Estágios',
                        collapsed: true,
                        items: [
                            {
                                text: 'Busca Instrução',
                                link: '/referencia/componentes/stage_if',
                            }, {
                                text: 'Decodifica Instrução',
                                link: '/referencia/componentes/stage_id',
                            }, {
                                text: 'Executa',
                                link: '/referencia/componentes/stage_ex',
                            }, {
                                text: 'Acesso a Memória',
                                link: '/referencia/componentes/stage_mem',
                            }, {
                                text: 'Escrita de Resposta',
                                link: '/referencia/componentes/stage_wb',
                            },
                        ],
                    }, 
                ],
            }, {
                text: 'Instruções',
                collapsed: false,
                items: [
                    {
                        text: 'Build',
                        link: '/referencia/isa/#build',
                    }, {
                        text: 'Shift',
                        link: '/referencia/isa/#shift',
                    }, {
                        text: 'Arithmetic',
                        link: '/referencia/isa/#arithmetic',
                    }, {
                        text: 'Logical',
                        link: '/referencia/isa/#logical',
                    }, {
                        text: 'Compare',
                        link: '/referencia/isa/#compare',
                    }, {
                        text: 'Branch',
                        link: '/referencia/isa/#branch',
                    }, {
                        text: 'Link',
                        link: '/referencia/isa/#link',
                    }, {
                        text: 'Loads',
                        link: '/referencia/isa/#loads',
                    }, {
                        text: 'Stores',
                        link: '/referencia/isa/#stores',
                    }, {
                        text: 'Pseudo-instruções',
                        link: '/referencia/isa/pseudo',
                    },
                ],
            },
        ],
    },
} satisfies DefaultTheme.Config
