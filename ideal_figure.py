#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:28:31 2020

@author: tanvir
"""
def PlotEm(output, data_path = None, saveit = False):
    plt.rcParams.update({'font.size' : 16})
    
    #fig = plt.figure(1, figsize=(6,6))
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    
    axs[0].plot(output[:,0], output[:,1],'k', label = r'$<v^2>_{atom}$') # 1e12 because we want to plot in ps
    axs[1].plot(output[:,0], output[:,2],'k', label = r'$<v^2>_{brownian}$')
    #axs[1].ticklabel_format(useOffset=False)
    #axs[0].set_ylim([3.0,3.02])
    #plt.axhline(3.0, color='black', linestyle='dashdot', linewidth=1, alpha = 0.9)
    #axs[0].axvline(300.0, color='black', linestyle='dashdot', alpha = 0.9)
    #axs[1].axvline(300.0, color='black', linestyle='dashdot',  alpha = 0.9)
    #axs[1].set_ylim([2.5,3.5])
    #axs[1].set_ylim([700,715])
    #plt.ylabel(r'$<v>$')
    for ax in axs.flatten(): 
        ax.legend()
    plt.tight_layout()
    if saveit: 
        plt.savefig(os.path.join(data_path,'_v2_.png'), dpi=300,bbox_inches="tight")
    plt.show()
