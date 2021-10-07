# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:51:16 2021

@author: Administrator
"""

import numpy as np
from scipy.optimize import brentq, curve_fit

# Eq. (17) of our PRB paper
def equation_17(u,w_p_bar,wg,y,delta,P):
    Iplus=np.sqrt((1+y ** 2) * (1+u ** 2/wg ** 2)) + u*y/wg
    Iminus=np.sqrt((1+y ** 2)*(1+u ** 2/wg ** 2)) - u*y/wg
    part1=(wg ** 2-(wg ** 2 + u ** 2) * delta ** 2)/(2*u*np.sqrt(wg ** 2+u ** 2))
    part2=(2*w_p_bar**2*delta/u**2)*((wg/u)*(np.arctan(wg*P/u) - np.arctan(wg/u))+1/P-1)
    e1=1+(w_p_bar ** 2/u ** 2)*((1-delta ** 2)*y/P-np.log(Iplus/Iminus)*part1)+part2
    return e1

n_molecule = 0.6446549401 # NO2
n_nanotube = 0.126 # nanotube
w_p_bar = np.sqrt(4*np.pi*n_molecule/3) # same as w_1
eps0 = 5 # something

wp = np.sqrt(4 * np.pi * n_nanotube) # plasma frequency
Ef = 0.5 * (3 * n_molecule * np.pi **2)**(2/3)

# penn model to compute wg
def equation_18(x):
       return (eps0-1)**2*(9/4)*x**4/(w_p_bar**4) + (eps0-1)*(3/4)*x**3/(w_p_bar**2*Ef) - 1

# inital guess was that the solution is between two reasonable points
wg = brentq(equation_18,0.1,0.7) # we guess the solution is between 0.1 to 0.7

kf = np.sqrt(2*Ef)
delta = np.sqrt(3*(kf**2)/5)
big_delta = wg/(4*Ef)
y = 1/big_delta
P = np.sqrt(1 + y**2)

u = np.arange(0.01,200,0.01) # same as du in your code
epsilon_1 = np.zeros(len(u))

for jj in range(len(u)):
    epsilon_1[jj] = equation_17(u[jj],w_p_bar,wg,y,big_delta,P)


print(epsilon_1)