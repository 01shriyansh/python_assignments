# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:55:38 2020

@author: shriyansh jain

"""

def printt(subjects,verbs,objects):    
    for i in subjects:
        for j in verbs:
            for k in objects:
                print("{} {} {}".format(i,j,k))
            

subjects=["Americans ","Indians","Germans"]
verbs=["play","watch"]
objects=["Baseball","Cricket","Football"]
   
printt(subjects,verbs,objects)         