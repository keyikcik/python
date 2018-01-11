
## Cevabı  Evet hayır olan  soruları sorup cevaplarını boolean değişkenlere
##çeviren bir fonksiyon
def evet_hayir(soru):
    print(soru+'e/E/h/H',end="")
    cevap=input()
    while cevap not in ['e','E','H','h']:
        print(soru + 'e/E/h/H', end="")
        cevap = input()
    if cevap in ['e','E']:
        return True
    else:
        return False
#sayaçlar ve toplamlar için başlangıç değerleri
tum_cocuk_say=0
tum_net_ucret=0
tum_gelir_kesintisi=0
tum_toplam_brut_ucret=0
max_toplam_brut_ucret=0
max_net_ucret=0
say_calisan=0
say_200_tl=0
say_100_tl=0
say_50_tl=0
say_20_tl=0
say_10_tl=0
say_5_tl=0
say_1_tl=0
say_50_kurus=0
say_25_kurus=0
say_10_kurus=0
say_5_kurus=0
say_1_kurus=0

say_engelli=0


say_1_vergi_dilimi=0
say_2_vergi_dilimi=0
say_3_vergi_dilimi=0
say_4_vergi_dilimi=0

say_net_2000_alti=0

say_evli=0
say_es_calisiyor=0

say_cocuklu_calisan=0
say_ucten_fazla_cocuklu=0
brut_asgari_ucret=1777.5
calisan_var=True



while calisan_var:
    say_calisan += 1
    #Her çalışan için varsayılan değerler, aksi durumlarda aşağıda değişecek.
    es_yardimi=0
    cocuk_yardimi=0
    engelli_indirimi=0
    ## girdiler alınıyor.
    kimlik_no=input("TC kimlik no yu giriniz")
    ad_soyad=input("çalışanın adini ve soyadını giriniz")
    print(" aylik brut ücreti giriniz.",brut_asgari_ucret ," veya  daha fazla",end="")
    brut_ucret=float(input())
    while (brut_ucret<brut_asgari_ucret):
        print("Hata::aylik brut ücreti giriniz.", brut_asgari_ucret, " veya  daha fazla", end="")
        brut_ucret = float(input())

    medeni_durum=input("calisanin medeni durumu:e/b/E/B ?")
    while medeni_durum not in ['e','b','E','B']:
        medeni_durum = input("Hata::calisanin medeni durumu:e/b/E/B ?")

    if medeni_durum in ['e','E']:
        say_evli+=1
        es_calisiyor=evet_hayir("es_calisiyor mu ?")
        if(es_calisiyor):
            say_es_calisiyor+=1
        else:
            es_yardimi = 220
    cocuk_say=int(input("cocuk sayisi? cocuk yoksa 0 giriniz"))
    while cocuk_say<0:
        cocuk_say = int(input("Hata ::cocuk sayisi? cocuk yoksa 0 giriniz"))

    if cocuk_say>0:
        say_cocuklu_calisan+=1
        tum_cocuk_say+=cocuk_say
        if(cocuk_say>3):
            say_ucten_fazla_cocuklu+=1
        altidan_buyuk_say=int(input("alti yasindan büyük cocuk sayisini giriniz. Cocuklar alti_yasindan buyuk değilse 0 giriniz"))
        while(altidan_buyuk_say<0):
                altidan_buyuk_say = int( input("alti yasindan büyük cocuk sayisini giriniz. Cocuklar alti_yasindan buyuk değilse 0 giriniz"))

        cocuk_yardimi=(altidan_buyuk_say*45+(cocuk_say-altidan_buyuk_say)*25)


    engelli_mi=evet_hayir("Calışan engelli mi?")
    if(engelli_mi):
        say_engelli+=1
        engel_orani=int(input("Engel oranını [1,100] aralıgında tamsayi olarak giriniz"))
        while (engel_orani<1 or engel_orani>100):
            engel_orani = int(input("Hata::Engel oranını [1,100] aralıgında tamsayi olarak giriniz"))
        if engel_orani >= 80:

            engelli_indirimi=900
            engel_derecesi="1.derece engelli"
        elif engel_orani >= 60:

            engelli_indirimi=470
            engel_derecesi="2. derece engelli"
        elif engel_orani >= 40:

            engelli_indirimi=210
            engel_derecesi="3.derece engelli"
        else:
            engelli_indirimi=0
            engel_derecesi="Bu engel oranı derecelendirilmemiştir."

    ##Her bir çalışan için toplam brut ucret hesaplanıyor. Tüm çalışanlarınkine ekleniyor.
    toplam_brut_ucret=brut_ucret+es_yardimi+cocuk_yardimi
    tum_toplam_brut_ucret+=toplam_brut_ucret
    ##


    ##Kaç lira üzerinden vergi kesintisi yapılacak?
    temp = toplam_brut_ucret - engelli_indirimi

    if (temp < 2000):
        kesinti=temp * 0.15
        say_1_vergi_dilimi+=1
    elif (temp < 5000):
        kesinti=temp * 0.2
        say_2_vergi_dilimi+=1
    elif (temp < 10000):
        kesinti=temp * 0.27
        say_3_vergi_dilimi+=1
    else:
        kesinti=temp* 0.35
        say_4_vergi_dilimi+=1

    ## Net ucret hesaplanıyor.
    net_ucret=toplam_brut_ucret-kesinti
    ## 2000 den az  net ucret alanların sayısı belirleniyor.
    if(net_ucret<2000):
        say_net_2000_alti+=1
    ## net ücreti en fazla olan  çalışan belirleniyor.
    if(net_ucret>max_net_ucret):
        net_winner_name=ad_soyad
        net_winner_kimlik_no=kimlik_no
        max_net_ucret=net_ucret
        net_winner_toplam_brut_ucret=toplam_brut_ucret
        net_winner_kesinti=kesinti
    #toplam brut ücreti en fazla olan çalışan belirleniyor.
    if (toplam_brut_ucret > max_toplam_brut_ucret):
        brut_winner_name = ad_soyad
        brut_winner_kimlik_no = kimlik_no
        max_toplam_brut_ucret = toplam_brut_ucret
        brut_winner_net_ucret = net_ucret
        brut_winner_kesinti = kesinti

    tum_gelir_kesintisi+=kesinti
    tum_net_ucret+=net_ucret
    ##Her bir çalışana ait bilgiler yazdırılıyor.
    print("Calisanın adi - soyadi ve TC kimlik nosu: ",ad_soyad," ,",kimlik_no)
    print("aylik brut ucreti :",format(brut_ucret,".2f"), " TL dir")
    print("Eş için aile yardım ödeneği",format(es_yardimi,".2f")," TL dir")
    print(" Cocuk icin aile yardım ödeneği",format(cocuk_yardimi,".2f")," TL dir")
    print("aylik toplam brut ucret:",format(toplam_brut_ucret,".2f")," TL dir")
    print("gelir vergisi kesintisi: ",format(kesinti,".2f")," TL dir")
    if(engelli_mi):
        print(engel_derecesi)

    # para türleri belirleniyor.
    print("Aylik net ucret:", format(net_ucret,".2f"),"TL dir")
    print("Odemede kulanılacak para turleri")

    para_int=int(net_ucret)
    para_kurus=int((net_ucret-para_int)*100)
    for banknot in [200,100,50,20,10,5,1]:
        banknot_say=para_int//banknot
        if banknot_say!=0:
            if(banknot==200):
                say_200_tl+=banknot_say
            elif(banknot==100) :
                say_100_tl+=banknot_say
            elif(banknot==50):
                say_50_tl+=banknot_say
            elif(banknot==20):
                say_20_tl+=banknot_say
            elif(banknot==10):
                say_10_tl+=banknot_say
            elif(banknot==5):
                say_5_tl+=banknot_say
            else:
                say_1_tl+=banknot_say


            print(banknot_say,"adet",banknot," TL ")
        para_int=para_int%banknot

    for bozukluk in [50,25,10,5,1]:
         kurus_say=para_kurus//bozukluk
         if (kurus_say!=0):
             if(bozukluk==50):
                 say_50_kurus+=kurus_say
             elif(bozukluk==25):
                 say_25_kurus+=kurus_say
             elif(bozukluk==10):
                 say_10_kurus+=kurus_say
             elif(bozukluk==5):
                 say_5_kurus+=kurus_say
             else:
                 say_1_kurus+=kurus_say
             print(kurus_say,"adet",bozukluk,"kuruş")
         para_kurus=para_kurus%bozukluk

    calisan_var=evet_hayir("Başka çalişan var mi")
## Tüm çalışanların bilgileri hesaplandı. Döngüden çıktık. şimdi genel istatistikler yazdırılıyor.
print("Tüm çalışanlara bir ayda ödenen aylık toplam net ücret tutarı:",format(tum_net_ucret,'.2f')
                                                                     , "TL \n ve devlete aktarılan aylık toplam gelir vergisi tutarı:", format(tum_gelir_kesintisi,".2f"),"TL  dir." )
print()
print()
print("Tüm çalışanların aylık toplam brüt ücretlerinin ve net ücretlerinin ortalaması:",format(tum_toplam_brut_ucret/say_calisan,'.2f')," TL \n ve " ,format(tum_net_ucret/say_calisan,".2f")," TL dir.")
print()
print()
print("Çalışanlara aylık net ücretlerinin en az sayıda \n banknot ve madeni para kullanılarak  ödenebilmesi için  toplamda ")
print(say_200_tl,"adet 200 TL")
print(say_100_tl, "adet 100 TL")
print(say_50_tl,"adet 50 TL")
print(say_10_tl," adet 10 TL")
print(say_5_tl,"adet 5 TL")
print(say_1_tl," adet 1 TL")
print(say_50_kurus,"adet 50 kurus")
print(say_25_kurus,"adet 25 kurus")
print(say_10_kurus,"adet 10 kurus")
print(say_5_kurus," adet 5 kurus")
print(say_1_kurus," adet 1 kurus")
print("GEREKLİDİR")
print()
print()
print("2000 tl nin altında net ucret alanların sayisi:", say_net_2000_alti )
print()
print()
print("%15  vergi odeyenleri sayisi",say_1_vergi_dilimi, " yuzdelik payi  %",format(100*say_1_vergi_dilimi/say_calisan,".2f"))
print("%20  vergi odeyenlerin sayisi",say_2_vergi_dilimi," yuzdelik payi %",format(100*say_2_vergi_dilimi/say_calisan,".2f"))
print("%27  vergi odeyenlerin sayisi",say_3_vergi_dilimi," yüzdelik payi %",format(100*say_3_vergi_dilimi/say_calisan,".2f"))
print("%35  vergi odeyenlerin  sayisi",say_4_vergi_dilimi," yuzdelik payi %",format(100*say_4_vergi_dilimi/say_calisan,".2f"))
print()
print()
print("aylık net ücreti en yüksek olan çalışanın TC kimlik numarası:",net_winner_kimlik_no,"\n  adı soyadı:",net_winner_name
,"\n aylık toplam brüt ücreti",format(net_winner_toplam_brut_ucret,".2f"),"  TL \n  gelir vergisi kesintisi ",format(net_winner_kesinti,".2f"),"TL \n ve aylık net ücreti  ",format(max_net_ucret,".2f"),"TL dir")

print()
print()
print("aylık toplam brut ücreti en yüksek olan çalışanın TC kimlik numarası:",brut_winner_kimlik_no,"\n  adı soyadı:",brut_winner_name
,"\n aylık toplam brüt ücreti",format(max_toplam_brut_ucret,".2f")
      ," TL  \n gelir vergisi kesintisi ",format(brut_winner_kesinti,".2f")," \n ve aylık net ücreti  ",format(brut_winner_net_ucret,".2f"),"TL dir")
print()
print("Tüm çalışanlar içinde evlilerin yüzdesi",format(100*say_evli/say_calisan,".2f"))
print()
print("Evli olanlar içinde eşleri çalışanlarin yüzdesi:", format(100*say_es_calisiyor/say_evli,".2f"))
print()
print("çalışanların bakmakla yükümlü oldukları çocuk sayısının ortalaması ",format(tum_cocuk_say/say_cocuklu_calisan,".2f"))
print()
print(" çocuk sayısı 3’ten fazla olan çalışanların sayısı",say_ucten_fazla_cocuklu)
print()
print(" Engelli çalışan sayisi ", say_engelli,"  ve  yuzdesi %",format(100*say_engelli/say_calisan,".2f"))









