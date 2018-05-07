#!/bin/bash
# "tail -5 outputFinal.txt" Read last 5 lines
#For EVT2, read thermal_zone11
#For EVT2.1, read thermal_zone9
while true
do

#Print Date
#currentdate=$(date +"%Y%m%d")
currentdate=$(date +"%Y%m%d")  #%T = %H:%M:%S
echo $currentdate >> outputData.csv

#Print Time
now=$(date +"%T")  #%T = %H:%M:%S
#now=$(date +"%Y%m%d-%T")  #%T = %H:%M:%S
echo $now >> outputData.csv

#Print Description
arg1="$1"
echo $1 >> outputData.csv

#Print temps of different zones
adb shell "cat /sys/class/thermal/thermal_zone0/temp;
			cat /sys/class/thermal/thermal_zone5/temp; 
			cat /sys/class/thermal/thermal_zone7/temp; 
			cat /sys/class/thermal/thermal_zone8/temp; 
			cat /sys/class/thermal/thermal_zone9/temp; 
			cat /sys/class/thermal/thermal_zone11/temp;
            cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq;
            cat /sys/class/leds/lcd-backlight/brightness;
            cat /sys/class/leds/LM36923H-BL/brightness;" >> outputData.csv



#Modify data from multilines into csv
#https://stackoverflow.com/questions/8714355/bash-turning-multi-line-string-into-single-comma-separated
cat outputData.csv | xargs -n 12 | sed -e 's/ /,/g' > outputFinal.csv

#Repeat every minute
sleep 60
done
