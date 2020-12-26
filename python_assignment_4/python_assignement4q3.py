# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:14:28 2020

@author: shriyansh jain
"""
#this is an example string..!!
lst=["shriyansh","jain","cricket","football","hockey"]

#map fuction apply the function given to each elemnet and then we convert it into list
final_list = list(map(lambda x: len(x) , lst)) 

print(final_list) 