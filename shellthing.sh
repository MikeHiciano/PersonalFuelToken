#!/bin/bash
### BEGIN INIT INFO
# Provides:          blabla
# Required-Start:    $syslog
# Required-Stop:     $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: it run my cool stuffs!
# Description:
#
### END INIT INFO

while true
do
   python3 press.py
   kill $!
   sleep 5
   python3 gas.py
   kill $!
   sleep 5
done