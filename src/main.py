# Montador RISC-V (versão simplificada)
# O trabalho consiste na implementação de uma versão simplificada de um montador RISC-V de acordo com as especificações.

from assembler import*
import sys

def main():
    if len(sys.argv) < 2:
        print("python3 main.py <filename>.asm [-o <outputFilename>]")
        return
    inputFilename = sys.argv[1]
    if len(sys.argv) >= 4 and sys.argv[2] == "-o":
        outputFilename = sys.argv[3]
        writer(inputFilename, outputFilename)
    else:
        reader(inputFilename)

if __name__ == "__main__":
    main()