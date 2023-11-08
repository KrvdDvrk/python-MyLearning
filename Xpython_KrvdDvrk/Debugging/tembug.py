#!/usr/bin/env python3

# PTB - PYTHON DEBUGGER
# Para usar essa ferramenta do próprio python
# > python -m pdb tembug.py

# Ferramenta gráfica de debugging
# > pip install pubd
# Para abrir
# > python -m pudb tembug.py

# PROBLEMA 01

def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas"""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõôâéáíó":
            final_word = letter * 2
        else:
            final_word = letter
    return final_word

print(repete_vogal("banana"))

# FORMA DE ENTRAR NO DEBUGGER COM BREAKPOINT DENTRO DO CODIGO
# IMPORT PDB

"""
def repete_vogal(word):
    # Retorna a palavra com as vogais repetidas
    final_word = ""
    for letter in word:
        breakpoint()
        # OU: import pdb;pdb.set_trace()
        # OU: __import__("pdb").set_trace()
        if letter.lower() in "aeiouãõôâéáíó":
            final_word = letter * 2
        else:
            final_word = letter
    return final_word

print(repete_vogal("banana"))
"""


"""
# PROBLEMA 02

def repete_vogal(word):
    # Retorna a palavra com as vogais repetidas
    final_word = ""
    for index, letter in enumerate(word):
        # usamos enumerate para ajudar a sabermos as voltas do loop
        print(f"{index=} {letter=}")
        if letter.lower() in "aeiouãõôâéáíó":
            final_word = letter * 2
        else:
            final_word = letter

        print(f"{final_word=}")
    return final_word


print(repete_vogal("banana"))
"""
