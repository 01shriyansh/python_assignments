# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:51:43 2021

@author: hp
"""

import numpy as np

list_given=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
k=3
n=13

arr=np.array(list_given)

solution=[]
for i in range(n-k):
    sum=0
    for j in range(k):
        sum=sum+arr[i+j]
    solution.append(sum/k)

print('------------------------------')
for i in solution:
    print(i)
print('------------------------------')    