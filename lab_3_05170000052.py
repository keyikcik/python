tip=input("Aracın motor tipini giriniz. benzinli:b, dizel:d, otogaz:o:,hibrit:h")
ort_yakit=float(input("Aracın 100  km de tükettiği  ortalama yakıt miktarini giriniz"))

#####
if (tip=='h' or tip=='b'):
    ort_ucret=ort_yakit*5.17
elif (tip=='d'):
    ort_ucret=ort_yakit*4.82
else:
    ort_ucret=ort_yakit*3.29


#####

if (ort_ucret <= 20):
    sinif='A'
elif (ort_ucret <=30 ):
    sinif='B'
elif (ort_ucret <=40 ):
    sinif='C'
elif (ort_ucret<=50):
    sinif='D'
else:
    sinif='E'

#######

print(" Aracin 100 km de tükettiği yakitin ortalama ücreti",format(ort_ucret,'.2f'),' TL  dir')
print("Arac yakit tüketimine göre  ",sinif, ' sinifindadir.')


