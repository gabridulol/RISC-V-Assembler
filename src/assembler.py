# {lb, sb, add, and, ori, sll, bne}

# Source: Computer Organization and Design RISC-V Edition: The Hardware Software Interface

# R-type (Arithmetic instructions format)
# funct7 rs2 rs1 funct3 rd opcode

# I-type (Loads & immediate arithmetic)
# immediate[11:0] rs1 funct3 rd opcode

# S-type (Stores)
# immed[11:5] rs2 rs1 funct3 imm[4:0] opcode

# SB-type (Conditional branches format)
# immed[12] immed[10:5] rs2 rs1 funct3 imm[4:1] imm[11] opcode

# UJ-type (Unconditional jumps format)
# immed[20] immed[10:1] immed[11] immed[19:12] rd opcode

# U-type (Upper immediate format)
# immed[31:12] rd opcode

# PS-type (New for pseudo-instructions format)
# mv -> addi / R-type
# li -> addi / I-type
# j -> jal / UJ-type
# la -> lui + addi / U-type + I-type

def instruction(instruction):
    instructionDictionary = {
        # R-type
        "add": "R",
        "sub": "R",
        "sll": "R",
        "xor": "R",
        "srl": "R",
        "sra": "R",
        "or": "R",
        "and": "R",
        "lr.d": "R",
        "sc.d": "R",

        # I-type
        "lb": "Il",
        "lh": "Il",
        "lw": "Il",
        "ld": "Il",
        "lbu": "Il",
        "lhu": "Il",
        "lwu": "Il",
        "addi": "Ii",
        "slli": "Ii",
        "xori": "Ii",
        "srli": "Ii",
        "srai": "Ii",
        "ori": "Ii",
        "andi": "Ii",
        "jalr": "Ij",

        # S-type
        "sb": "S",
        "sh": "S",
        "sw": "S",
        "sd": "S",

        # SB-type
        "beq": "SB",
        "bne": "SB",
        "blt": "SB",
        "bge": "SB",
        "bltu": "SB",
        "bgeu": "SB",

        # UJ-type
        "jal": "UJ",

        # U-type
        "lui": "U",

        # PS-type
        # "mv": "PS",
        # "li": "PS",
        # "j": "PS",
        # "la": "PS"
    }
    instructionType = instructionDictionary.get(instruction)
    if instructionType == None:
        return f"Invalid instruction '{instruction}'"
    return instructionType

def opcode(instructionType):
    opcodeDictionary = {
        "R": "0110011",
        "Il": "0000011",
        "Ii": "0010011",
        "Ij": "1100111",
        "S": "0100011",
        "SB": "1100111",
        "UJ": "1101111",
        "U": "0110111",
        # "PS": "PS"
    }
    opcodeValue = opcodeDictionary.get(instructionType)
    if opcodeValue == None:
        return f"Invalid instruction {instructionType}-type "
    return opcodeValue

def funct3(instruction):
    funct3Dictionary = {
        "add": "000",
        "sub": "000",
        "sll": "001",
        "xor": "100",
        "srl": "101",
        "sra": "101",
        "or": "110",
        "and": "111",
        "lr.d": "011",
        "sc.d": "011",
        "lb": "000",
        "lh": "001",
        "lw": "010",
        "ld": "011",
        "lbu": "100",
        "lhu": "101",
        "lwu": "110",
        "addi": "000",
        "slli": "001",
        "xori": "100",
        "srli": "101",
        "srai": "101",
        "ori": "110",
        "andi": "111",
        "jalr": "000",
        "sb": "000",
        "sh": "001",
        "sw": "010",
        "sd": "111",
        "beq": "000",
        "bne": "001",
        "blt": "100",
        "bge": "101",
        "bltu": "110",
        "bgeu": "111",
    }
    funct3Value = funct3Dictionary.get(instruction)
    if funct3Value == None:
        return f"Invalid instruction '{instruction}'"
    return funct3Value

def funct7(instruction):
    funct7Dictionary = {
        "add": "0000000",
        "sub": "0100000",
        "sll": "0000000",
        "xor": "0000000",
        "srl": "0000000",
        "sra": "0000000",
        "or": "0000000",
        "and": "0000000",
        "lr.d": "0001000",
        "sc.d": "0001100",
        # "slli": "000000",
        # "srli": "000000",
        # "srai": "010000",
    }
    funct7Value = funct7Dictionary.get(instruction)
    if funct7Value == None:
        return f"Invalid instruction '{instruction}'"
    return funct7Value

def immediate(immediate):
    if (immediate.startswith("0x") or immediate.startswith("-0x")):
        immediate = int(immediate, 16)
    else:
        immediate = int(immediate)
    if (immediate >= 0):
        binary = format(immediate, '032b')
        return binary[::-1]
    else:
        binary = format((1 << 32) + immediate, '032b')
        return binary[::-1]

def register(register):
    registerDictionary = {
        "x0": "00000",
        "x1": "00001",
        "x2": "00010",
        "x3": "00011",
        "x4": "00100",
        "x5": "00101",
        "x6": "00110",
        "x7": "00111",
        "x8": "01000",
        "x9": "01001",
        "x10": "01010",
        "x11": "01011",
        "x12": "01100",
        "x13": "01101",
        "x14": "01110",
        "x15": "01111",
        "x16": "10000",
        "x17": "10001",
        "x18": "10010",
        "x19": "10011",
        "x20": "10100",
        "x21": "10101",
        "x22": "10110",
        "x23": "10111",
        "x24": "11000",
        "x25": "11001",
        "x26": "11010",
        "x27": "11011",
        "x28": "11100",
        "x29": "11101",
        "x30": "11110",
        "x31": "11111"
    }
    registerValue = registerDictionary.get(register)
    if registerValue == None:
        return f"Invalid register '{register}'"
    return registerValue

def writer(inputFilename, outputFilename):
    inputFile = open("src/inputs/" + inputFilename, "r")
    outputFile = open("src/outputs/" + outputFilename + ".asm", "w")
    for instruction in inputFile:
        assemblerWriter(formater(instruction), outputFile)
    inputFile.close()
    outputFile.close()

def assemblerWriter(instructionLine, file):
    if instruction(instructionLine[0]) == "R":
        file.write(f"{funct7(instructionLine[0])}{register(instructionLine[3])}{register(instructionLine[2])}{funct3(instructionLine[0])}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n")
    elif instruction(instructionLine[0]) == "Il" or instruction(instructionLine[0]) == "Ij":
        file.write(f"{immediate(instructionLine[2])[0:12][::-1]}{register(instructionLine[3])}{funct3(instructionLine[0])}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n")
    elif instruction(instructionLine[0]) == "Ii":
        file.write(f"{immediate(instructionLine[3])[0:12][::-1]}{register(instructionLine[2])}{funct3(instructionLine[0])}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n")
    elif instruction(instructionLine[0]) == "S":
        file.write(f"{immediate(instructionLine[2])[5:12][::-1]}{register(instructionLine[1])}{register(instructionLine[3])}{funct3(instructionLine[0])}{immediate(instructionLine[2])[0:5][::-1]}{opcode(instruction(instructionLine[0]))}\n")
    elif instruction(instructionLine[0]) == "SB":
        file.write(f"{immediate(instructionLine[3])[12][::-1]}{immediate(instructionLine[3])[5:11][::-1]}{register(instructionLine[2])}{register(instructionLine[1])}{funct3(instructionLine[0])}{immediate(instructionLine[3])[1:5][::-1]}{immediate(instructionLine[3])[11][::-1]}{opcode(instruction(instructionLine[0]))}\n")
    elif instruction(instructionLine[0]) == "UJ": # Verificar
        file.write(f"{immediate(instructionLine[2])[20][::-1]}{immediate(instructionLine[2])[1:11][::-1]}{immediate(instructionLine[2])[11][::-1]}{immediate(instructionLine[2])[12:20][::-1]}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n")
    elif instruction(instructionLine[0]) == "U": # Verificar
        file.write(f"{immediate(instructionLine[2])[12:32][::-1]}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n")
    # elif instruction(instructionLine[0]) == "PS":
    #     file.write("mv -> addi / R-type\nli -> addi / I-type\nj -> jal / UJ-type\nla -> lui + addi / U-type + I-type\n")

def reader(filename):
    inputFile = open("src/inputs/" + filename, "r")
    print("RISC-V Assembler")
    for instruction in inputFile:
        print(instruction.strip())
        print(assemblerReader(formater(instruction)).strip())
    inputFile.close()

def assemblerReader(instructionLine):
    if instruction(instructionLine[0]) == "R":
        return f"{funct7(instructionLine[0])}{register(instructionLine[3])}{register(instructionLine[2])}{funct3(instructionLine[0])}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n"
    elif instruction(instructionLine[0]) == "Il" or instruction(instructionLine[0]) == "Ij":
        return f"{immediate(instructionLine[2])[0:12][::-1]}{register(instructionLine[3])}{funct3(instructionLine[0])}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n"
    elif instruction(instructionLine[0]) == "Ii":
        return f"{immediate(instructionLine[3])[0:12][::-1]}{register(instructionLine[2])}{funct3(instructionLine[0])}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n"
    elif instruction(instructionLine[0]) == "S":
        return f"{immediate(instructionLine[2])[5:12][::-1]}{register(instructionLine[1])}{register(instructionLine[3])}{funct3(instructionLine[0])}{immediate(instructionLine[2])[0:5][::-1]}{opcode(instruction(instructionLine[0]))}\n"
    elif instruction(instructionLine[0]) == "SB":
        return f"{immediate(instructionLine[3])[12][::-1]}{immediate(instructionLine[3])[5:11][::-1]}{register(instructionLine[2])}{register(instructionLine[1])}{funct3(instructionLine[0])}{immediate(instructionLine[3])[1:5][::-1]}{immediate(instructionLine[3])[11][::-1]}{opcode(instruction(instructionLine[0]))}\n"
    elif instruction(instructionLine[0]) == "UJ": # Verificar
        return f"{immediate(instructionLine[2])[20][::-1]}{immediate(instructionLine[2])[1:11][::-1]}{immediate(instructionLine[2])[11][::-1]}{immediate(instructionLine[2])[12:20][::-1]}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n"
    elif instruction(instructionLine[0]) == "U": # Verificar
        return f"{immediate(instructionLine[2])[12:32][::-1]}{register(instructionLine[1])}{opcode(instruction(instructionLine[0]))}\n"
    # elif instruction(instructionLine[0]) == "PS":
    #     return "mv -> addi / R-type\nli -> addi / I-type\nj -> jal / UJ-type\nla -> lui + addi / U-type + I-type\n"

def formater(instruction):
    instruction = instruction.strip()
    instruction = instruction.replace(",", "")
    instruction = instruction.replace("(", " ")
    instruction = instruction.replace(")", "")
    instruction = instruction.split()
    return instruction


