#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:51:49 2018

@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np
X = [1,2,3,4,5]
Y = [2,4,6,8,10]
Z = [3,6,9,12,15]
plt.figure()
plt.plot(X,Y)
plt.plot(Y,Z)