#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:23:56 2019

@author: root
"""

import pandas as pedo
dbox= {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'], 'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
messy=pedo.DataFrame(dbox)
tidy = messy.pivot_table(index=['Box'],columns=['Dimension'],values='Value')
tidy['Volume'] = tidy.Length*tidy.Height*tidy.Width