# Variaveis são usadas para salvar algo na memória do computador.
# PEP8: inicie varáveis com letras minúsculas, pode usa números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável).
#Variaveis são feitas para usar valor em outros lugares = referencia
nome = "Juliano Fernando da Silva "
print(nome)
soma_dois_mais_dois = 2 + 2
print(nome , soma_dois_mais_dois)

print("\n*************************************\n")

print(int("1"), type(int("1")))# não é legal repetir as coisas em programação, isso pode resultar em um problema de valores divergentes
#Exemplo, imagina que você possui um salario de $10.000,00.
# A empresa que converte os valores para real usa um formula manual para converter.
salarioJuliano = 10000.00
print(f"Salário do Juliano convertido = {salarioJuliano * 5.89}")

salarioJulia = 5000.00
print(f"Salário da Julia convertido = {salarioJulia * 5.99}")

print("\n*************************************\n")

#Chegar se é maior de idade
nome = "Juliano"
idade = 21
maior_de_idade = idade >= 18

print(f"Nome: {nome} é maior de idade: {maior_de_idade}")