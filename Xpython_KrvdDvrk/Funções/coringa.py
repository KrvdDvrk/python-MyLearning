#!/usr/bin/env python3

"""def soma(a, b):
    return a + b

soma(1, 3)
soma(1, b=3)

def hello(nome, sobrenome="Sabugosa"):
    print(f"Hello {nome}, {sobrenome}")

hello("Dvrk", "Krvd")
hello("Dvrk", sobrenome="Krvd")
hello(sobrenome="Krvd", nome="Dvrk")
hello("Dvrk") """

# JEITO CORINGA AGORA:

# def funcao(*args):
    # Faz um empacotamento
    # print(args)

# SOLID - Single Responsability

def funcao(*args, timeout=10, **options):
    for item in args:
        print(item)
    print(options)

    print(f"timeout {timeout}")

funcao("Dvrk",
       1,
       True,
       timeout=90,
       nome="Maria",
       cidade="Viana",
       data="hoje",
       banana=1,
       panela=3,
       teclado=True,
)
