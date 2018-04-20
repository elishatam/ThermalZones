#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:41:35 2018

@author: elishatam
https://stackoverflow.com/questions/18784354/imshow-when-you-are-plotting-data-not-images-realtion-between-aspect-and-exten/36307312#36307312
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
    data = np.loadtxt(r"20180418/3D_255_2_test.csv", delimiter=",", skiprows=10, usecols=range(1,321))

    fig, ax = plt.subplots()
    im=ax.imshow(data, extent=extent, aspect=calculate_aspect(shape, extent), cmap='afmhot')
    fig.colorbar(im)
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

