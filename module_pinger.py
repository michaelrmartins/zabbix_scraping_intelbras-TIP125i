# Michael Martins - 2024
# Check Host is online/Offline using ping

# Receive Target Ip Address as argument and return "down" or "up"

# Libraries
import os 

# Function
def ping(hostIpAddress):
    response = os.popen(f"ping -c 3 {hostIpAddress}").read()
    if "Request timed out." in response or "Unreachable" in response:
        return ("down")
    else:
        return ("up")