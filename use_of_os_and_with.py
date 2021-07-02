import os, glob

# a path
path = 'C:/Users/Administrator'

# join pathes
new_path = os.path.join(path,'Documents')
os.chdir(new_path) # change directory
'''
find all text file (I had only one so file_name is a string.
If I has more than one txt files, file_name would be a list of strings.
'''
for file in glob.glob("*.txt"):
    file_name = file

# read the file
with open(file_name, 'r') as f:
            filestring = f.readlines() # read the first line
            print(filestring[0].split('\n')) # split the first string into a list of string sepearted by \n in this case
