add x2, x0, x1
sw x5, 40(x6)
lw x5, 40(x6)
beq x5, x6, 100
lui x5, 100
jal x5, 100