#-*- encoding: utf-8 -*-
# Interfaceador Zabbix >> Grafana
# Michael Martins - 2022
# -
# -------------------------------------------------------------------------------
# Este Software tem a finalidade de obter os dados do banco de dados do Zabbix  -
# e exportar em um arquivo no formato JSON.                                      -
# -------------------------------------------------------------------------------
# -

# Bibliotecas
from pickle import FALSE
from socket import timeout
from zabbix_api import ZabbixAPI
import os
import json
import re

# Autenticação
ZBX_URL = 'http://localhost/zabbix'
ZBX_USERNAME = 'gti'
ZBX_PASSWORD = '6feira*13'

# Conexão com a API
try:
    zapi = ZabbixAPI(ZBX_URL, timeout=180)
    zapi.login(ZBX_USERNAME, ZBX_PASSWORD)
    print(f'Conectado a API do Zabbix, {zapi.api_version()}')
except Exception as erro:
    print(f'Erro na Conexão {erro}')
    exit()

    