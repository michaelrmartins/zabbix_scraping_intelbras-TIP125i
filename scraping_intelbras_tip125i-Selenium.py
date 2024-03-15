from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Configure ChromeOptions
chrome_options = Options() # Initialize object
chrome_options.add_argument('--headless')  # Run Headless Mode
chrome_options.add_argument('--no-sandbox')  # Important to run in No GUI Evironment 
chrome_options.add_argument('--disable-dev-shm-usage')  # Important to run in No GUI Evironment 
chrome_options.add_argument('--ignore-certificate-errors')  # No check SSL Certified Error

# Inicialize ChromeDriver Service
service = Service()

# Inicialize o driver do Chrome com as opções configuradas
driver = webdriver.Chrome(service=service, options=chrome_options)

# Website URL
url_status = 'https://admin:admin@192.168.5.75/_index.html#/status'
url_account = 'https://admin:admin@192.168.5.75/_index.html#/account/1'
print("Acessando a URL:", url_status)

# Get website Data
driver.get(url_status)

print("Aguardando a página carregar...")

# Wating body element
wait = WebDriverWait(driver, 100)
wait.until(EC.visibility_of_element_located((By.ID, "label_operation_time")))
time.sleep(5)  # Wait Full Page Load
print("Page Loaded!")

# WAN element find and Click to change page --------- PAGE STATUS / "SISTEMA"
elementWanClickPage1 = driver.find_element(By.ID, '1')
elementWanClickPage1.click()
time.sleep(1)  # Wait

# Get webpage data
out_system_uptime = driver.find_elements(By.ID, 'operation_time')[0].text
out_system_version = driver.find_elements(By.ID, 'app_version')[0].text
out_system_revision = driver.find_elements(By.ID, 'revision')[0].text
out_user_account_status = driver.find_elements(By.ID, 'user')[0].text

# WAN element find and Click to change page --------- PAGE STATUS / "WAN"
elementWanClickPage2 = driver.find_element(By.ID, '2')
elementWanClickPage2.click()
time.sleep(1)  # Wait

# Get webpage Data
out_wan_ip_address = driver.find_elements(By.ID, 'wan_ip_address')[0].text
out_wan_mac_address = driver.find_elements(By.ID, 'wan_mac_address')[0].text
out_wan_host_name = driver.find_elements(By.ID, 'wan_hostname')[0].text


# WAN element find and Click to change page --------- PAGE "CONTA" / "BASICO"
print("Loading ", url_account)
# Get website Data
driver.get(url_account)
time.sleep(5)  # Wait
elementAccountClickPage1 = driver.find_element(By.ID, '1')
elementAccountClickPage1.click()
time.sleep(1)  # Wait

# Get webpage Data
out_account_caller_id_name = driver.find_element(By.ID, 'line_caller_id')
out_account_caller_id_name_value = out_account_caller_id_name.get_attribute('value')

out_account_caller_register_name = driver.find_element(By.ID, 'line_caller_name')
out_account_caller_register_name_value = out_account_caller_register_name.get_attribute('value')

out_account_caller_user_name = driver.find_element(By.ID, 'line_auth_user')
out_account_caller_user_name_value = out_account_caller_user_name.get_attribute('value')

out_account_sip_server_ip = driver.find_element(By.ID, 'sip_server')
out_account_sip_server_ip_value = out_account_sip_server_ip.get_attribute('value')

out_account_sip_server_port = driver.find_element(By.ID, 'sip_server_port')
out_account_sip_server_port_value = out_account_sip_server_port.get_attribute('value')

out_account_sip_proxy_server_ip = driver.find_element(By.ID, 'outbound_proxy_ip')
out_account_sip_proxy_server_ip_value = out_account_sip_proxy_server_ip.get_attribute('value')

out_account_sip_proxy_server_port = driver.find_element(By.ID, 'outbound_proxy_port')
out_account_sip_proxy_server_port_value = out_account_sip_proxy_server_port.get_attribute('value')

out_account_sip_server_secondary_ip = driver.find_element(By.ID, 'sip_server2')
out_account_sip_server_secondary_ip_value = out_account_sip_server_secondary_ip.get_attribute('value')

out_account_sip_server_secondary_port = driver.find_element(By.ID, 'sip_server_port2')
out_account_sip_server_secondary_port_value = out_account_sip_server_secondary_port.get_attribute('value')

# Print website data
print ("Uptime:", out_system_uptime)
print ("Version:", out_system_version)
print ("Revision:", out_system_revision)
print ("IP:", out_wan_ip_address)
print ("Mac:", out_wan_mac_address)
print ("Hostname:", out_wan_host_name)
print ("Account Status:", out_user_account_status)
print ("ID Name:", out_account_caller_id_name_value)
print ("Register Name:", out_account_caller_register_name_value)
print ("User Name:", out_account_caller_user_name_value)
print ("SIP Server IP:", out_account_sip_server_ip_value)
print ("SIP Server Port:", out_account_sip_server_port_value)
print ("SIP Proxy Server IP:", out_account_sip_proxy_server_ip_value)
print ("SIP Proxy Server Port:", out_account_sip_proxy_server_port_value)
print ("SIP Server Secondary IP:", out_account_sip_server_secondary_ip_value)
print ("SIP Server Secondary Port:", out_account_sip_server_secondary_port_value)

