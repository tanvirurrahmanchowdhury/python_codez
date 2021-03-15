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
x = np.arange(0,20,0.1)
y = np.exp(-x)

coefficients = P.polyfit(x,y,3)

# order c[0], c[1], .. etc.
# note fitting function = c[0] + c[1]*x + c[2]*x**2 + ...
# Then
print(coefficients)
plt.plot(x,y,x,P.polyval(x, coefficients))
'''

x = np.arange(0,20,0.1)
y = np.exp(-x)

curve = np.polyfit(x,y,6) # c[6], c[5], ...
p = np.poly1d(curve)

plt.plot(x,y,x,p(x))
