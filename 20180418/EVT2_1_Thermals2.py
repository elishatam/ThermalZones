#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:29:20 2018

@author: elishatam
"""
import matplotlib.dates as mtdates
import matplotlib.pyplot as plt
import numpy as np



# reading all lines into list of string
with open(r"ZoneDungeon3D255.csv") as f:
    content = f.readlines()

content = [x.strip() for x in content]

dates = []
zone9_list = []
for line in content:
    splt = line.split(',')
    dates.append(splt[3])
    zone9_list.append(float(splt[8]))
    
#time = np.arange(0, len(dates))
plt.figure()
#plt.scatter(time, zone9_list, label="Zone9-lcd_therm")
plt.scatter(dates, zone9_list, label="Zone9-lcd_therm", color="y")


# reading all lines into list of string
with open(r"FlirDungeon3D255_minute.csv") as f:
    content = f.readlines()

content = [x.strip() for x in content]

dates2 = []
point1 = []
point2 = []
point3 = []
point4 = []
for line in content:
    splt = line.split(',')
    dates2.append(float(splt[5]))
    point1.append(float(splt[6]))
    point2.append(float(splt[7]))
    point3.append(float(splt[8]))
    point4.append(float(splt[9]))

#plt.scatter(dates2,point1)

dates2desired = dates2[1::200]
point1desired = point1[1::200]
point2desired = point2[1::200]
point3desired = point3[1::200]
point4desired = point4[1::200]

#print(point1desired)
#plt.plot_date(dates2, point1)
#plt.xlim(0,30)
plt.scatter(dates2desired,point1desired,label="Spot1",color="b")
plt.scatter(dates2desired,point2desired,label="Spot2",color="r")
plt.scatter(dates2desired,point3desired,label="Spot3",color="g")
plt.scatter(dates2desired,point4desired,label="Spot4",color="k")

#plt.xlim(0,30)
#plt.ylim(0,55)

plt.title('Dungeon 3D:255')
plt.xlabel('Time (min)')
plt.ylabel('Temperature (C)')
#plt.xlim(-5,30)
plt.xticks(rotation=30)
plt.ylim(0,55)
plt.legend(loc='lower right', frameon=True)



plt.annotate('%0.2f' % zone9_list[-1], xy=(1,zone9_list[-1]), xytext=(0, 5), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="y")
plt.annotate('%0.2f' % point1desired[-1], xy=(1,point1desired[-1]), xytext=(0, 10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="b")
plt.annotate('%0.2f' % point2desired[-1], xy=(1,point2desired[-1]), xytext=(0, -2), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="r")
plt.annotate('%0.2f' % point3desired[-1], xy=(1,point3desired[-1]), xytext=(0, -10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="g")
plt.annotate('%0.2f' % point4desired[-1], xy=(1,point4desired[-1]), xytext=(0, 10), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points',color="k")
plt.show()