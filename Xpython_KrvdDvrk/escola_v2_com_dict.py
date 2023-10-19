#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade
Imprimir a lista de crianças agrupadas por sala que frequentam cada umas das atividades
"""

from pprint import pprint

__version__ = "0.1.0"
__author__ = "KrvdDvrk"

sala = {
    "T01": ["Erika", "Maria", "Gabriel", "Manuela", "Sofia", "João"],
    "T02": ["Joana", "Antonio", "Carlos", "Mario", "Isolda"],
}

salae = {
    "T03I": ["Erika", "Maria", "Joana", "Carlos", "Antonio"],
    "T04M": ["Erika", "Carlos", "Maria"],
    "T05D": ["Gabriel", "Sofia", "João", "Antonio"],
}

print("Relação de Alunos das turmas complementares e suas respectivas turmas de origem")
print()
print(f"A turma de Inglês é composta pelos alunos: ")
print(salae["T03I"])
print("Os alunos da T01 presentes nessa turma são: ")
print(set(sala["T01"]) & set(salae["T03I"]))
print("Os alunos da T02 presentes nessa turma são: ")
print(set(sala["T02"]) & set(salae["T03I"]))
print()
print(f"A turma de Música é composta pelos alunos: ")
print(salae["T04M"])
print("Os alunos da T01 presentes nessa turma são: ")
print(set(sala["T01"]) & set(salae["T04M"]))
print("Os alunos da T02 presentes nessa turma são: ")
print(set(sala["T02"]) & set(salae["T04M"]))
print()
print(f"A turma de Dança é composta pelos alunos: ")
print(salae["T05D"])
print("Os alunos da T01 presentes nessa turma são: ")
print(set(sala["T01"]) & set(salae["T05D"]))
print("Os alunos da T02 presentes nessa turma são: ")
print(set(sala["T02"]) & set(salae["T05D"]))



