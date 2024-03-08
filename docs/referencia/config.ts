import type { DefaultTheme } from 'vitepress/types'


export default {
    sidebar: {
        '/referencia/': [
            {
                text: 'Instruções',
                collapsed: false,
                items: [
                    {
                        text: 'Shifts',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>SLL</code>',
                                link: '/referencia/isa/#SLL',
                            }, {
                                text: '<code>SLLI</code>',
                                link: '/referencia/isa/#SLLI',
                            }, {
                                text: '<code>SRL</code>',
                                link: '/referencia/isa/#SRL',
                            }, {
                                text: '<code>SRLI</code>',
                                link: '/referencia/isa/#SRLI',
                            }, {
                                text: '<code>SRA</code>',
                                link: '/referencia/isa/#SRA',
                            }, {
                                text: '<code>SRAI</code>',
                                link: '/referencia/isa/#SRAI',
                            },
                        ],
                    }, {
                        text: 'Arithmetic',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>ADD</code>',
                                link: '/referencia/isa/#ADD',
                            }, {
                                text: '<code>ADDI</code>',
                                link: '/referencia/isa/#ADDI',
                            }, {
                                text: '<code>SUB</code>',
                                link: '/referencia/isa/#SUB',
                            }, {
                                text: '<code>LUI</code>',
                                link: '/referencia/isa/#LUI',
                            }, {
                                text: '<code>AUIPC</code>',
                                link: '/referencia/isa/#AUIPC',
                            },
                        ],
                    }, {
                        text: 'Logical',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>XOR</code>',
                                link: '/referencia/isa/#XOR',
                            }, {
                                text: '<code>XORI</code>',
                                link: '/referencia/isa/#XORI',
                            }, {
                                text: '<code>OR</code>',
                                link: '/referencia/isa/#OR',
                            }, {
                                text: '<code>ORI</code>',
                                link: '/referencia/isa/#ORI',
                            }, {
                                text: '<code>AND</code>',
                                link: '/referencia/isa/#AND',
                            }, {
                                text: '<code>ANDI</code>',
                                link: '/referencia/isa/#ANDI',
                            },
                        ],
                    }, {
                        text: 'Compare',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>SLT</code>',
                                link: '/referencia/isa/#SLT',
                            }, {
                                text: '<code>SLTI</code>',
                                link: '/referencia/isa/#SLTI',
                            }, {
                                text: '<code>SLTU</code>',
                                link: '/referencia/isa/#SLTU',
                            }, {
                                text: '<code>SLTI</code>',
                                link: '/referencia/isa/#SLTI',
                            },
                        ],
                    }, {
                        text: 'Branches',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>BEQ</code>',
                                link: '/referencia/isa/#BEQ',
                            }, {
                                text: '<code>BNE</code>',
                                link: '/referencia/isa/#BNE',
                            }, {
                                text: '<code>BLT</code>',
                                link: '/referencia/isa/#BLT',
                            }, {
                                text: '<code>BGE</code>',
                                link: '/referencia/isa/#BGE',
                            }, {
                                text: '<code>BLTU</code>',
                                link: '/referencia/isa/#BLTU',
                            }, {
                                text: '<code>BGEU</code>',
                                link: '/referencia/isa/#BGEU',
                            },
                        ],
                    }, {
                        text: 'Link',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>JAL</code>',
                                link: '/referencia/isa/#JAL',
                            }, {
                                text: '<code>JALR</code>',
                                link: '/referencia/isa/#JALR',
                            },
                        ],
                    }, {
                        text: 'Synch',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>FENCE</code>',
                                link: '/referencia/isa/#FENCE',
                            }, {
                                text: '<code>FENCE</code>',
                                link: '/referencia/isa/#FENCE',
                            },
                        ],
                    }, {
                        text: 'Enviroment',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>ECALL</code>',
                                link: '/referencia/isa/#ECALL',
                            }, {
                                text: '<code>EBREAK</code>',
                                link: '/referencia/isa/#EBREAK',
                            },
                        ],
                    }, {
                        text: 'Loads',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>LB</code>',
                                link: '/referencia/isa/#LB',
                            }, {
                                text: '<code>LH</code>',
                                link: '/referencia/isa/#LH',
                            }, {
                                text: '<code>LBU</code>',
                                link: '/referencia/isa/#LBU',
                            }, {
                                text: '<code>LHU</code>',
                                link: '/referencia/isa/#LHU',
                            }, {
                                text: '<code>LW</code>',
                                link: '/referencia/isa/#LW',
                            },
                        ],
                    }, {
                        text: 'Stores',
                        collapsed: true,
                        items: [
                            {
                                text: '<code>SB</code>',
                                link: '/referencia/isa/#SB',
                            }, {
                                text: '<code>SH</code>',
                                link: '/referencia/isa/#SH',
                            }, {
                                text: '<code>SW</code>',
                                link: '/referencia/isa/#SW',
                            },
                        ],
                    },
                ],
            }, {
                text: 'Componentes',
                link: '/referencia/componentes/',
                collapsed: false,
                items: [
                    {
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
                            }, {
                                text: 'Pilha',
                                link: '/referencia/componentes/generic_stack',
                            }
                        ],
                    }, {
                        text: 'RV32I',
                        collapsed: true,
                        items: [
                            {
                                text: 'Bit da ULA',
                                link: '/referencia/componentes/rv32i_alu_bit',
                            }, {
                                text: 'ULA',
                                link: '/referencia/componentes/rv32i_alu',
                            }
                        ],
                    }, {
                        text: 'Módulos',
                        collapsed: true,
                        items: [
                        ],
                    }, {
                        text: 'Blocos',
                        collapsed: true,
                        items: [
                        ],
                    }, 
                ],
            },
        ],
    },
} satisfies DefaultTheme.Config
