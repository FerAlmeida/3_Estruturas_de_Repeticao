convidados = ["Maria", "Gabriel", "Fernando", "Fernanda", "Vinicius", "Ana",  "Lucas","Tatiane"]

for convidado in convidados:
    print(convidado)

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

for i in range(8):
    print(i)

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

for i in range(1,6):
    print(i)

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

numeros = []                            # criada uma lista vazia

for i in range(0, 41):
    numeros.append(i)                   # solicitado para adicionar os 50 elementos na lista vazia
print(numeros)

usuario = {"nome":"Fernando",
           "tipo de acesso":"Administrador",
           "nivel de acesso": 1}

for valor in usuario.values():
    print(valor)

usuario = {"nome":"Fernando",
           "tipo de acesso":"Administrador",
           "nivel de acesso": 1}

for chave in usuario.keys():
    print(chave)

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

convidados = ["Maria", "Gabriel", "Fernando", "Fernanda", "Vinicius", "Ana",  "Lucas","Tatiane"]

for convidado in convidados:
    print(f"Seja muito bem vindo(a) {convidado}")

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

# Estrutura condicional - Comando if

"""
Operadores Aritiméticos 
- soma: +
- subtração: -
- multiplicação: *
- divisão: /
- potenciação: **

Operadores Relacionais
- igual: ==
- maior: >
- maior igual: >=
- menor: <
- menor igual: <=

"""

idade = 18

if idade >= 18:
    print("Pode dirigir!")

idade = 10

if idade >= 18:
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

idades = [12, 45, 23, 67, 5, 6, 90, 2, 3, 34, 25, 17, 19]     # idade compatível para consumo de bebida alcoólica

for idade in idades:
    print(f"Idade: {idade} anos: ")
    if idade >= 21:
        print("Pela sua idade, você pode fazer consumo de bebida alcoólica. Aprecie com moderação!")
    else:
        print("Sua idade não permite que você faça uso de bebida alcoólica.Respeite as leis de consumo!")