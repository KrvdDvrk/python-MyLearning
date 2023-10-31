#!/usr/bin/env python3

"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma
das palavras com suas vogais duplicadas.

ex:
python repete_vocal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bolacha
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Boolaachaa
"""

import os
import sys

path = os.curdir
filepath = os.path.join(path, "word.txt")

words = []
while True:
    word = input("Digite uma palavra, ou aperte Enter para sair: ").strip()
    if not word:
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter

        # If ternário alternativo
        # final_word += letter * 2 if letter.lower() in "aeiou" else letter

    words.append(final_word)

print(*words, sep="\n")

