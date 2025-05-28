#Crie um programa que solicite o nome, e o ano de nascimento de uma pessoal, e imprima no formato:
# ”NOME: Fulano de Tal”
# ”IDADE: 21”
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Qual seu ano de nascimento: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento
print(f"NOME: {nome}")
print(f"IDADE: {idade}")
