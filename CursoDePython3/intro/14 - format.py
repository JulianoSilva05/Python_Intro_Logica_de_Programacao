a = "A"
b = "B"
c = 1.1

formato = "a={nome1} b={nome2} c={nome3:.2f} d={nome3}".format(
    5, #5 = argumento
    nome1 = a,#nome1 = parametro
    nome2 = b,
    nome3 = c
    )

print(formato)