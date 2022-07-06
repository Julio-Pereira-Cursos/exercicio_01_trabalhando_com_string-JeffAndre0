"""
Programa em Python que solicite as informações de três pessoas, como nome, idade, peso, altura.
Apresenta na tela estas informações de modo que permaneçam alinhados verticalmente com formatação de interpolação.
"""

count = 0
texto=""
while(count < 2):
    nome01 = input("Informe seu nome: ")
    idade01 = input("Informe sua idade: ")
    peso01 = input("Informe seu peso: ")
    altura01 = input("Informe sua altura: ")
    texto += f'Nome: {nome01:20}, Idade: {idade01:2}, Peso: {peso01:6}, Altura:{altura01:4}' +'\n'
    count= count + 1
print(texto)