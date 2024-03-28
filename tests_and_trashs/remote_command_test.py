# Python program to demonstrate and Zabbix Remote Commands test
# command line arguments
 
# Libraries
import sys
import module_checkHostStatus

ip_address = sys.argv[1]

status = module_checkHostStatus.checkstatus(ip_address)