#!/usr/bin/env python3

import os
import sys

try:
    names = open("names.txt").readlines()
    # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

#OUTROS MODOS DE RESOLVER ERROS:
#try:
#    names = open("names.txt").readlines() # FileNotFoundError
#    1/1 #1/0 # ZeroDivisionError
#    print(names.append) #print(names.banana) # AttributeError
#except FileNotFoundError:
#    print("[Error] File names.txt not found.")
#    sys.exit(1)
#except ZeroDivisionError:
#    print("[Error] You cant divide by zero!!!")
#    sys.exit(1)
#except AttributeError:
#    print("[Error] list doensn't have banana")
#    sys.exit(1)

# Quando não sabemos de fato qual é o erro:
#try:
#    raise RuntimeError("Ocorreu um erro")
#except Exception as e:
#    print(str(e))

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)

