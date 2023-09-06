#!/bin/bash

#This script outputs the IP address and Hostname of a machine
#echo 'This is a script. Hello!'
greeting="This is a script. Hello!"
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME
a=$(ip a | grep 'noprefixroute ens33' | awk '{print $2}')
echo My IP is $a
