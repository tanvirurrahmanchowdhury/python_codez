#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 23:28:55 2021

@author: tanvir
"""

import numpy as np
import matplotlib.pyplot as plt
'''
from numpy.polynomial import polynomial as P
coefficients, _ = P.polyfit(x,y,degree,full=False)
'''

x = np.arange(0,20,0.1)
y = np.exp(-x)

curve = np.polyfit(x,y,6)
p = np.poly1d(curve)

plt.plot(x,y,x,p(x))
