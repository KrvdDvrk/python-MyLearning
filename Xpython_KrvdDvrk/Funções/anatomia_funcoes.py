#!/usr/bin/env python3

"""
Este módulo serve apenas de anotação.
"""

# definição ou atribuição
# assinatura + type hints
# documentação / docstring
# codigo
# valor de retorno

# - parametros
# posicional

def nome_da_funcao(a: int, b: int, c: int) -> int:
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    quando o parametro a tiver o valor 10
    vai acontecer x

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

# passagem de argumentos
valor = (nome_da_funcao(1, 2, 3))

#passagem de argumentos nomeados, vantagem é que pode inverter e mudar
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(c=1, b=2, a=3)
valor = nome_da_funcao(b=1, a=2, c=3)

# passagem de argumento mista
# argumentos posicionais antes dos nomeados
valor = nome_da_funcao(1, 2, c=3)
valor = nome_da_funcao(1, c=2, b=3)

print(valor)

###########################################

def outra_funcao(a, b, c):
    """Explica o que ela faz"""
    return a * 2, b * 2, c * 2

# outro_valor = outra_funcao(1, 2, 3)
# print(outro_valor)

# ou

valor1, valor2, valor3 = outra_funcao(1, 2, 3)
print(valor1)
print(valor2)
print(valor3)

# Quero apenas o valor1, como ignorar os outros?

valor1, *_ = outra_funcao(1, 2, 3)
print(valor1)

# Ignorando o valor1, mas ao ignorar, também colocar o restante em uma lista.

valor1, *resto = outra_funcao(1, 2, 3)
print(valor1)
print(resto)

#########################################################

# Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de 2 números."""
    return n1 + n2

# normal
print(soma(10,20))

# argumentos em sequência / posicional
args = (20, 30) # tuple
# print(soma(args[0], args[1]))
#ou
print(soma(*args))

# argumentos dicionario / nomeados
args = {"n2": 90, "n1": 100}
# print(soma(n1=args["n1"], n2=args["n2"]))
# ou
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
]

for item in lista_de_valores_para_somar:
    print(soma(**item))

# Caso eu quissesse inserir na mesma lista uma tupla, o ** não funcionará.
# Sendo assim, será:

lista_de_valores_para_somar2 = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar2:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))

#####################################################

