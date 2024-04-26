import sys

def create_GENERIC_ROM(memory):

    with open(memory, "r") as mem_file: 
        mem_lines = mem_file.readlines()

    mem_file.close()
    index_instruction = 0
    list_instructions_tmp = []
    list_instructions = [
        "00000001",
        "00000010",
        "00000100",
        "00001000",
        "00010000",
        "00100000",
        "01000000",
        "10000000",
    ]
    for inst in list_instructions:
        instruction_tmp = '        tmp(' + str(index_instruction) + ') := "' + inst + '";\n'
        list_instructions_tmp.append(instruction_tmp)
        index_instruction += 1
    
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
#    memory = sys.argv[1]
#    create_GENERIC_ROM(memory)
#    
#
#if __name__ == "__main__":
#    main()