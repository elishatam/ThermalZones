#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:29:20 2018

@author: elishatam
"""
import matplotlib.dates as mtdates
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#Change these variables
filename_zone = "20180418_zone2D_0.csv"    
filename_flir = "20180420Flir-Sleep_noUSB.csv"
title = '2D:0/255'

# reading all lines into list of string
with open(filename_zone, 'r') as f:
#with open(r"20180418_zone2D_0.csv") as f:
    content = f.readlines()[1:]

content = [x.strip() for x in content]

dates = []
zone9_list = []
for line in content:
    splt = line.split(',')
    dates.append(datetime.strptime(splt[0], '%H:%M:%S').time())
    zone9_list.append(float(splt[2]))

#time = np.arange(0, len(dates))
plt.figure()
#plt.scatter(time, zone9_list, label="Zone9-lcd_therm")
plt.scatter(dates, zone9_list, label="Zone9-lcd_therm", color="y")


# reading all lines into list of string
with open(filename_flir, 'r') as f:
#with open(r"20180418_flir2D_0.csv") as f:
    content = f.readlines()[13:]

content = [x.strip() for x in content]

dates2 = []
point1 = []
point2 = []
point3 = []
point4 = []
for line in content:
    splt = line.split(',')
    dates2.append(datetime.strptime(splt[2], '%H:%M:%S').time())
    point1.append(float(splt[3])) 
    point2.append(float(splt[4])) 
    point3.append(float(splt[5])) 
    point4.append(float(splt[6])) 


dates2desired = dates2[1::200]
point1desired = point1[1::200]
point2desired = point2[1::200]
point3desired = point3[1::200]
point4desired = point4[1::200]

plt.scatter(dates2desired,point1desired,label="Spot1",color="b")
plt.scatter(dates2desired,point2desired,label="Spot2",color="r")
plt.scatter(dates2desired,point3desired,label="Spot3",color="g")
plt.scatter(dates2desired,point4desired,label="Spot4",color="k")


plt.title(title)
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
#plt.xlim(-5,30)
plt.xticks(rotation=30)
plt.ylim(0,(max(zone9_list)+10))
plt.legend(loc='lower right', frameon=True)



plt.annotate('%0.2f' % zone9_list[-1], xy=(1,zone9_list[-1]), xytext=(0, -20), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="y")
plt.annotate('%0.2f' % point1desired[-1], xy=(1,point1desired[-1]), xytext=(0, 10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="b")
plt.annotate('%0.2f' % point2desired[-1], xy=(1,point2desired[-1]), xytext=(0, 10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="r")
plt.annotate('%0.2f' % point3desired[-1], xy=(1,point3desired[-1]), xytext=(0, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="g")
plt.annotate('%0.2f' % point4desired[-1], xy=(1,point4desired[-1]), xytext=(0, -10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="k")
plt.show()