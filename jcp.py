#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:40:07 2021

@author: tanvir_chowdhury
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,5)
y1 = np.array([-0.11,-1.16,0.16,-0.24])
y2 = np.array([0.23,-1.88,0.95,0.49])
y3 = np.array([0.79,-0.95,2.33,1.61])
plt.plot(x,y1,linewidth=5,marker='o',markersize=25,label='SCAN')
plt.plot(x,y2,linewidth=5,marker='o',markersize=25,label='PBE')
plt.plot(x,y3,linewidth=5,marker='o',markersize=25,label='LSDA')
plt.grid(axis='x')
#plt.plot(d,fourL,linestyle='dashed',linewidth=4,label='MoS2 4 Layers; c = 21.5 Angstrom')
#plt.xlabel(r'$\bar{b}$',fontsize=26)
plt.xticks(np.arange(1,5), [r'$B_2$', r'$C_2$', r'$O_2$',r'$F_2$'])
plt.ylabel('Errors',fontsize=26)
#plt.ylim(-4.1, -2.8)
plt.legend(loc=4,fontsize=26)
plt.rc('xtick',labelsize=26)
plt.rc('ytick',labelsize=26)
plt.show()