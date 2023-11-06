#!/usr/bin/env python3

import time

def imprime_nome(nome, sobrenome):
    # escopo local {nome: .., sobrenome: ..}
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Dvrk", "Krvd")
imprime_nome("Linus", "Torvalds")

#ou

def imprime_nome(nome, sobrenome="Sabugosa"):
    # escopo local {nome: .., sobrenome: ..}
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Dvrk", "Krvd")
imprime_nome("Linus")

#____

def conecta(host, timeout=10):
    print(f"conectando com {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("Erro ao conectar")

conecta("localhost", 5)

#ou

def conecta(host, timeout=10):
    print(f"conectando com {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("Erro ao conectar")

conecta("localhost")
