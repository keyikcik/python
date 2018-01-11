import math
def sayi_al(alt_sinir,ust_sinir):
    sayi=float(input())
    while (sayi<alt_sinir or sayi>ust_sinir):
        print("Hata:belirtilen aralıkta sayi giriniz.",end="")
        sayi=float(input())
    return sayi

def dikdortgenin_alani(kenar1,kenar2):
    return kenar1*kenar2

def karenin_alani(kenar):
    return dikdorgenin_alani(kenar,kenar)

def eskenar_ucgenin_alani(kenar):
    return (kenar**2)*math.sqrt(3)/4
def dairenin_alani(yaricap):
    return math.pi*yaricap**2

def dikdortgen_prizmanin_hacmi(kenar1,kenar2,yukseklik):
    return dikdortgenin_alani(kenar1,kenar2)*yukseklik
def kare_prizmanin_hacmi(kenar,yukseklik):
    return dikdortgen_prizmanin_hacmi(kenar,kenar,yukseklik)

def kupun_hacmi(kenar):
    return kare_prizmanin_hacmi(kenar,kenar)

def eskenar_ucgen_prizmanin_hacmi(kenar,yukseklik):
    return eskenar_ucgenin_alani(kenar)*yukseklik

def silindirin_hacmi(yaricap,yukseklik):
    return dairenin_alani(yaricap)*yukseklik



def main():

    print(" [2,10]  aralığinda birinci  reel sayiyi giriniz ",end="")
    sayi1=sayi_al(2,10)
    print(" [2,10]  aralığinda ikinci  reel sayiyi  giriniz ", end="")
    sayi2 = sayi_al(2, 10)
    print(" [2,10]  aralığinda ücüncü  reel sayiyi  giriniz ", end="")
    sayi3 = sayi_al(2, 10)

    print(" taban kenar uzunlukları" ,sayi1," ve", sayi2," olan, yüksekliği", sayi3," olan dikdörtgen prizmanın hacmi:",
          format(dikdortgen_prizmanin_hacmi(sayi1,sayi2,sayi3),'.2f'))

    print(" taban kenar uzunlugu", sayi1+sayi2, " olan, yüksekliği", sayi3,
          " olan kare prizmanın hacmi:",
          format(kare_prizmanin_hacmi(sayi1+sayi2, sayi3), '.2f'))

    print("  kenar uzunlugu", sayi1 + sayi2+sayi3, " olan kare prizmanın hacmi:",
          format(kupun_hacmi(sayi1 + sayi2+ sayi3), '.2f'))

    print(" taban kenar uzunlugu", sayi1 + sayi2, " olan, yüksekliği", sayi3,
          " olan eskenar ücgen prizmanın hacmi:",
          format(eskenar_ucgen_prizmanin_hacmi(sayi1 + sayi2, sayi3), '.2f'))

    print(" taban capi", sayi1+sayi2, " olan, yüksekliği", sayi3,
          " olan silindirin hacmi:",
          format(silindirin_hacmi((sayi1+sayi2)/2, sayi3), '.2f'))



main()