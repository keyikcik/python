# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:47:23 2017

@author: kyk
"""
#%%
def name():
    fname=input("Name?  :")
    lname=input("Surname?  :")
    fullname=fname+" "+lname
    print("Welcome",fullname)
    cname=input("What is the city name you live in?    :")
    coname=input("In which country it is?")
    city_state=cname + "," + coname   
    print(city_state,".Great!")
#%%
