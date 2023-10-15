#Using netaddr for MAC address information

from netaddr import *
import socket               #Module to pull hostname automatically from computer
from uuid import getnode    #Module to pull MAC address automatically from computer
mac = getnode()    
hostname = socket.gethostname()
macAddr = EUI(mac)          #Formats getnode() into the standard IEEE EUI-48 format
oui = macAddr.oui
ouiOrg = oui.registration().org           
ouiOrgAddress = oui.registration().address
print(f"Here is some MAC address information for {hostname}: \n")
print(f"EUI-48 format: {macAddr} \nHex format: {hex(macAddr)}\n")
print(f"The organization identifier is: {oui} \nThis OUI belongs to {ouiOrg} located at {ouiOrgAddress}")














