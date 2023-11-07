#!/usr/bin/env python3

def transforma_em_maiusculo(texto):
    return texto.upper


def transforma_em_minusculo(texto):
    return texto.lower()


def fivide_por_2(numero):
    return numero // 2


# e nossa função principal

def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)


names = ["Dvrk", "Joao", "Bernardo", "Cintia", "Marcia", "Juca"]

# Imprime lista na ordem alfabética:
print(sorted(names))

# Usando um modo diferente, por exemplo imprimir em ordem de tamanho:
print(sorted(names, key =len))

# Usando de modo diferente, por exemplo pela quantidade de letras "i":
print(sorted(names, key=lambda name: name.count("i")))

# Usando de modo diferente, por exemplo imprime somente o que começa com a letra "b":
print(list(filter(lambda name: name[0].lower() == "b", names)))

# Usando de modo diferente, por exemplo com o "map" colocar "Hello" antes de todos os nomes:
print(list(map(lambda name: "Hello " + name, names)))

# Calculadora

operacao = input("operação [sum, mul, div, sub]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

# Diferença entre a função normal e a lambda, no caso a soma será feita com a função
# A subtração, multiplicação e divisão com a lambda, o resultado será o mesmo.

def soma(a, b):
    return a + b

operacoes = {
    "sum": soma,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

# Vantagens da lambda:
# Ela é uma função anônima, não tem nome, enquanto a soma conseguimos usar ela em
# vários lugares, a lambda só é usada como argumento, então pode-se atribuir ela
# dentro de um dicionário, passar ela como parametro para outra função como map,
# filter ou sorted ...

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é: {resultado}")

