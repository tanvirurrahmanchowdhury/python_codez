# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:56:28 2022

@author: Administrator
"""

#!/usr/bin/env python

import yaml

with open("t_yl.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
    except yaml.YAMLError as exc:
        print(exc)