#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:
Tenha a variável LANG devidamente configurada, por ex:

	exporte LANG=pt_BR

Execução:

	python3 hello.bat
	ou
	./hello.bat
"""
__version__ = "0.0.1"
__author__ = "KrvdDvrk"
__license__ = "Unlicense"

import os

#Iniciando aqui o programa

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
	msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "es_ES":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
elif current_language == "zh_CN":
    msg = "你好世界!"

print(msg)
print(56 + 4)


