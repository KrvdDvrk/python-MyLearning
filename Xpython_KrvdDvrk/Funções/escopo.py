#!/usr/bin/env python3

# NAMESPACES ->
# L.E.G.B ->
# LOCAL está contido em ENVOLVENTE ->
# ENVOLVENTE está contido em GLOBAL ->
# GLOBAL está contido em BUILT-IN.

# aqui começa o escopo global
nome = "Global"
numero = 1
flag = True

def funcao():
    # aqui começa o escopo local da funcao
    nome = "Local"

    def funcao_interna(): # inner function
        # aqui começa o escopo local da funcao interna
        nome = "Interna"

        print("Escopo local da funcao interna: ", locals())
        print("*" * 30)

        print(nome)
        return nome
        # aqui termina o escopo local da funcao interna

    print("Escopo local da funcao: ", locals())

    print("-" * 30)
    funcao_interna()

    return "nome"
    # aqui termina o escopo local da funcao

print("Escopo global do programa", globals())
print("-" * 30)

funcao ()
print(nome)
# aqui termina o escopo global
