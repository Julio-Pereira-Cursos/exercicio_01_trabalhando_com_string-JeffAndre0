"""
Programa em Python que solicite as informações de três pessoas, como nome, idade, peso, altura.
Apresenta na tela estas informações de modo que permaneçam alinhados verticalmente com formatação de interpolação.
"""
nome01 = input("Informe seu nome: ")
idade01 = input("Informe sua idade: ")
peso01 = input("Informe seu peso: ")
altura01 = input("Informe sua altura: ")

nome02 = input("Informe seu nome: ")
idade02 = input("Informe sua idade: ")
peso02 = input("Informe seu peso: ")
altura02 = input("Informe sua altura: ")

nome03 = input("Informe seu nome: ")
idade03 = input("Informe sua idade: ")
peso03 = input("Informe seu peso: ")
altura03 = input("Informe sua altura: ")

print(f'Nome: {nome01:20}, Idade: {idade01:2}, Peso: {peso01:6}, Altura:{altura01:4} ')
print(f'Nome: {nome02:20}, Idade: {idade02:2}, Peso: {peso02:6}, Altura:{altura02:4} ')
print(f'Nome: {nome03:20}, Idade: {idade03:2}, Peso: {peso03:6}, Altura:{altura03:4} ')


# # Via loop
# count = 0
# texto=""
# while(count < 2):
#     nome01 = input("Informe seu nome: ")
#     idade01 = input("Informe sua idade: ")
#     peso01 = input("Informe seu peso: ")
#     altura01 = input("Informe sua altura: ")
#     texto += f'Nome: {nome01:20}, Idade: {idade01:2}, Peso: {peso01:6}, Altura:{altura01:4}' +'\n'
#     count= count + 1
# print(texto)