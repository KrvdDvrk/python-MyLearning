#!/usr/bin/env python3

"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o índice de umidade
do ar, sendo que caso será exibida uma mensagem de alerta dependendo das condições:

        temperatura maior que 45: ALERTA!!! Perigo calor extremo
temperatura vezes 3 for mais ou igual a umidade: ALERTA!!! Perigo de calor úmido
temperatura entre 10 e 30: Normal
temperatura entre 0 e 10: Frio
temperatura abaixo de 0: Frio extremo
"""

import sys
import logging
log = logging.Logger("alerta")

info = {"temperatura": None, "umidade": None}

while True:
    # condiçao de parada
    # o dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break

    if all(info.values()):
        break

    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = float(input(f"Qual a {key}").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break

    temp, umidade = info.values()

    if temp > 45:
        print("ALERTA!!! Perigo calor extremo")
    elif temp >30 and temp * 3 >= umidade:
        print("ALERTA!!! Perigo de calor úmido")
    elif temp >= 10 and temp <= 30:
        print("Normal")
    elif temp >= 0 and temp <= 10:
        print("Frio")
    elif temp < 0:
        print("ALERTA!!! Frio extremo")



