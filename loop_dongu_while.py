# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:51:33 2017

@author: kyk
"""

#%%
def dongu():
    num=2
    while num<=10:
        print(num, end=" ") #end=" " aynı satırda devam ettirmek için kullanılıyor
        num=num+2
    print()
    while num>=0:
        print(num, end=" ")
        num=num-1
#%%
        """kodda bir hata var negatif değer giremiyorum metin algılıyor"""
def sayi():
   # a_str=input("bir sayı giriniz: ")
   # if a_str: 
       # a=int(a_str)
       a=int(input("bir sayı giriniz:"))
       if a:
        #if  a>0: 
            while a>0:
                print(a,end=" ")
                a=a-1
            print()
       # elif a<0:
            while a<0:
                print(a,end=" ")
                a=a+1
            print()
       # else:
         #   print(a)           
    else:
        print("hiçbişey girmediniz, Bye!")
                