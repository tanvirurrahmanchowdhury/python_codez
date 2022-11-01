my_db= VaspCalcDb.from_db_file('/home/apike/miniconda3/envs/my_atomate/config/db.json') #load data from the db
calcs = my_db.collection.find({'state':'successful'},projection={'formula_pretty':1,'output.energy_per_atom':1,'calcs_reversed.run_type':1,'calcs_reversed.input.potcar_spec':1,'output.spacegroup.symbol':1,'_id':1})
