#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:10:12 2018

@author: elishatam
http://alanpryorjr.com/visualizations/seaborn/heatmap/heatmap/
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.rcParams['font.family'] = "serif"

temps = pd.read_csv('20180418/temps.csv')
#df = pd.pivot_table(data=sns.load_dataset("flights"),
df = pd.pivot_table(temps,
                    index='month',
                    values='passengers',
                    columns='year')
df.head()

sns.heatmap(df)

