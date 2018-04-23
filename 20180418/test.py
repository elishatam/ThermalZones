#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:51:49 2018

@author: elishatam
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#X = [1,2,3,4,5]
#Y = [2,4,6,8,10]
#Z = [3,6,9,12,15]
#plt.figure()
#plt.plot(X,Y)
#plt.plot(Y,Z)

#5:05:54 PM
date_string = '05:05:54 PM'
format = '%I:%M:%S %p'
#date_string = '2009-11-29 03:17 PM'
#format = '%Y-%m-%d %I:%M %p'
my_date = datetime.strptime(date_string, format)

# This prints '2009-11-29 03:17 AM'
print(my_date.strftime(format))