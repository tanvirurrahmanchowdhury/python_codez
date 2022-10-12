# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:56:28 2022

@author: Administrator
"""

#!/usr/bin/env python

import yaml

with open("yaml_file_name.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
    except yaml.YAMLError as exc:
        print(exc)
        
# convert json to yaml

import yaml, json

with open('json_file_name.json', 'r') as file:
    configuration = json.load(file)

with open('yaml_file_name.yaml', 'w') as yaml_file:
    yaml.dump(configuration, yaml_file)

with open('yaml_file_name.yaml', 'r') as yaml_file:
    print(yaml_file.read())
    
# read json file and convert it to python dict
# importing the module
import json
 
# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print("\nPeople1:", data['people1'])
