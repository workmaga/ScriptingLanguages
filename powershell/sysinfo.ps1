function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 

write-host(getIP)

$IP = getIP

write-host("This machine's IP is $IP")
write-host("This machine's IP is {0}" -f $IP)
