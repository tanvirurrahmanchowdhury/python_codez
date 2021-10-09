# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:53:33 2021

@author: Administrator
"""

import time, math

import multiprocessing as mp

#print(mp.cpu_count()) counting the nuber of cpus available

r_a = []
r_b = []
r_c = []

def f_1(numbers): # a random function
    for n in numbers:
        r_a.append(math.sqrt(n**3))
        
def f_2(numbers):
    for n in numbers:
        r_b.append(math.sqrt(n**3))

def f_3(numbers):
    for n in numbers:
        r_c.append(math.sqrt(n**3))
        
if __name__ == '__main__':
    n_list = list(range(1000000))
    
    # begin multiprocessing
    # p1 = mp.Process(target=f_1,args=(n_list,)) # target = function_name, argrs = argument list as tuple
    # p2 = mp.Process(target=f_2,args=(n_list,))
    # p3 = mp.Process(target=f_3,args=(n_list,))
    
    
    # start = time.time()
    # p1.start()
    # p2.start()
    # p3.start()
    # end = time.time()
    # print(end-start)
    # end multiprocessing
    
    #begin serial processing
    start = time.time()
    f_1(n_list)
    f_2(n_list)
    f_3(n_list)
    end = time.time()
    print(end-start)
    # end serial processing
