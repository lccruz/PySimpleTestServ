#-*- coding:utf-8 -*-
#
# Copyright (c) 2012 by Luciano Camargo Cruz <luciano@lccruz.net>
#
# GNU General Public License (GPL)
#
import os

#Configuracao para envio de email
EMAIL_FROM = "alerta@gmail.com"
EMAIL_TO = ["to@to.com.br", "to@to.net"]
EMAIL_USERNAME = 'alerta@gmail.com'
EMAIL_PASSWORD = 'XXX'
EMAIL_SMTP = 'smtp.gmail.com:587'

#Arquivo de log
PATHPROJECT = os.path.abspath(os.path.dirname(__file__))
LOG_PATH = "%s/%s" % (PATHPROJECT,"log/log.log")

#Lista de urls para testar
URLLIST = ["http://www.python.org/", "http://plone.org/"]
