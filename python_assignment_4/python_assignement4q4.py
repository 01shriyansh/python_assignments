# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:25:00 2020

@author: shriyansh jain
"""
#funciton which cheaks weather the given charachter is a vowel or not
def check_vowel(c):
        if(c =='a' or c=='e' or c=='i' or c=='o' or c=='u'):
            return True
        else:
            return False
         

lst=['a','u','q','w','r','t','i','p','s','d','o','n','e']

for i in lst:
    if(check_vowel(i)):
        print("{} is vowel".format(i))
    else:
        print("{} is not vowel".format(i))
    
    