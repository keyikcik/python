# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:47:48 2017

@author: kyk
"""

#%%
def if_durumlari():
    x=5
    y=0
    z=0
    if x>0:
        print("x is possitive")
        
    if y>0:
        print("y is possitive")
    else:
        print("y is not possitive")
        
    if z>0:
         print("z is possitive")
    elif z<0:
        print("z is not possitive")
    else:
        print("z must be '0'")
#%%
        """ true ve false döndürüyor, eşitlik sonucuna bakıyor"""
x=5
y=5
z=0
print("x is equal to y",x==y)
print("x is not equal to y", x!=y)
print("x is equal to z",x==z)
print("x is not equal to z",x!=z)
#%%
""" if-elif-else ile oluşturulan döngüde kare ve daire girme durumlarında alanı bulduran kod"""
def alan(type_,x):
    if type_=="circle": 
        alan=3,14*x**2
        print (alan)
    elif type_=="square":
        alan=x**2
        print(alan)
    else:
        print("what is this, I don't know")
#%% 
def absolutevalue(num):
    if num>0 :
        print("The absolute value of",num,"is",num)
    elif num<0 :
        print("The absolute value of",num,"is",num*-1)
    else :
        print("The absolute value of",num,"is",0)
#%% 
def mutlakdeger(num):
    if num>=0:
        mutlak_num=num
    else:
        mutlak_num=-num
    print(num,"sayısınım mutlak değeri=",mutlak_num)

    
    