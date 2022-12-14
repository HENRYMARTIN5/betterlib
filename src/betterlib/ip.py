"""
A collection of utilities for getting information about the current system's private and public IP address, hostname, approximate location, and more.
"""
import socket, re, uuid, requests

class ipAddress():
	def __init__(self, address=None):
		if address is None:
			url = "http://ip-api.com/json"
			response = requests.get(url)
			self.address = response.json()['query']
		else:
			self.address = address
		response = requests.get("http://ip-api.com/json/%s?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query" % self.address)

		for k, v in response.json():
			setattr(self, k, v)

if __name__ == '__main__':
    print("This module is not meant to be run directly.")
    exit(1)