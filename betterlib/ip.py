"""
A collection of utilities for getting information about the current system's private and public IP address, hostname, MAC address, approximate location, and more.
"""
import socket
import re
import uuid
import requests

def getIp():
	"""
	Returns the current system's private IP address.
	"""

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("gmail.com",80))
		ip = s.getsockname()[0]
		s.close()
		return ip
	except:
		return None

def getPubIp():
	"""
	Returns the current system's public IP address.
	"""
	
	try:
		url = "http://ip-api.com/json"
		response = requests.get(url)
		return response.json()['query']
	except:
		return None

def getHostname():
	"""
	Returns the current system's hostname.
	"""

	try:
		return socket.gethostname()
	except:
		return None

def getMac():
	"""
	Returns the current system's MAC address.
	"""

	try:
		return ':'.join(re.findall('..', '%012x' % uuid.getnode()))
	except:
		return None

def getMacVendor(mac):
	"""
	Returns the vendor of the given MAC address.
	"""

	try:
		url = "https://api.macvendors.com/%s" % mac
		response = requests.get(url)
		return response.status
	except:
		return None

def approximateLocation(ip):
	"""
	Returns the approximate location of the given IP address.
	"""

	try:
		url = "http://ip-api.com/json/%s" % ip
		response = requests.get(url)
		return response.json()
	except:
		return None

def isBehindProxy():
	"""
	Returns whether or not the current system is behind a proxy.
	"""

	try:
		url = "http://ip-api.com/json"
		response = requests.get(url)
		return response.json()['proxy']
	except:
		return None

def isTor(ip):
	"""
	Returns whether or not the given IP address is a Tor exit node.
	"""

	try:
		url = "http://ip-api.com/json/%s" % ip
		response = requests.get(url)
		return response.json()['tor']
	except:
		return None

def isVpn(ip):
	"""
	Returns whether or not the given IP address is a VPN exit node.
	"""

	try:
		url = "http://ip-api.com/json/%s" % ip
		response = requests.get(url)
		return response.json()['vpn']
	except:
		return None

def getLatLong(ip=None):
	"""
	Returns the latitude and longitude of the given IP address.
	"""

	if ip is None:
		ip = getPubIp()
	try:
		url = "http://ip-api.com/json/%s" % ip
		response = requests.get(url)
		return response.json()['lat'], response.json()['lon']
	except:
		return None

if __name__ == '__main__':
    print("This module is not meant to be run directly.")
    exit(1)