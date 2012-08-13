PySimpleTestServ:
    Script para testar conexões com servidores através da url.
    Envia e-mail se o respectivo servidor estiver down.
    Grava um log de execução.
    Copyright (c) 2012
    GNU General Public License (GPL)

Credits
    * Luciano Camargo Cruz <luciano@lccruz.net>

Requirements:
    Python == 2.7 or 2.6

Servidor local:
    + Configurar valores no arquivo settins.py
        #Configuracao para envio de email
        EMAIL_FROM = "alerta@gmail.com"
        EMAIL_TO = ["to@to.com.br", "to@to.net"]
        EMAIL_USERNAME = 'alerta@gmail.com'
        EMAIL_PASSWORD = 'XXX'
        EMAIL_SMTP = 'smtp.gmail.com:587'

        #Arquivo de log
        LOG_PATH = "log/log.log"

        #Lista de urls para testar
        URLLIST = ["http://www.python.org/", "http://plone.org/"]

    + adicionar regra no Crontab:
        crontab -e (executa todos os dias meio-dia e a meia-noite)
        00 00,12 * * * python CAMINHO/pysimpletestserv.py
