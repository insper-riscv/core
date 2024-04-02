import sys

def create_binary_instructions(assembly, memory):
    instruction_opcode = {
        "lui"  : "0110111",
        "addi" : "0010011",
        "jal"  : "1101111",
    }

    instruction_funct3 = {
        "addi" : "000",
        "add"  : "000",
    }

    instruction_funct7 = {
        "add" : "0000000",
    }

    instruction_type = {
        "lui"  : "U",
        "addi" : "I",
        "jal"  : "J",
    }

    with open(assembly, "r") as asm_file: 
        asm_lines = asm_file.readlines()

    with open(memory, "r") as mem_file: 
        mem_lines = mem_file.readlines()

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

            immediate = "{0:012b}".format(int(line_list[3]))
            rs1 = "{0:05b}".format(int(line_list[2][1:]))
            funct3 = instruction_funct3[line_list[0]]
            rd = "{0:05b}".format(int(line_list[1][1:]))
            opcode = instruction_opcode[line_list[0]]
            instruction = immediate + rs1 + funct3 + rd + opcode
            list_instructions.append(instruction)

        if line_type == "U":
            immediate = "{0:020b}".format(int(line_list[2]))
            rd = "{0:05b}".format(int(line_list[1][1:]))
            opcode = instruction_opcode[line_list[0]]
            instruction = immediate + rd + opcode
            list_instructions.append(instruction)
        
        if line_type == "R":
            funct7 = instruction_funct7[line_list[0]]
            rs2 = "{0:05b}".format(int(line_list[3][1:]))
            rs1 = "{0:05b}".format(int(line_list[2][1:]))
            funct3 = instruction_funct3[line_list[0]]
            rd = "{0:05b}".format(int(line_list[1][1:]))
            opcode = instruction_opcode[line_list[0]]
            instruction = funct7 + rs2 + rs1 + funct3 + rd + opcode
            list_instructions.append(instruction)

        if line_type == "J":
            immediate = "{0:020b}".format(int(line_list[2]))
            imm_20 = immediate[0]
            imm_10_1 = immediate[10:20]
            imm_11 = immediate[9]
            imm_19_12 = immediate[1:9]
            rd = "{0:05b}".format(int(line_list[1][1:]))
            opcode = instruction_opcode[line_list[0]]
            instruction = imm_20 + imm_10_1  + imm_11 + imm_19_12 + rd + opcode
            list_instructions.append(instruction)

        if line_type == "S":
            line_list[2] = line_list[2].replace(")", "")
            offset_list = line_list[2].split("(")
            line_list = [line_list[0], line_list[1], offset_list[1], offset_list[0]]

            immediate = "{0:012b}".format(int(line_list[3]))
            imm_11_5 = immediate[0:7]
            rs2 = "{0:05b}".format(int(line_list[1][1:]))
            rs1 = "{0:05b}".format(int(line_list[2][1:]))
            funct3 = instruction_funct3[line_list[0]]
            imm_4_0 = immediate[7:12]
            opcode = instruction_opcode[line_list[0]]
            instruction = imm_11_5 + rs2 + rs1 + funct3 + imm_4_0 + opcode
            list_instructions.append(instruction)

        if line_type == "B":
            immediate = "{0:012b}".format(int(line_list[3]))
            imm_12 = immediate[0]
            imm_10_5 = immediate[2:8]
            rs2 = "{0:05b}".format(int(line_list[2][1:]))
            rs1 = "{0:05b}".format(int(line_list[1][1:]))
            funct3 = instruction_funct3[line_list[0]]
            imm_11 = immediate[1]
            imm_4_1 = immediate[8:12]
            opcode = instruction_opcode[line_list[0]]
            instruction = imm_12 + imm_10_5 + rs2 + rs1 + funct3 + imm_11 + imm_4_1 + opcode
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


#def main():
#    assembly = sys.argv[1]
#    memory = sys.argv[2]
#    create_binary_instructions(assembly, memory)
#    
#
#if __name__ == "__main__":
#    main()