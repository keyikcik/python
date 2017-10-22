# -*- coding: utf-8 -*-

#%% 
"""main ile program açıldığında yapılacakları koyabilirsin, burada program açıldığında hello fonksiyonunu çağırıyor"""
def hello(isim,yas):
    print('Hello', isim, yas, 'yaşındasın')
    print('merhaba'+isim+str(yas)+'yaşındasın')
    
    if isim=='Ayşegül' and yas==30:
        print('seni tanıyorum')
    else:
        print('sen de kimsin?')
    
    print(isim,"\"30 yaşındayım\" dedi")
#%%
def main():
    hello('Ayşegül',30)
#%%
"""yarıçapı girip dairenin alanını bulduruyor"""
def alandaire(radius):
    alan=3.14*radius**2
    print('yarıçapı',radius,'olan bir dairenin alanı=',alan)
#%%
""" taban ve yüksekliği verilen bir üçgeninn alanını buldurmak"""
def alanucgen(b,h):
    alan=b*h/2
    print('tabanı:',b,'yüksekliği:',h, 'olan bir üçgenin alanı:',alan)
#%%
    