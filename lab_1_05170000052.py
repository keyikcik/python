#by utku erdogan, 05170000052

##take  inputs
ad_soyad=input("sürücü ismini giriniz")
kapasite=float(input("yakıt deposunun kapasitesini litre cinsinden giriniz."))
ort_tuketim=float(input("100 km de ortalama yakıt tuketimini litre cinsinden giriniz"))
beklenti=float(input("Kaç km gitmeyi planlıyorsunuz?"))

#do  calculations

min_miktar=beklenti*ort_tuketim/100
ucret=min_miktar*5.17
depo_ucret=kapasite*5.17
max_mesafe=kapasite*100/ort_tuketim

# give outputs

print("Sayın  ",ad_soyad )
print("Almanız gereken minimum yakıt miktarı  ",format(min_miktar,".2f")," lt dir")
print("Bunun için ",format(ucret,".2f"), " TL odemelisiniz")
print("Bir depo yakıt için", format(depo_ucret,".2f")," TL odeyerek")
print(format(max_mesafe,".2f")," km yol gidebilirsiniz")