function getIP{ 

    (get-netipaddress).ipv4address  | select-string "192.168.4"

} 

function getUser{

    $env:USERNAME

}

function hostName{

    $env:COMPUTERNAME
}

function psInfo{
    
    (get-host | select-object).Version.Major

}

function getDate{

    Get-Date -Format "dddd, MMMM dd,yyyy"

}

$IP = getIP
$HostName = hostName
$VERSION = psInfo
$USER = getUser
$DATE = getDate



$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HostName. PowerShell Version $VERSION. Today's Date is $DATE."
Write-Host ($BODY)
Write-Output ($BODY) | Out-File -FilePath .\OutFile.txt -Append



