# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from pymatgen.io.vasp.outputs import Vasprun
import numpy as np

work_dir = os.getcwd()

all_data = []
        
dirs = os.listdir(work_dir)
dir_print = []
for d in dirs: 
    try: 
        file_path = os.path.join(work_dir, d) 
        if os.path.isdir(file_path):
            dir_print.append(d) 
            os.chdir(file_path)
            vrun = Vasprun(filename="./vasprun.xml")
            if(vrun.converged):
                print(f"Energies were successfully converged for {d}")
                all_data.append( vrun.final_energy )
            else: 
                print("Sorry! Energies were not converged.")

    except Exception as e: 
        print(e)
        dir_print.append(d)
        all_data.append('NA')

#np.savetxt('report.txt',list(zip(dirs,all_data)))

os.chdir(work_dir)
with open('report.txt', 'w') as f:
    for f1, f2 in zip(dir_print, all_data):
        print(f1, f2, file=f)
