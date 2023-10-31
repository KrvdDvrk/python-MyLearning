#!/usr/bin/env python3

"""
 Faça um programa de terminal que exibe ao usuário listas dos quartos disponíveis para
 alugar e o preço de cada quarto, esta informação está disponível em um arquivo de
 texto separado por vírgulas.

'quartos.txt'
'''
# codigo, nome, preço

1, Suite Master, 500
2, Quarto Familia, 200
3, Quarto Single, 100
4, Quarto Simples, 50

 O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado e a
 quantidade de dias e no final exibe o valor estimado a ser pago.

 O programa deve salvar esta escolha em outro arquivo contendo as reservas

 'reservas.txt'
 '''
 # cliente, quarto, dias
 Dvrk, 3, 20
 '''
 Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma mensagem
 informando que já está reservado.
"""

import os
import sys

path = os.curdir
filepath = os.path.join(path, "quartos.txt")
templatepath = os.path.join(path, "reservas.txt")

print(
    "Códigos dos quartos:\n"
    "01 - Suíte master, no valor de R$ 500,00\n"
    "02 - Quarto Família, no valor de R$ 200,00\n"
    "03 - Quarto Single, no valor de R$100,00\n"
    "04 - Quarto Simples, no valor de R$ 50,00\n"
)

name = input("Digite seu nome: ")
days = int(input("Digite a quantidade dias que pretende ficar: "))
cod = input("Digite o código do tipo de quarto reservado: ")

quarto = []

for line in open(filepath):
    cod, type_, value = line.split(",")
    quarto[int(cod)] = {
        "type_": type_,
        "value": float(value),
    }

#cod = input("Digite o código do tipo de quarto reservado: ")

print(f"O quarto escolhido foi o {type_} no valor de {value}")

#FALHEI, NÃO CONSEGUI RESOLVER.







