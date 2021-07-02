import pickle
import numpy as np
# creating a random dictionary
data_dict = {'volts':np.random.random(10),'current':np.random.random(10)}

# writing a binary (wb) pickle file (extension pkl)
# the variable of with is pickle_file
with open('data_pick.pkl', 'wb') as pickle_file:
    pickle.dump(data_dict,pickle_file) # dump(data_to_be_pickled,with variable)
    

with open('data_pick.pkl', 'rb') as pickle_file:
    new_data = pickle.load(pickle_file) # new_data = dump(with variable)
