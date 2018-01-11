#take inputs
tip=input("Aracın yakıt tipini giriniz Benzin:b ? Dizel:d ? Hibrit:h ?")
kapasite=float(input("Aracın yakıt deposunun kapasitesini lt cinsinden giriniz"))
max_mesafe=float(input(" Aracın bu  yakıtla gidebildiği maksimum mesafeyi giriniz"))
if(tip!="h"):
    full_emisyon=float(input("Aracın yol boyunca toplam CO2 salınım miktarını kg cinsinden giriniz"))

#do computations
ort_tuketim=kapasite/max_mesafe*100;
if(tip=="b"):
    ort_ucret=ort_tuketim*5.17
    ort_emisyon = full_emisyon / max_mesafe
elif(tip=="d"):
    ort_ucret=ort_tuketim*4.82
    ort_emisyon = full_emisyon / max_mesafe
else:
    ort_ucret = ort_tuketim * 5.17

#outputs

print("Aracın 100 km de ortalama yakıt tüketimi: ", format(ort_tuketim,'02.f'),"  lt dir")
print("Aracın 100 km de ortalama yakıt  ücreti:",format(ort_ucret,'02.f'), "TL dir")

if(tip!="h"):
    print("Aracın km başına ortalama CO2 salınımı", format(ort_emisyon,'0.2f')," kg dır")

