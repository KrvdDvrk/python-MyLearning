#!/usr/bin/env python3

# NAMESPACES ->
# L.E.G.B ->
# LOCAL está contido em ENVOLVENTE ->
# ENVOLVENTE está contido em GLOBAL ->
# GLOBAL está contido em BUILT-IN.

contador = 0

def incrementa_contador():
    # aqui começa o escopo local
    # assignment `=` `+=` `-==`
    global contador
    contador += 1

incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)
