#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:55:56 2019

@author: root
"""


import pandas as pedo
#setting libraries
dmath={'Student':['Ice bear','Panda','Grizzly'], 'Math':[80,95,79]}
delectronics={'Student':['Ice bear','Panda','Grizzly'], 'Electronics':[85,81,83]}
dgeas={'Student':['Ice bear','Panda','Grizzly'], 'GEAS':[90,79,93]}
desat={'Student':['Ice bear','Panda','Grizzly'], 'ESAT':[93,89,88]}
#dataframezzzz
math=pedo.DataFrame(dmath)
elecs=pedo.DataFrame(delectronics)
geas=pedo.DataFrame(dgeas)
esat=pedo.DataFrame(desat)
#merge
grades = pedo.merge(pedo.merge(pedo.merge(math,elecs),geas),esat)
#long to short
messy = pedo.melt(grades, id_vars=['Student'], value_vars=['Math','Electronics','GEAS','ESAT']).rename(columns={'variable' : 'Subject', 'value' : 'Grades'})
