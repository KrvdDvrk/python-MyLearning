#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade
Imprimir a lista de crianças agrupadas por sala que frequentam cada umas das atividades
"""
__version__ = "0.1.0"
__author__ = "KrvdDvrk"

sala1 = ["Erika", "Maria", "Gabriel", "Manuela", "Sofia", "João"]
sala2 = ["Joana", "Antonio", "Carlos", "Mario", "Isolda"]

aula_ingles = ["Erika", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erika", "Carlos", "Maria"]
aula_danca = ["Gabriel", "Sofia", "João", "Antonio"]

atividades = [
        ("Inglês", aula_ingles),
        ("Música", aula_musica),
        ("Dança", aula_danca)
]

# Listar alunos em cada atividade por sala

print("Alunos das aulas complementares e suas salas de origem")
print()

for nome_atividade, atividade in atividades:

    # Sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"Alunos de {nome_atividade} da sala 1: ", atividade_sala1)
    print(f"Alunos de {nome_atividade} da sala 2: ", atividade_sala2)
    print("-" * 30)



