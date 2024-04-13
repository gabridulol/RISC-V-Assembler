# My instructions {lb, sb, add, and, ori, sll, bne}

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

        # PS-type - IMPLEMENTAÇÃO DIFE
        "mv": "PS",
        "li": "PS",
        "j": "PS",
        "la": "PS"
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
        "SB": "1100011",
        "UJ": "1101111",
        "U": "0110111",
        "PS": "PS"
    }
    opcodeValue = opcodeDictionary.get(instructionType)
    if opcodeValue == None:
        return f"Invalid instruction {instructionType}-type "
    return opcodeValue

def funct3(instruction):

def funct7(instruction):

def immediate(immediate):

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