# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 by Luciano Camargo Cruz <luciano@lccruz.net>
#
# GNU General Public License (GPL)
#
import smtplib
from datetime import datetime
from urllib2 import Request, urlopen, URLError
from settings import *

def writeLog(msg, notError=True):
    """Escreve no arquivo de log"""
    log = open(LOG_PATH,'a')
    if notError:
        msg = ("%s - %s\n") % (datetime.now().strftime("%d/%m/%Y %H:%M"), msg)
    else:
        msg = ("%s - ERRO - %s\n") % (datetime.now().strftime("%d/%m/%Y %H:%M"), msg)
    log.write(msg)
    log.close()

def sendMail(parTitulo, parMenssagem):
    """Envia email """
    menssagem = """From: %s
Mime-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Subject: %s

%s""" % (EMAIL_FROM, parTitulo, parMenssagem)

    server = smtplib.SMTP(EMAIL_SMTP)
    try:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, menssagem)
        server.quit()
        writeLog("Email enviado com sucesso")
    except Exception as (errno, strerror):
        writeLog(strerror, False)
        server.quit()

def testServ():
    """Teste conexao com servidor para cada entrada da lista global URLLIST"""
    for url in URLLIST: 
        try:
            req = Request(url)
            urlopen(req)
        except URLError, e:
            errorTitle = "%s SERVIDOR = %s" % (e.reason[1], url)
            writeLog(errorTitle, False)
            titulo = "ERRO - %s" % (url)
            msg = "ERRO = %s\n SERVIDOR = %s" % (e.reason[1], url)
            sendMail(titulo, msg)

testServ()
