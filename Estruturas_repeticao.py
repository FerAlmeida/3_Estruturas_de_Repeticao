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