#!/usr/bin/env python3

""" Exemplos de envio de e-mail

Usar o comando no terminal para criar um servidor de teste:

python -m smtpd -c DebuggingServer -n localhost:8025

"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "dvrk@krvd.com"
TO = ["destino1@server.com, destino2@server.com"]
SUBJECT = "Meu e-mail via python"
TEXT = """\
Este é o meu e-mail enviado pelo python
<b>Olá mundo<\b>"""

message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
