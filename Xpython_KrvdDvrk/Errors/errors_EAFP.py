#!/usr/bin/env python3

import os
import sys
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão

def try_to_open_a_file(filepath, retry =1) -> list:
    """Tries to open a file, if error, retries n times"""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(2)
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)

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

