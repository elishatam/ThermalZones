#!/bin/bash
#This script reads the internal temperature sensors in the Hydrogen Phone.
#Make sure to "adb root" your phone.
#In Windows PowerShell, run by typing: "./readtempWindows.sh testname". 'testname' will be an element in the output csv.
#"tail -5 outputDataWindows.csv" to read last 5 lines
#For EVT2.0A & 2.0B, read thermal_zone11 for internal LCD hotspot
#For EVT2.1A & 2.1B, read thermal_zone9 for internal LCD hotspot

while true
do

outputfile=outputDataWindows.csv

#Print Date
currentdate=$(date +"%Y%m%d")  
echo $currentdate >> $outputfile 
echo $'\r' >> $outputfile    #create newline in Windows

#Print Time
now=$(date +"%T")  #%T = %H:%M:%S
echo $now >> $outputfile 
echo $'\r' >> $outputfile   #create newline in Windows

#Print Description of test
arg1="$1"
echo $1 >> $outputfile 
echo $'\r' >> $outputfile    #create newline in Windows

#Print temps of different zones
adb shell "cat /sys/class/thermal/thermal_zone0/temp;
			cat /sys/class/thermal/thermal_zone5/temp; 
			cat /sys/class/thermal/thermal_zone7/temp; 
			cat /sys/class/thermal/thermal_zone8/temp; 
			cat /sys/class/thermal/thermal_zone9/temp; 
			cat /sys/class/thermal/thermal_zone11/temp;
                        cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq;                   #GPU frequency
                        cat /sys/class/leds/lcd-backlight/brightness;                    #2D Backlight brightness
                        cat /sys/class/leds/LM36923H-BL/brightness;" >> $outputfile      #3D Backlight brightness

echo $'\r' >> $outputfile   #create newline in Windows


#This only works on Mac or Linux. It has issues with the newline in windows.
#Thomas says he can just use the outputData.csv for the Python script
#Modify data from multilines into csv
#https://stackoverflow.com/questions/8714355/bash-turning-multi-line-string-into-single-comma-separated
#cat outputData.csv | xargs -n 12 | sed -e 's/ /,/g' > outputFinal.csv

#Repeat every minute
sleep 60
done
