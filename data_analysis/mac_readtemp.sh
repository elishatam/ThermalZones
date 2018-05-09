#!/bin/bash
#This script reads the internal temperature sensors in the Hydrogen Phone.
#Make sure to "adb root" your phone.
#In terminal, run by typing: "./mac_readtemp.sh testname". 'testname' will be an element in the output csv.
#"tail -5 file.csv" to read last 5 lines
#For EVT2.0A & 2.0B, read thermal_zone11 for internal LCD hotspot
#For EVT2.1A & 2.1B, read thermal_zone9 for internal LCD hotspot
while true
do

outputfile=outputData.csv
outputFinalFile=outputFinal.csv

#Print Date
currentdate=$(date +"%Y%m%d") 
echo $currentdate >> $outputfile 

#Print Time
now=$(date +"%T")  #%T = %H:%M:%S
echo $now >> $outputfile 

#Print Description
arg1="$1"
echo $1 >> $outputfile 

#Print temps of different zones
adb shell "cat /sys/class/thermal/thermal_zone0/temp;
			cat /sys/class/thermal/thermal_zone5/temp; 
			cat /sys/class/thermal/thermal_zone7/temp; 
			cat /sys/class/thermal/thermal_zone8/temp; 
			cat /sys/class/thermal/thermal_zone9/temp; 
			cat /sys/class/thermal/thermal_zone11/temp;
            cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq;                   #GPU frequency
            cat /sys/class/leds/lcd-backlight/brightness;                    #2D Backlight Brightness 
            cat /sys/class/leds/LM36923H-BL/brightness;" >> $outputfile      #3D Backlight Brightness



#Modify data from multilines into csv
#https://stackoverflow.com/questions/8714355/bash-turning-multi-line-string-into-single-comma-separated
cat $outputfile | xargs -n 12 | sed -e 's/ /,/g' > $outputFinalFile


#Repeat every minute
sleep 60
done
