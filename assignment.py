# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:06:45 2024

@author: ECE SU
"""

"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
def std_loops():
    x = [1,2,3,4,5]
    
    mean = (x[0]+x[1]+x[2]+x[3]+x[4])/5
    
    b=(x[0]-mean)**2
   
    b1=(x[1]-mean)**2
    
    b2=(x[2]-mean)**2
    
    b3=(x[3]-mean)**2
    
    b4= (x[4]-mean)**2
    
    sqr_mean= (b+b1+b2+b3+b4)/5
    
    from math import sqrt
    sqrt(sqr_mean)
    print(sqrt(sqr_mean))
    
std_loops()


def std_builtin():
    import math
    
    #declare the dataset list
    x = [1,2,3,4,5]
    
    #find the mean of dataset
    sm=0
    for i in range(len(x)):
       sm+=x[i]
       mean = sm/len(x)
    
    #calculating population standard deviation of the dataset
    deviation_sum = 0
    for i in range(len(x)):
       deviation_sum+=(x[i]- mean)**2
       psd = math.sqrt((deviation_sum)/len(x))
    
    #display output
    print(psd)

    
std_builtin()   