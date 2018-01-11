#initilizations
counter_b=0;counter_d=0;counter_o=0
ucret_b=0;ucret_d=0;ucret_o=0

flag='E'

while(flag=='E'):
    tip=input('motor tipini giriniz: Benzinli=b ? Dizel=d ? Otogaz=o')
    ucret=float(input("Odenen yakit  ucretini giriniz. (TL)"))
    if (tip=='b'):
        counter_b+=1;ucret_b+=ucret
    elif (tip=='d'):
        counter_d+=1;ucret_d+=ucret
    else:
        counter_o+=1;ucret_o+=ucret
    flag=input("Başka araç var mı? E\H")



#desired calculations
toplam_arac=counter_b+counter_d+counter_o
toplam_ucret=ucret_b+ucret_d+ucret_o

dizel_sayi_yuzdesi=counter_d/(toplam_arac)*100
dizel_ucret_yuzdesi=ucret_d/(toplam_ucret)*100


ortalama_ucret=toplam_ucret/(toplam_arac)


###outputs
print(" Benzinli arac sayisi :",counter_b)
print("Dizel araç sayisı: ",counter_d)
print("Otogazlı araç sayisi",counter_o)
###
print("Benzine yaplan toplam odeme: ", format(ucret_b,'.2f'),"TL")
print("Dizele yaplan toplam odeme: ", format(ucret_d,'.2f'),"TL")
print("Otogaza yaplan toplam odeme: ", format(ucret_o,'.2f'),"TL")
###
print(" Dizel taşıtların sayısının, tüm taşıtlar içindeki yüzdesi : %",format(dizel_sayi_yuzdesi,'.2f'))
print(" Dizel taşıtların toplam yakıt giderinin, tüm taşıtların toplam yakıt gideri içindeki yüzdesi \
: %",format(dizel_ucret_yuzdesi,'.2f'))

##
print("Toplam arac sayisi", toplam_arac)

print("Toplam yakıt ucreti",format(toplam_ucret,'.2f'))

print("Şirketteki bir taşıtın aylık ortalama yakıt gideri :", format(toplam_ucret,'.2f'),'TL')