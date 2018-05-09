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

    file_data0 = '20180506/heatmap/01_3DMetal_2D0.csv'
    file_data1 = '20180506/heatmap/03_2_3DMetal_Dungeon.csv'
    title_ax0 = '3DLEDBar on Metal, Thermal-eng off, 2D:0'
    title_ax1 = '3DLEDBar on Metal, Thermal-eng off, Dungeon'
    
    data0 = np.loadtxt(file_data0, delimiter=",", skiprows=2, usecols=range(1,321))
    data1 = np.loadtxt(file_data1, delimiter=",", skiprows=2, usecols=range(1,321))
 
#    data0 = np.loadtxt(r"20180506/heatmap/04_H39_2D0.csv", delimiter=",", skiprows=2, usecols=range(71,321))
#    data1 = np.loadtxt(r"20180506/heatmap/06_H39_Dungeon.csv", delimiter=",", skiprows=2, usecols=range(71,321))
 
    datadifference = data1 - data0
    fig, ax = plt.subplots(3, sharex=True)
#    fig, ax = plt.subplots(1, 3)
    im0=ax[0].imshow(data0, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im0, ax = ax[0])
    ax[0].set_title(title_ax0)
#    ax[0].set_ylabel('Pixel')
    i,j = np.unravel_index(data0.argmax(), data0.shape) #i = row number. j = column number
    
    #print(i+3,j+2) #Need to add in 3 in i because skip 2 rows and counting starts at 0, not 1
               #Need to add in 2 in j because skip 1 column and counting starts at 0, not 1
#    ax[0].annotate('Fig1 max value of %0.2f C at X:%i Y: %i' % (np.amax(data0), j+2, i+3), xy=(0,350), xytext=(0, 0), 
#                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print("Fig1 max value of", np.amax(data0),"at X:", j+2," Y:",i+3)
    
    
    im1=ax[1].imshow(data1, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im1, ax = ax[1])
    ax[1].set_title(title_ax1)
#    ax[1].set_ylabel('Pixel')
    i,j = np.unravel_index(data1.argmax(), data1.shape) #i = row number. j = column number
    #print(i+3,j+2) #Need to add in 3 in i because skip 2 rows and counting starts at 0, not 1
               #Need to add in 2 in j because skip 1 column and counting starts at 0, not 1
#    ax[0].annotate('Fig2 max value of %0.2f C at X:%i Y: %i' % (np.amax(data1), j+2, i+3), xy=(0,330), xytext=(0, 0), 
#                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print("Fig2 max value of", np.amax(data1),"at X:", j+2," Y:",i+3)
    
    #Focus on Top 3D LED Bar area
    data0_focusOnTop3DLED = np.loadtxt(file_data0, delimiter=",", skiprows=2, usecols=range(71,321))
    data1_focusOnTop3DLED = np.loadtxt(file_data1, delimiter=",", skiprows=2, usecols=range(71,321))
    k,l = np.unravel_index(data1_focusOnTop3DLED.argmax(), data1_focusOnTop3DLED.shape) #k = row number. l = column number
#    ax[0].annotate('Fig2 3D max value of %0.2f C at X:%i Y: %i' % (np.amax(data1_focusOnTop3DLED), l+72, k+3), xy=(0,310), xytext=(0, 0), 
#                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print("Fig2 Top 3D max value of", np.amax(data1_focusOnTop3DLED),"at X:", l+72," Y:",240-k)
    print(data1_focusOnTop3DLED, file=open("data1_focusOnTop3DLED", "a"))
#    print((np.amax(data1_focusOnTop3DLED)))
    
    
    im2=ax[2].imshow(datadifference, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im2, ax = ax[2])
    ax[2].set_title('Temperature Difference')
#    ax[2].set_xlabel('Pixel')
#    ax[2].set_ylabel('Pixel')
    i,j = np.unravel_index(datadifference.argmax(), datadifference.shape) #i = row number. j = column number
    #print(i+3,j+2) #Need to add in 3 in i because skip 2 rows and counting starts at 0, not 1
               #Need to add in 2 in j because skip 1 column and counting starts at 0, not 1
#    ax[0].annotate('Fig3 max value of %0.2f C at X:%i Y: %i' % (np.amax(datadifference), j+2, i+3), xy=(0,290), xytext=(0, 0), 
#                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print("Fig3 max value of", np.amax(datadifference),"at X:", j+2," Y:",i+3)
    
    #Focus on Top 3D LED Bar area
    datadifference_focusOnTop3DLED = data1_focusOnTop3DLED - data0_focusOnTop3DLED
    k,l = np.unravel_index(datadifference_focusOnTop3DLED.argmax(), datadifference_focusOnTop3DLED.shape) #k = row number. l = column number
#    ax[0].annotate('Fig3 3D max value of %0.2f C at X:%i Y: %i' % (np.amax(datadifference_focusOnTop3DLED), l+72, k+3), xy=(0,270), xytext=(0, 0), 
#                 xycoords=('figure fraction', 'data'), textcoords='offset points',color="k",)
    print("Fig3 Top 3D max value of", np.amax(datadifference_focusOnTop3DLED),"at X:", l+72," Y:",240-k)    
    plt.show()
    
def calculate_aspect(shape, extent):
    dx = (extent[1] - extent[0]) / float(shape[1])
    dy = (extent[3] - extent[2]) / float(shape[0])
    return dx / dy

main()



