# Coversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
x = 4
y = 2
z = 3

print("{:.1f}".format( x / y ))
print(f"X / Z = {format( x / z )}")
print(f"X // Z = {format( x // z )}")
print(f"X // Z = {format( x // z )}")

# Tipos diferentes
print(1 + 2)
b = "3"
c = int(b)
print (3  + c) # retorna um erro, python possui tipagem forte
#Tipagem dinâmica: O tipo das variáveis é determinado automaticamente em tempo de execução.
# Tipagem forte: Python não converte tipos automaticamente quando eles são incompatíveis; você precisa fazer isso manualmente.
print(bool(" "))
nome = ""

nome = input("Digite seu nome: ")
print (f"Seu nome é: {nome}")
temNome = bool(nome)
print(temNome)

if (temNome == True):
        print("Tem Nome")
else:
        print("Não tem nome")