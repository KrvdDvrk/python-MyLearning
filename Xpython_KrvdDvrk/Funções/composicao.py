#!/usr/bin/env python3

names = ["Dvrk", "João", "Fernando", "Juliana", "Briar"]

# Substituir o loop abaixo para um função:
#for name in names:
#    if name.lower().startswith("j"):
#        print(name)

# TODO: usar lambdas

def starts_with_j(text):
    return text[0].lower() == "j"
    #return text.startswith(("j","J"))

print(*list(filter(starts_with_j, names)))
