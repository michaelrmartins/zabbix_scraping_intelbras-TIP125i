import requests
import subprocess

# Configurações de autenticação e URL da API do Zabbix
ZBX_URL = 'http://localhost/zabbix/api_jsonrpc.php'
ZBX_USERNAME = 'gti'
ZBX_PASSWORD = '6feira*13'

# Variables
zabbix_group_id = 56

# Função para autenticar na API do Zabbix e obter o token de autenticação
def authenticate_zabbix_api():
    try:
        response = requests.post(ZBX_URL, json={
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": ZBX_USERNAME,
                "password": ZBX_PASSWORD
            },
            "id": 1
        })
        return response.json()['result']
    except Exception as e:
        print("Erro durante a autenticação:", e)
        return None

# Função para obter os IDs de todos os hosts em um grupo
def get_host_ids_in_group(group_id, auth_token):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid"],
                "selectGroups": "extend",
                "groupids": [group_id]  # Usando o ID do grupo fornecido
            },
            "auth": auth_token,
            "id": 1
        }
        response = requests.post(ZBX_URL, json=payload)
        return [host['hostid'] for host in response.json()['result']]
    except Exception as e:
        print("Erro ao obter IDs dos hosts no grupo:", e)
        return None

# Função para obter os detalhes das interfaces de host
def get_host_interfaces(auth_token, host_id):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "hostinterface.get",
            "params": {
                "output": "extend",
                "hostids": host_id  # ID do host que você quer obter os detalhes das interfaces
            },
            "auth": auth_token,  # Incluindo o token de autenticação
            "id": 1
        }
        response = requests.post(ZBX_URL, json=payload)
        return response.json()
    except Exception as e:
        print("Erro ao obter detalhes das interfaces de host:", e)
        return None

# Função para extrair apenas os IPs das interfaces de host da resposta da API do Zabbix
def extract_ips(response):
    if 'result' in response:
        return [interface['ip'] for interface in response['result']]
    else:
        print("Erro: Não foi possível extrair IPs. Resposta da API não contém o campo 'result'.")
        return []

# Autenticar na API do Zabbix
auth_token = authenticate_zabbix_api()
if auth_token:
    # Chamar a função para obter os IDs dos hosts no grupo
    hosts_list = get_host_ids_in_group(zabbix_group_id, auth_token)  #
    ip_interface_list_json = get_host_interfaces(auth_token, hosts_list)  # 
    ip_interface_list = extract_ips(ip_interface_list_json)
    if hosts_list:
        # print("IDs dos hosts no grupo:", hosts_list) # Debug
        # print("Ips dos hosts no grupo:", ip_interface_list) # Debug
        for ip in ip_interface_list:
            subprocess.run(['python3', '/home/gti/zabbix_scraping/scraping_intelbras_tip125i-Selenium.py', ip])
            print(ip)
    else:
        print("Falha ao obter IDs dos hosts no grupo.")
else:
    print("Falha na autenticação. Não foi possível obter o token de autenticação.")
