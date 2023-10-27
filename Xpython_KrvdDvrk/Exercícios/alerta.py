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

while True:

    print("------------------------")
    print("ALERTA DE TEMPERATURA")
    print("------------------------")
    try:
        temp = float(input("Qual é a temperatura atual do seu local?\n").strip())
    except ValueError:
        log.error("Temperatura inválida")
        sys.exit(1)

    try:
        umi = float(input("Qual a umidade atual do seu local?\n").strip())
    except ValueError:
        log.error("Umidade inválida")
        sys.exit(1)

    print()

    if temp > 45:
        print("ALERTA!!! Perigo calor extremo\n")
    elif temp >= 31 and temp <= 45:
        print("ALERTA!!! Calor forte\n")
    elif temp >= 10 and temp <= 30:
        print("Temperatura normal\n")
    elif temp >= 0 and temp < 10:
        print("Temperatura fria\n")
    elif temp < 0:
        print("ALERTA!!! Frio extremo\n")

    if umi > temp * 3 and umi > 30:
        print("ALERTA!!! Perigo de calor úmido\n")

    if input(
    "Se deseja realizar outra consulta aperte enter, caso queira sair aperte qualquer outra tecla e em seguida o enter\n"
    ):
        break
