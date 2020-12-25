# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:38:14 2020

@author: shriyansh jain
"""

#quetion 1:Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()

from functools import reduce

def myreduce(ftn,li):
    temp=[]
    for i in range(len(li)-1):          #iterate through the list 
        temp=ftn(li[i],li[i+1])         #apply the function on i and i+1 elment of the list
        li[i+1]=temp
    return temp                         # we return the temp variable as it has the last operation value stored in it.    
        
                  

#example

lst =[1,2,3,4,5,6,7,8]

ans=reduce(lambda a,b: a+b,lst)

var=myreduce(lambda a,b: a+b, lst)

#to check weather it is working properly or not.
print(ans)

print(var)


