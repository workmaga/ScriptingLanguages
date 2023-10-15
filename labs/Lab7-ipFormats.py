from netaddr import *
import pprint
import socket

#automatic search and retrieval for hostname and IP address of host using socket module

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)

ip = IPAddress(ip_address)


#Use case 1: Using netaddr to represent an IP address in different formats

print(f"Here is the IP address for {hostname} in: ")

print(f"IPv4 Notation: {ip}")
print(f"Hex format: {hex(ip)}")
print(f"Binary format: {ip.bin}")
print(f"IPv4 Binary Notation: {ip.bits()}")