#!/usr/bin/env python3

import os
import logging

#SEM O LOG_LEVEL:
"""
#nossa instancia
log = logging.Logger("Dvrk", logging.DEBUG)

#level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#formatação
#Pode achar os atributos de logging aqui: https://docs.python.org/3/library/logging.html
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

#destino
log.addHandler(ch)
"""

#COM O LOG_lEVEL:
"""
#Transforma uma configuração de logging, para uma que é controlada pelo usuário.
#Digitando no terminal por exemplo "export LOG_LEVEL=error", o usuário deixa de ver o WARNING e só vê o ERROR e CRITICAL

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

#nossa instancia
log = logging.Logger("Dvrk", log_level)

#level
ch = logging.StreamHandler()
ch.setLevel(log_level)

#formatação
#Pode achar os atributos de logging aqui: https://docs.python.org/3/library/logging.html
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

#destino
log.addHandler(ch)
"""


#Modo cru sem a definição de um log
"""
logging.debug("Message for the dev, qe, sysadmin")
logging.info("General message for the users")
logging.warning("Warn that not does error")
logging.error("Error who affects one only execution")
logging.critical("General Error, Ex: Database not found")
"""

#A Configuração abaixo é apenas para configurar o log
#É uma configuração repetitiva e por isso é chamada de BOILERPLATE
#TODO: Usar função
#TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Dvrk", log_level)
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Como fizemos o log lá em cima na "nossa instancia", não será mais necessário usar "logging.debug", poderemos usar só "log.debug"

log.debug("Message for the dev, qe, sysadmin")
log.info("General message for the users")
log.warning("Warn that not does error")
log.error("Error who affects one only execution")
log.critical("General Error, Ex: Database not found")

print("-----")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("%s", str(e))
