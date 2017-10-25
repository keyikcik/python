# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:12:09 2017

@author: kyk
"""
#%%
isim=   "Mekanın adı : AYSEGUL'S KİTCHEN"
isim2= 'mekanın ismi: "AYŞEGÜL"ÜN MUTFAĞI"'
print(isim)
print(isim2)
#%%
"""fahrenhaytı cantigrata çeviren fonksiyon"""
def fahrenheit_to_celcius(temp):
    cel_temp=5*(temp-32)/9
    print(temp,"fahrenheit",cel_temp,"santigrattır")
#%%
def celcius_to_fah(temp):
    new_temp=temp*9/5+32
    print(temp, "santigrat", new_temp,"fahrenhaeit'tır")
#%%
a="Aysegul"
"""ilk harf 0 ile başlıyor !!! 0123456 ya da geriye doğru da kullanılabiliyor 
   geriye doğru da gidilebilir -7-6-5-4-3-2-1 """
a[3] 
"""e"""
a[0:4]
"""Ayse"""
a[1:]
"""ysegul"""
a[-1]
"""l"""
a[-3:-1]
"""gu"""
a[-3:0]
"""gul""" 

#%%
a=121%12
