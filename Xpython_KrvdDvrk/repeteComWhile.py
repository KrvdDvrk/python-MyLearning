#!/usr/bin/env python3

# While - Enquanto

"""
n = 0
while True:   # loop infinito, main loop
    print(n)
    n += 1
"""

"""
n = 0
while n < 101:  # condição de parada
    print(n)
    n += 1
"""

"""
# condição de parada com break
n = 0
while n < 101:
    if n == 40:
        break
    print(n)
    n += 1
"""

"""
# para pular um número com o continue
n = 0
while n < 101:
    if n == 40:
        n += 1
        continue
    print(n)
    n += 1
"""

"""
# para pular um intervalo de números com o continue
n = 0
while n < 101:
    if n >= 40 and n <= 60:
        n += 1
        continue
    print(n)
    n += 1
"""

"""
# apenas os números pares com o continue
n = 0
while n < 101:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1
"""




