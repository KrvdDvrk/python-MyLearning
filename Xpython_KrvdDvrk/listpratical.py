#Modo principall: users = []
#Outros:
#
#type(users)
#lists
#
#users = list()
#
#type(users)
#list
#_______________________________________________

print("1º")
users = []
users. append("Dvrk")
print(users)
print()
users.append("João")
print(users)
print()
users.append("Alice")
print(users)
print()
#Inserindo em uma posição específica
users.insert(0, "Maria")
print(users)
print()
users.insert(2, "Kolina")
print(users)
print()
#Para remover
users.remove("Alice")
print(users)
print()

#Usando o head, body, tail
head, *body, tail = users
print(head)
print(tail)
print(body)
print()

#Somar/juntar listas

users2 = ["Carlos", "Mario", "José"]
print(users + users2)

#Inserindo uma lista em outra
users.extend(users2)
print(users)
print()

#Inserindo uma lista em outra, modo +=
users3 = ["Medeiros", "Gabe"]

users += users3
print(users)
print()

# modo += pode também adicionar direto na lista
users += ["Léo"]
print(users)
print()

#Para contar quantos itens repetidos tem na lista ... vou adicionar mais 2 dvrk e depois contar.
users += ["Dvrk", "Dvrk"]
print(users)
print()

print('O nome "Dvrk" se repete: ')
print(users.count("Dvrk"), " vezes.")
print()

#Tirar os elementos do fim da lista, um a um.
users.pop()
users.pop()
users.pop()

print(users)
print()

#Operação com lista
resultado = []
for x in range(9):
    resultado.append(x * 4)
print(resultado)
print()

#Para identificar se há algum valor na lista
print("O número 22 está na lista acima?")

print(22 in resultado)

print("O número 24 está na lista acima?")
print(24 in resultado)
print()


