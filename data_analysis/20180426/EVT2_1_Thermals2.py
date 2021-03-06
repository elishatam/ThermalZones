#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:29:20 2018

@author: elishatam
"""
#import matplotlib.dates as mtdates
import matplotlib.pyplot as plt
#import numpy as np
from datetime import datetime

#Change these variables
filename_zone = "05_DungeonHighGPU.csv"    
filename_flir = "20180426 - 05_DungeonHighGPU.csv"
title = 'Dungeon Masters, 4x1, ACT On, DOF On, High GPU'

plt.figure()

# reading all lines into list of string
with open(filename_zone, 'r') as f:
#with open(r"20180418_zone2D_0.csv") as f:
    content = f.readlines()[1:]

content = [x.strip() for x in content]

dates = []
zone9_list = []
for line in content:
    splt = line.split(',')
    dates.append(datetime.strptime(splt[1], '%H:%M:%S').time())
    zone9_list.append(float(splt[7]))

#time = np.arange(0, len(dates))

#plt.scatter(time, zone9_list, label="Zone9-lcd_therm")
plt.scatter(dates, zone9_list, label="Zone9-lcd_therm", color="y")
plt.annotate('%0.2f' % zone9_list[-1], xy=(1,zone9_list[-1]), xytext=(0, 5), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="y")


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
point5 = []
point6 = []
point7 = []
point8 = []
point9 = []
point10 = []
for line in content:
    splt = line.split(',')
    #dates2.append(datetime.strptime(splt[2], '%H:%M:%S').time()) 
    dates2.append(datetime.strptime(splt[1], '%I:%M:%S %p').time())
    point1.append(float(splt[4])) 
    point2.append(float(splt[5])) 
    point3.append(float(splt[6])) 
    point4.append(float(splt[7])) 
    point5.append(float(splt[8])) 
    point6.append(float(splt[9])) 
    point7.append(float(splt[10]))
    point8.append(float(splt[11]))
    point9.append(float(splt[12]))
    point10.append(float(splt[13]))

#Pick every 200 points
dates2desired = dates2[1::200]
point1desired = point1[1::200]
point2desired = point2[1::200]
point3desired = point3[1::200]
point4desired = point4[1::200]
point5desired = point5[1::200]
point6desired = point6[1::200]
point7desired = point7[1::200]
point8desired = point8[1::200]
point9desired = point9[1::200]
point10desired = point10[1::200]

#print(dates2desired)

plt.scatter(dates2desired,point1desired,label="Spot1",color="b")
plt.scatter(dates2desired,point2desired,label="Spot2",color="r")
plt.scatter(dates2desired,point3desired,label="Spot3",color="g")
plt.scatter(dates2desired,point4desired,label="Spot4",color="k")
plt.scatter(dates2desired,point5desired,label="Spot5",color="c")
plt.scatter(dates2desired,point6desired,label="Spot6",color="m")
plt.scatter(dates2desired,point7desired,label="Spot7",color="b",marker="*")
plt.scatter(dates2desired,point8desired,label="Spot8",color="r",marker="*")
plt.scatter(dates2desired,point9desired,label="Spot8",color="g",marker="*")
plt.scatter(dates2desired,point10desired,label="Spot8",color="k",marker="*")

plt.title(title)
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
#plt.xlim(-5,30)
plt.xticks(rotation=30)
#plt.ylim(0,(max(zone9_list)+10))
plt.ylim(0,(max(point1)+10))
print(max(point1))
plt.legend(loc='lower right', frameon=True)



plt.annotate('%0.2f' % point1desired[-1], xy=(1,point1desired[-1]), xytext=(0, 5), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="b")
plt.annotate('%0.2f' % point2desired[-1], xy=(1,point2desired[-1]), xytext=(0, 5), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="r")
plt.annotate('%0.2f' % point3desired[-1], xy=(1,point3desired[-1]), xytext=(0, -25), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="g")
plt.annotate('%0.2f' % point4desired[-1], xy=(1,point4desired[-1]), xytext=(0, 10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="k")
plt.annotate('%0.2f' % point5desired[-1], xy=(1,point5desired[-1]), xytext=(0, 5), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="c")
plt.annotate('%0.2f' % point6desired[-1], xy=(1,point6desired[-1]), xytext=(0, 7), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="m")
plt.annotate('%0.2f' % point7desired[-1], xy=(1,point7desired[-1]), xytext=(0, -15), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="b")
plt.annotate('%0.2f' % point8desired[-1], xy=(1,point8desired[-1]), xytext=(0, -9), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="r")
plt.annotate('%0.2f' % point9desired[-1], xy=(1,point9desired[-1]), xytext=(0, -18), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="g")
plt.annotate('%0.2f' % point10desired[-1], xy=(1,point10desired[-1]), xytext=(0, -24), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="k")
plt.show()

