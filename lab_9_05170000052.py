
def sayi_al(alt_sinir,ust_sinir):
    sayi=int(input())
    while (sayi<alt_sinir or sayi>ust_sinir):
        print("Hata:belirtilen aralÄ±kta sayi giriniz.",end="")
        sayi=int(input())
    return sayi

satir_say=10
sutun_say=4

notlar=[0]*satir_say
for ind in range(satir_say):
    notlar[ind]=[0]*sutun_say

print("[1,4]  araliğinda tamsayi olarak öğrenci sinifini giriniz.")
ogr_sinif=sayi_al(1,4)

while(ogr_sinif!=0):
    print("[1,100]  araliğinda tamsayi olarak öğrenci notunu giriniz.")
    ogr_not = sayi_al(1, 100)
    grup=ogr_not//satir_say # lab yazili kaginda if elif kullandim. bu aklima geldiğinde süre bitmişti. What a shame!
    notlar[grup][ogr_sinif-1]+=1

    print("[1,4]  araliğinda tamsayi olarak öğrencinin sinifini giriniz. ogrenci yoksa 0 gir.")
    ogr_sinif = sayi_al(0, 4)


print("Gruplar",end="")

for sutun in range(sutun_say):
    print(format(sutun+1,"13"),end="")
print("\t\t\tToplam")

for sutun in range(sutun_say+1):
    print(format("---------","13"),end="")
print("\t-----")
for satir in range(satir_say):
    print(format(satir*10,'3'),'--',format((satir+1)*10,'3'),end="")
    for sutun in range(sutun_say):
        print(format(notlar[satir][sutun],"11"),end=" ")
    print ( format( sum(notlar[satir]),"13") )


