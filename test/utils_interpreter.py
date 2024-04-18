import sys

instruction_opcode = {
    "lui"    : "0110111",
    "auipc"  : "0010111",
    "sll"    : "0110011",
    "slli"   : "0010011",
    "srl"    : "0110011",
    "srli"   : "0010011",
    "sra"    : "0110011",
    "srai"   : "0010011",
    "add"    : "0110011",
    "addi"   : "0010011",
    "sub"    : "0110011",
    "mul"    : "0110011",
    "mulh"   : "0110011",
    "mulhsu" : "0110011",
    "mulhu"  : "0110011",
    "div"    : "0110011",
    "divu"   : "0110011",
    "rem"    : "0110011",
    "remu"   : "0110011",
    "xor"    : "0110011",
    "xori"   : "0010011",
    "or"     : "0110011",
    "ori"    : "0010011",
    "and"    : "0110011",
    "andi"   : "0010011",
    "slt"    : "0110011",
    "slti"   : "0010011",
    "sltiu"  : "0010011",
    "sltu"   : "0110011",
    "beq"    : "1100011",
    "bne"    : "1100011",
    "blt"    : "1100011",
    "bge"    : "1100011",
    "bltu"   : "1100011",
    "bgeu"   : "1100011",
    "jal"    : "1101111",
    "jalr"   : "1100111",
    "lb"     : "0000011",
    "lh"     : "0000011",
    "lbu"    : "0000011",
    "lhu"    : "0000011",
    "lw"     : "0000011",
    "sb"     : "0100011",
    "sh"     : "0100011",
    "sw"     : "0100011",
}

instruction_funct3 = {
    "sll"    : "001",
    "slli"   : "001",
    "srl"    : "101",
    "srli"   : "101",
    "sra"    : "101",
    "srai"   : "101",
    "add"    : "000",
    "addi"   : "000",
    "sub"    : "000",
    "mul"    : "000",
    "mulh"   : "001",
    "mulhsu" : "010",
    "mulhu"  : "011",
    "div"    : "100",
    "divu"   : "101",
    "rem"    : "110",
    "remu"   : "111",
    "xor"    : "100",
    "xori"   : "100",
    "or"     : "110",
    "ori"    : "110",
    "and"    : "111",
    "andi"   : "111",
    "slt"    : "010",
    "slti"   : "010",
    "sltiu"  : "011",
    "sltu"   : "011",
    "beq"    : "000",
    "bne"    : "001",
    "blt"    : "100",
    "bge"    : "101",
    "bltu"   : "110",
    "bgeu"   : "111",
    "jalr"   : "000",
    "lb"     : "000",
    "lh"     : "001",
    "lbu"    : "100",
    "lhu"    : "101",
    "lw"     : "010",
    "sb"     : "000",
    "sh"     : "001",
    "sw"     : "010",
}

instruction_funct7 = {
    "sll"    : "0000000",
    "slli"   : "0000000",
    "srl"    : "0000000",
    "srli"   : "0000000",
    "sra"    : "0100000",
    "srai"   : "0100000",
    "add"    : "0000000",
    "sub"    : "0100000",
    "mul"    : "0000001",
    "mulh"   : "0000001",
    "mulhsu" : "0000001",
    "mulhu"  : "0000001",
    "div"    : "0000001",
    "divu"   : "0000001",
    "rem"    : "0000001",
    "remu"   : "0000001",
    "xor"    : "0000000",
    "or"     : "0000000",
    "and"    : "0000000",
    "slt"    : "0000000", 
    "sltu"   : "0000000",
}

instruction_type = {
    "lui"    : "U",
    "auipc"  : "U",
    "sll"    : "R",
    "slli"   : "I",
    "srl"    : "R",
    "srli"   : "I",
    "sra"    : "R",
    "srai"   : "I",
    "add"    : "R",
    "addi"   : "I",
    "sub"    : "R",
    "mul"    : "R",
    "mulh"   : "R",
    "mulhsu" : "R",
    "mulhu"  : "R",
    "div"    : "R",
    "divu"   : "R",
    "rem"    : "R",
    "remu"   : "R",
    "xor"    : "R",
    "xori"   : "I",
    "or"     : "R",
    "ori"    : "I",
    "and"    : "R",
    "andi"   : "I",
    "slt"    : "R",
    "slti"   : "I",
    "sltiu"  : "I",
    "sltu"   : "R",
    "beq"    : "B",
    "bne"    : "B",
    "blt"    : "B",
    "bge"    : "B",
    "bltu"   : "B",
    "bgeu"   : "B",
    "jal"    : "J",
    "jalr"   : "I",
    "lb"     : "I",
    "lh"     : "I",
    "lbu"    : "I",
    "lhu"    : "I",
    "lw"     : "I",
    "sb"     : "S",
    "sh"     : "S",
    "sw"     : "S",
}

def create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type):

    with open(assembly, "r") as asm_file: 
        asm_lines = asm_file.readlines()

    asm_file.close()

    with open(memory, "r") as mem_file: 
        mem_lines = mem_file.readlines()

    mem_file.close()

    list_instructions = []
    for line in asm_lines:
        line = line.replace(",", "")
        line = line.replace("\n", "")
        line_list = line.split(" ")

        line_type = instruction_type[line_list[0]]

        if line_type == "I":
            if "(" in line and ")" in line_list[2]:
                line_list[2] = line_list[2].replace(")", "")
                offset_list = line_list[2].split("(")
                line_list = [line_list[0], line_list[1], offset_list[1], offset_list[0]]

            if line_list[0] in instruction_funct7:
                funct7 = instruction_funct7[line_list[0]]
                shamt = "{0:05b}".format(int(line_list[3]))
                if len(shamt) != 5:
                    raise Exception("invalid shamt - type I instruction")
                immediate = funct7 + shamt
            else:
                immediate = "{0:012b}".format(int(line_list[3]))
                if len(immediate) != 12:
                    raise Exception("invalid immediate - type I instruction")
            rs1 = "{0:05b}".format(int(line_list[2][1:]))
            if len(rs1) != 5:
                raise Exception("invalid rs1 - type I instruction")
            funct3 = instruction_funct3[line_list[0]]
            rd = "{0:05b}".format(int(line_list[1][1:]))
            if len(rd) != 5:
                raise Exception("invalid rd - type I instruction")
            opcode = instruction_opcode[line_list[0]]
            instruction = immediate + rs1 + funct3 + rd + opcode
            list_instructions.append(instruction)

        if line_type == "U":
            immediate = "{0:020b}".format(int(line_list[2]))
            if len(immediate) != 20:
                raise Exception("invalid immediate - type U instruction")
            rd = "{0:05b}".format(int(line_list[1][1:]))
            if len(rd) != 5:
                raise Exception("invalid rd - type U instruction")
            opcode = instruction_opcode[line_list[0]]
            instruction = immediate + rd + opcode
            list_instructions.append(instruction)
        
        if line_type == "R":
            funct7 = instruction_funct7[line_list[0]]
            rs2 = "{0:05b}".format(int(line_list[3][1:]))
            if len(rs2) != 5:
                raise Exception("invalid rs2 - type R instruction")
            rs1 = "{0:05b}".format(int(line_list[2][1:]))
            if len(rs1) != 5:
                raise Exception("invalid rs1 - type R instruction")
            funct3 = instruction_funct3[line_list[0]]
            rd = "{0:05b}".format(int(line_list[1][1:]))
            if len(rd) != 5:
                raise Exception("invalid rd - type R instruction")
            opcode = instruction_opcode[line_list[0]]
            instruction = funct7 + rs2 + rs1 + funct3 + rd + opcode
            list_instructions.append(instruction)

        if line_type == "J":
            immediate = "{0:021b}".format(int(line_list[2]))
            if len(immediate) != 21:
                raise Exception("invalid immediate - type J instruction")
            imm_20 = immediate[0]
            imm_10_1 = immediate[10:20]
            imm_11 = immediate[9]
            imm_19_12 = immediate[1:9]
            rd = "{0:05b}".format(int(line_list[1][1:]))
            if len(rd) != 5:
                raise Exception("invalid rd - type J instruction")
            opcode = instruction_opcode[line_list[0]]
            instruction = imm_20 + imm_10_1  + imm_11 + imm_19_12 + rd + opcode
            list_instructions.append(instruction)

        if line_type == "S":
            line_list[2] = line_list[2].replace(")", "")
            offset_list = line_list[2].split("(")
            line_list = [line_list[0], line_list[1], offset_list[1], offset_list[0]]

            immediate = "{0:012b}".format(int(line_list[3]))
            if len(immediate) != 12:
                raise Exception("invalid immediate - type S instruction")
            imm_11_5 = immediate[0:7]
            rs2 = "{0:05b}".format(int(line_list[1][1:]))
            if len(rs2) != 5:
                raise Exception("invalid rs2 - type S instruction")
            rs1 = "{0:05b}".format(int(line_list[2][1:]))
            if len(rs1) != 5:
                raise Exception("invalid rs1 - type S instruction")
            funct3 = instruction_funct3[line_list[0]]
            imm_4_0 = immediate[7:12]
            opcode = instruction_opcode[line_list[0]]
            instruction = imm_11_5 + rs2 + rs1 + funct3 + imm_4_0 + opcode
            list_instructions.append(instruction)

        if line_type == "B":
            immediate = "{0:013b}".format(int(line_list[3]))
            if len(immediate) != 13:
                raise Exception("invalid immediate - type B instruction")
            imm_12 = immediate[0]
            imm_10_5 = immediate[2:8]
            rs2 = "{0:05b}".format(int(line_list[2][1:]))
            if len(rs2) != 5:
                raise Exception("invalid rs2 - type B instruction")
            rs1 = "{0:05b}".format(int(line_list[1][1:]))
            if len(rs1) != 5:
                raise Exception("invalid rs1 - type B instruction")
            funct3 = instruction_funct3[line_list[0]]
            imm_11 = immediate[1]
            imm_4_1 = immediate[8:12]
            opcode = instruction_opcode[line_list[0]]
            instruction = imm_12 + imm_10_5 + rs2 + rs1 + funct3 + imm_4_1 + imm_11 + opcode
            list_instructions.append(instruction)

    index_instruction = 0
    list_instructions_tmp = []
    for inst in list_instructions:
        instruction_tmp = '        tmp(' + str(index_instruction) + ') := "' + inst + '";\n'
        list_instructions_tmp.append(instruction_tmp)
        index_instruction += 4
    
    index_memory_lines = 0
    memory_begin = 0
    memory_end = 0
    for line in mem_lines:
        if "-- start memory" in line:
            memory_begin = index_memory_lines
        elif "-- end memory" in line:
            memory_end = index_memory_lines
        index_memory_lines += 1

    mem_lines_begin = mem_lines[:memory_begin + 1]
    mem_lines_end = mem_lines[memory_end:]
    new_memory_lines = mem_lines_begin + list_instructions_tmp + mem_lines_end

    with open(memory, "w") as new_mem_file: 
        for line_final in new_memory_lines:
            new_mem_file.write(line_final)

    new_mem_file.close()


#def main():
#    assembly = sys.argv[1]
#    memory = sys.argv[2]
#    create_binary_instructions(assembly, memory, instruction_opcode, instruction_funct3, instruction_funct7, instruction_type)
#    
#
#if __name__ == "__main__":
#    main()