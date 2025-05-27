#Crie um programa que solicite o nome, sobrenome e idade de uma pessoal e imprima no formato:
#”NOME: Fulano de Tal”
#”IDADE: 21”
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Sua idade: "))
print(f"NOME: {nome} {sobrenome}")
print(f"IDADE: {idade}")