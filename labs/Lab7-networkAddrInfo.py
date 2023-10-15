#Script that calculates IP addresses from a given CIDR notation

from netaddr import *


ipset = IPSet(['192.168.4.0/28'])

for ip in ipset:
    print(ip)
