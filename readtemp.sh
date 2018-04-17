#!/bin/bash

while true
do

arg1="$1"

adb shell "cat /sys/class/thermal/thermal_zone0/temp;
			cat /sys/class/thermal/thermal_zone5/temp; 
			cat /sys/class/thermal/thermal_zone7/temp; 
			cat /sys/class/thermal/thermal_zone8/temp; 
			cat /sys/class/thermal/thermal_zone9/temp; 
			cat /sys/class/thermal/thermal_zone11/temp" >> outputData.txt

echo $1 >> outputData.txt
now=$(date +"%T")  #%T = %H:%M:%S
echo $now >> outputData.txt

#https://stackoverflow.com/questions/8714355/bash-turning-multi-line-string-into-single-comma-separated
#cat outputData.txt | xargs -n 5 | sed -e 's/ /, /g' > output.txt
cat outputData.txt | xargs -n 8 | sed -e 's/ /,/g' > outputFinal.txt

sleep 120
done