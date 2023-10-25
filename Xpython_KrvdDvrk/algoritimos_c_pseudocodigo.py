#!/usr/bin/env python3

# Algoritimos
"""
Trasnformando um caso real, em um programa python de maneira genérica, a fim de aprendizado.

> Sequência de instruções lógicas que visam obter a solução de um problema.

Problema: Ir a padaria comprar pão:
Premissa: Padaria da Esquina abre no fds até 12hrs, semana até 19h, feriado (exceto natal) não abre.

1. A padaria está aberta?
    1. Se é feriado e NÃO é natal: não
    2. Senão, Se é sábado OU domingo E antes do meio dia: sim
    3. Senão, se é dia de semana E antes das 19h: sim
    4. senão: não
2. Se a padaria está aberta E:
    1. Se está chovendo: Pegar guarda-chuvas
    2. Se está chovendo E calor: Pegar guarda-chuvas e garrafa de água
    3. Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
3. Senão
    1. Ficar em casa e comer bolachas
"""
# PSEUDOCODIGO *Nçao existem no python do jeito que está, é apenas para aprendizado
import ir, pegar, pedir, tem, comer, ficar

# Premissas
todas = "Segunda"
hora = 15
natal = False
chovendo = True
frio: True
semana = ["Segunda", "Terça", "Quarte", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana" = 19,
    "fds": 12
}

# Algoritimo
# 1.1
if today in feriados and not natal:
    padaria_aberta = False
#1.2
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
#1.3
elif today not in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
#1.4
else:
    padaria_aberta = False

"""
# Outro modo para o 1.2 e 1.3
elif (today not in semana and hora < horario_padaria["fds"]) or (today not in semana and hora < horario_padaria["semana"]):
    padaria_aberta = True
"""

#2.1 / 2.2 / 2.3
if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuvas")
        pegar("agua")
    elif chovendo:
        pegar("guarda-chuva")
#2.4
    ir("padaria")
    if tem("pao int") and tem("baguete")
        pedir(6, "pao int")
        pedir(6, "baguete")
    elif tem("pao int") or tem("baguete")
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer pao")
#3
    ficar("casa")
    comer("bolacha")
