def sayi_al(haftalik):
    for ind in range(6):
        print(ind+1," i  ninci sayiyi gir :[1-49] arası ")
        sayi=int(input())
        while (sayi>49 or sayi<1 or sayi in haftalik[0:ind]):
            print('hata',ind + 1, " i  ninci sayiyi gir :[1-49] arası ")
            sayi = int(input())
        haftalik[ind]=sayi



tum_sayilar=[0]*49 #sayac vektörü

flag='e'

while (flag=='e'):
    haftalik=[0]*6
    sayi_al(haftalik)
    for ind in haftalik:
        tum_sayilar[ind-1]+=1

    flag=input(" baska hafta e,H ?")
print("sayi \t\t frekans")
print("----- \t \t ------")
for ind in range(1,50):
    print(ind,end="\t\t\t\t")
    print(tum_sayilar[ind-1])