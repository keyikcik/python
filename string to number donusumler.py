# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:48:12 2017

@author: kyk
"""

#%% 
""" fahrenhayt to celcius program"""
def fah_to_cel():
    temp_str=input("Enter a ahrenhayt Temperature:")
    temp=int(temp_str)
    cel=5*(temp-32)/9
    print("the Fahrenhayt teperature",temp,"is equal to", cel,"degrees Celcius")
"""evet program çalışıyor ama değeri girmeden entera basınca ya da sayı girmediğimizde hata veriyor"""
"""daha işlevsel hali true/false yöntemi ile girilen sayıyı kontrol etmek"""
#%% 
"""öncekinde sayı girmeden entere basıldığında hata veriyordu bu onu önlüyor"""
"""bir değer girildiyse true veriyor"""
"""ama hala hata var çünkü sayı değil de yazı girilebilirdi"""
def fahtocel():
    temp_str=input("Enter a ahrenhayt Temperature:")
    if temp_str:
         temp=int(temp_str)
         cel=5*(temp-32)/9
         print("the Fahrenhayt teperature",temp,"is equal to", cel,"degrees Celcius")

#%% 
         """ sayı mı diye kontrol eden .isdigit digit sayı demek"""
def fahtocel3():
    temp_str=input("Enter a fahrenhayt Temperature:")
    if temp_str:
        if temp_str.isdigit():
             temp=int(temp_str)
             cel=5*(temp-32)/9
             print("the Fahrenhayt teperature",temp,"is equal to", cel,"degrees Celcius")
        else:
            print("you must enter a number, BYE!")
    else:
        print("you did not enter anything, Bye")
#%% 
"""yeni program : inches to feet converter"""
""" / bölme yapar, // tam sayı bölmesi yapar"""
""" a=b%12 a sayısı b nin 12 ye bölümünden kalandır"""
def inchtofeet():
    inches_str=input("Enter a İnches value: ")
    
    if inches_str:
        inches=int(inches_str)
        feet=inches//12
        extrainch=inches-feet*12 #extrainches=inches%12
        print(inches,"inches equal to:",feet,"feet and",extrainch,"inches")
    else:
        print("you should enter a value")
        