# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:34:19 2020

@author: shriyansh
"""

#question 2:Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()

def even_check(num):                        #function to check even numbers in the list
    if num%2==0:
        return True
    

def myfilter(ftn,li):
    temp=list(map(ftn,li))                 #this temp varaible contains True at the index of the even element
    l1=[]
    j=0
    for i in temp:
        if(i):
            l1.append(li[j])
        j=j+1    
    return l1        

lst=[1,2,3,4,5,6,7,8,9,10]


ans=list(filter(even_check,lst))

var=myfilter(even_check, lst) 


print(ans)
print(var)