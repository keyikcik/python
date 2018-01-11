full_ucret=0
ondan_fazla=0
besyuzden_az=0
max_ucret=0
tas_say=int(input("tasit sayisini giriniz"))
while(tas_say<0):
    tas_say = int(input("tasit sayisini giriniz"))


for idx in range(tas_say):

    ad_soyad = input("sürücünün  adı soyadı")
    tek_ucret = float(input("aldığı yakıt ücreti"))#just for first buy
    arac_ucret=0;##initilizations  for each car
    alim_say=0;

    while(tek_ucret>0):

        alim_say+=1
        arac_ucret+=tek_ucret
        tek_ucret = float(input("aldığı yakıt ücreti"))


    full_ucret+=arac_ucret
    if (alim_say>10):
        ondan_fazla+=1


    if(arac_ucret<500):
        besyuzden_az+=1

    if(max_ucret<arac_ucret):
        winner_name=ad_soyad
        max_ucret=arac_ucret

###printing

print(" ay sonunda odenen toplam yakıt ucreti %.2f TL dir"%(full_ucret))
print("taşıt başına düşen ortalama yakit ücreti %.2f Tl dir"%(full_ucret/tas_say))
print(" ")
print("yakıt alım sayısı ondan fazla olan araçların sayısı %d dir."%(ondan_fazla),sep=" ")
print("ve tüm araçlar içindeki oranı  %",format(ondan_fazla*100/tas_say,'.2f'))
print("")
print("yakıt ücreti 500 TL den  olan araçların sayısı %d dir."%(besyuzden_az),sep=" ")
print("ve tüm araçlar içindeki oranı %",format(besyuzden_az*100/tas_say,'.2f'))
print(" ")
print(" En cok yakıt ücreti odeyen kişi: ",winner_name," ",format(max_ucret,'.2f'), " TL   ödemiştir.")


