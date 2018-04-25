#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:41:35 2018

@author: elishatam
https://stackoverflow.com/questions/18784354/imshow-when-you-are-plotting-data-not-images-realtion-between-aspect-and-exten/36307312#36307312
https://matplotlib.org/examples/images_contours_and_fields/pcolormesh_levels.html
"""

import matplotlib.pyplot as plt
import numpy as np

#a = np.random.random((16, 16))
#plt.imshow(a, cmap='hot', interpolation='nearest')
#plt.show()
#print(a)

##data = np.random.random((5, 15))
#data = np.loadtxt(r"20180418/3D_255_2_test.csv", delimiter=",", skiprows=10, usecols=range(1,255))
#fig, ax = plt.subplots()
#ax.imshow(data, extent=[-130,130,0,77])
#plt.show()
##print(data)

def main():
#    shape = (30, 1295)
#    extent = [-130,130,0,77]
    shape = (240, 321)
    extent = [0,321,0,240]


#    data = np.random.random(shape)
#    data0 = np.loadtxt(r"20180423/heatmap/03_Sleep_USBIn_Charging_Front.csv", delimiter=",", skiprows=2, usecols=range(1,321))
#    data1 = np.loadtxt(r"20180423/heatmap/02_Sleep_USBIn_Notcharging_Front.csv", delimiter=",", skiprows=2, usecols=range(1,321))
#    datadifference = data1 - data0
#    fig, ax = plt.subplots()
#    im=ax.imshow(datadifference, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
#    fig.colorbar(im)
#    plt.show()
#    print(datadifference)

    data0 = np.loadtxt(r"20180425/heatmap/03_3D255.csv", delimiter=",", skiprows=2, usecols=range(1,321))
    data1 = np.loadtxt(r"20180425/heatmap/06_Dungeon.csv", delimiter=",", skiprows=2, usecols=range(1,321))
    datadifference = data1 - data0
    fig, ax = plt.subplots(3, sharex=True)
#    fig, ax = plt.subplots(1, 3)
    im0=ax[0].imshow(data0, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im0, ax = ax[0])
    ax[0].set_title('3D: 255')
    ax[0].set_ylabel('Pixel')
    i,j = np.unravel_index(data0.argmax(), data0.shape) #i = row number. j = column number
    
    #print(i+3,j+2) #Need to add in 3 in i because skip 2 rows and counting starts at 0, not 1
               #Need to add in 2 in j because skip 1 column and counting starts at 0, not 1
    ax[0].annotate('Fig1 max value of %0.2f C at X:%i Y: %i' % (np.amax(data0), j+2, i+3), xy=(0,280), xytext=(0, 0), 
                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)

    
    
    im1=ax[1].imshow(data1, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im1, ax = ax[1])
    ax[1].set_title('Dungeon Masters, 4x1, ACT On, DOF On')
    ax[1].set_ylabel('Pixel')
    i,j = np.unravel_index(data1.argmax(), data1.shape) #i = row number. j = column number
    #print(i+3,j+2) #Need to add in 3 in i because skip 2 rows and counting starts at 0, not 1
               #Need to add in 2 in j because skip 1 column and counting starts at 0, not 1
    ax[0].annotate('Fig2 max value of %0.2f C at X:%i Y: %i' % (np.amax(data1), j+2, i+3), xy=(0,260), xytext=(0, 0), 
                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print(np.amax(data1))
    
    im2=ax[2].imshow(datadifference, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im2, ax = ax[2])
    ax[2].set_title('Temperature Difference')
    ax[2].set_xlabel('Pixel')
    ax[2].set_ylabel('Pixel')
    i,j = np.unravel_index(datadifference.argmax(), datadifference.shape) #i = row number. j = column number
    #print(i+3,j+2) #Need to add in 3 in i because skip 2 rows and counting starts at 0, not 1
               #Need to add in 2 in j because skip 1 column and counting starts at 0, not 1
    ax[0].annotate('Fig3 max value of %0.2f C at X:%i Y: %i' % (np.amax(datadifference), j+2, i+3), xy=(0,240), xytext=(0, 0), 
                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print(np.amax(datadifference))
    
    plt.show()
    
def calculate_aspect(shape, extent):
    dx = (extent[1] - extent[0]) / float(shape[1])
    dy = (extent[3] - extent[2]) / float(shape[0])
    return dx / dy

main()

#with open("20180418/3D_255_2_test.csv") as f:
#    ncols = len(f.readline().split(','))
#data = np.loadtxt(open("20180418/3D_255_2.csv", "rb"), delimiter=",", skiprows=1)
#data = np.loadtxt(r"20180418/3D_255_2_test.csv", delimiter=",", skiprows=10, usecols=range(1,255))

#data3=np.loadtxt(r"H43_H46_H21.csv", delimiter=',',skiprows=1)

