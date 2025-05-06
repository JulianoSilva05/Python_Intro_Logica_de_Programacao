#função print - Exibe na tela (Recebe argumento.)
#\r\n → CRLF (Sistemas Windows)
# \n → LF (Sistemas MacOS)
print(12, 34, end="  ", sep=" * ")  # O argumento end=" " é final do print, posso passar um argumento para finalizar
print(56, 78,sep=" * ")           # Este print será exibido na mesma linha
print(9, 10, sep=" ... ")           # Este print será exibido na mesma linha

idade = 19
#Formas de imprimir na tela
print('Juliano' + ' Silva ' + str( idade) + " anos")#CONCATENAÇÃO #Não tem como concatenar texto com numero
print('Juliano' , ' Silva ' , idade , " anos") #SEPARAÇÃO  
print(f'Juliano  Silva {idade} anos') #INTERPOLAÇÃO