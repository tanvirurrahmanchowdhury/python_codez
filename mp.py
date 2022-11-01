# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from tqdm  import tqdm

from pymatgen.ext.matproj import MPRester
#from pymatgen.core import Structure
from pymatgen.io.vasp.sets import MPRelaxSet


'''struc = Structure.formula("Si")
print(struc)

'''

MY_API= os.environ["MY_API"]

with MPRester(MY_API) as m:

    # Structure for material id
    struc = m.get_structure_by_material_id("mp-125")

    #struc = m.get_structures("Si")
    # Dos for material id
    #dos = m.get_dos_by_material_id("mp-1234")

    # Bandstructure for material id
    #bandstructure = m.get_bandstructure_by_material_id("mp-1234")

print(struc)
#struc.remove_sites([0])
#we can also use struc.remove_species() replace_species({"Ba":"Pb"})
## structure.make_supercell([3,3,3])      # Make a supercell 3x3x3

#relax_set = MPRelaxSet(structure=struc)
#relax_set.write_input(output_dir="./test_arsenal")
print("All VASP files have been created successfully!")
