# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:05:58 2024

@author: ECE SU
"""
def argmax(values):
    
 N = len(values)
 imax= 0
 Vmax= values[0]
 for l in range(1,11):
     v= values[i]
     if v> vmax:
        
        imax= i
        vmax= v
        return imax,vmax
def main():
    values= [2,3,-1,7,4]
    imax,vmax= argmax(values)
    print('flocation of max: (max), value: (vmax)')
    