import subprocess
import requests
import time

def updateURL():
	domain = "domainname"  # Replace with your own domain
	token = "token" # Replace with your token
	ip6addr = getIPV6() 
	ip6lanprefix = getIPV6Prefix()
	url = f"http://dynv6.com/api/update?hostname={domain}&token={token}&ipv6={ip6addr}&ipv6prefix={ip6lanprefix}"
	response = requests.get(url)
	print(response.text)

def getIPV6Prefix():
	output = subprocess.check_output(["ip", "-6", "addr", "show", "eth0"])
	ipv6 = output.split()[25].decode()
	prefix = ":".join(ipv6.split(":")[:4]) + "::"
	return prefix

def getIPV6():
	output = subprocess.check_output(["ip", "-6", "addr", "show", "eth0"])
	ipv6 = output.split()[25].decode()
	ipv6 = ipv6.split("/")[0]
	return ipv6

updateURL()
