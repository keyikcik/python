# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:02:46 2017

@author: kyk
"""

#%% 
""" range(startnumber, stop number, step)"""
def say():
    for a in range(1,10,2):
        print(a,end=" ")
#%% 
def say1():
    a=int(input("Enter starting number: "))
    b=int(input("Enter starting number: "))
    for x in range(a,b,2):
        print(x,end=" ")
#%%
def say3():
    for a in range(10,0,-1):
        print(a,end=" ")