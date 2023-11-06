#!/usr/bin/env python3

# NAMESPACES ->
# L.E.G.B ->
# LOCAL está contido em ENVOLVENTE ->
# ENVOLVENTE está contido em GLOBAL ->
# GLOBAL está contido em BUILT-IN.

nome = "Global"

def funcao():
    nome = "Local"
    print("Nome Local:", nome)
    nome = globals()["nome"]
    print("Nome Global:", nome)

funcao()
