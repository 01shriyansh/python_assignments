# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:04:22 2020

@author: shriyansh jain
"""

#parent class
class Take_Sides:
    
    def __init__(self):                 
        print("hi..this is parent class")
        
    def take_sides(self):             #this function take sides of the triangle
        self.a=int(input("Enter Side number 1 of triangle: "))
        self.b=int(input("Enter Side number 2 of triangle: "))
        self.c=int(input("Enter Side number 3 of triangle: "))
        
    def Semiparameter(self):        #returns the value of semiperimeter
        return (self.a+self.b+self.c)/2
    
    def tell_sides(self):           #returns the sides of triangle
        return self.a,self.b,self.c


#child class    
class Calculate_area (Take_Sides):
    
    def __init__(self):
        print("Hi,this is child class")
        
    def Cal_area(self):             #To calculate the Area
        super().take_sides()        #using super fuction we can acess the functions and attributes of parent class
        a,b,c=super().tell_sides()
        s=super().Semiparameter()
        return (s*(s-a)*(s-b)*(s-c))**0.5
       
#This create the instance area of object of Calculate_area      
area=Calculate_area()
var=area.Cal_area()


print("Area of Triangle is : {}".format(var))
        
        
        
