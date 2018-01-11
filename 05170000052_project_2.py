










def main():
    basla = 'e'
    while (basla == 'e'):
        oyun_oyna()
        basla = input("Yeni oyun oynamak istermisiniz? e/h")

def oyuncu_degistir(oyuncu, oyuncu1, oyuncu2):
    if oyuncu == oyuncu1:
        return oyuncu2
    else:
        return oyuncu1


def kenar_al(satir_say,sutun_list):
    # kullanıcıdan kenar seçmesini ister. Seçtiği karenin
    # satır, sutun bilgisini ve kenar D/B/K/G
    # bilgisini döndürür.
    print("sectigin karenin satiri?[1,", satir_say, "]" ,end=" ")
    sat_ind =int(input()) # istenen aralikta girilmesini sağla
    harf_sut_ind = (input(" sectigin karenin sutunu?"))
    yon_ind = (input("karenin hangi kenari "))
    while not (sat_ind in range(1, satir_say + 1) and harf_sut_ind in sutun_list[1:] and yon_ind in ['D', 'K', 'G',
                                                                                                     'B']):
        print("Koordinatlar hatalı girildi. Böyle bir kenar mevcut değil. Tekrar giriş yapınız. ")
        sat_ind = int(input("sectigin karenin satiri?"))  # istenen aralikta girilmesini sağla
        harf_sut_ind = (input(" sectigin karenin sutunu"))
        yon_ind = (input("karenin hangi kenari "))

    return (sat_ind, harf_sut_ind, yon_ind)


def kenar_ciz(sat_ind, say_sut_ind, yon_ind,yatay_kenar_mat,dikey_kenar_mat):

        # kullanıcının belirttiği karenin (sat_ind,sut_ind) çizilmesini istediği kenarini (yon_ind) ilgili matrislerde
        # boolean olarak tutar.Daha önceden seçilmiş bir karenin tekrar seçilmesini burada engelliyorum."


        if yon_ind == 'G':
            if yatay_kenar_mat[sat_ind][say_sut_ind - 1]:
                dolu= False
            else:
                yatay_kenar_mat[sat_ind][say_sut_ind - 1] = True
                dolu= True
        elif yon_ind == 'K':
            if yatay_kenar_mat[sat_ind - 1][say_sut_ind - 1]:
                dolu=False
            else:
                yatay_kenar_mat[sat_ind - 1][say_sut_ind - 1] = True
                dolu=True
        elif yon_ind == 'B':
            if dikey_kenar_mat[sat_ind][say_sut_ind - 1]:
                dolu=False
            else:
                dikey_kenar_mat[sat_ind][say_sut_ind - 1] = True
                dolu= True
        elif yon_ind == 'D':
            if dikey_kenar_mat[sat_ind][say_sut_ind]:
                dolu=False
            else:
                dikey_kenar_mat[sat_ind][say_sut_ind] = True
                dolu= True
        return dolu,yatay_kenar_mat,dikey_kenar_mat



def etrafi_tara(sat_ind, harf_sut_ind, yon_ind,sutun_list):
        # koordinatları verilen  kenarin ait olduğu karelerin  bilgisini   döndürür.
        komsu_kareler = [(sat_ind, harf_sut_ind)]
        temp_sutun=sutun_list.index(harf_sut_ind)
        if yon_ind == 'D':
            komsu_kareler.append((sat_ind, sutun_list[temp_sutun + 1]))
        elif yon_ind == 'B':
            komsu_kareler.append((sat_ind, sutun_list[temp_sutun- 1]))
        elif yon_ind == 'K':
            komsu_kareler.append((sat_ind - 1, harf_sut_ind))
        else:
            komsu_kareler.append((sat_ind + 1, harf_sut_ind))
        return komsu_kareler

def frame_ciz(satir_say,sutun_say,yatay_kenar_mat,dikey_kenar_mat,kare_kimin,sutun_list):
        #izgarayı çizer.
        for sutun_name in sutun_list:
            print(" " + sutun_name + "  ", end="")
        print()

        for satir in range(2 * satir_say + 1):
            for sutun in range(-1, sutun_say): # buraya da bir  tek çift dongusu iyi gider.
                if satir % 2 == 0:  # cift satirlar
                    if sutun == -1:  # ilk girinti
                        print("   ", end="")
                    else:  # yatay kenarlari ciz veya cizme

                        if yatay_kenar_mat[satir // 2][sutun]:
                            print(" ---", end="")  # en basa ve sona true koy.
                        else:
                            print("    ", end="")
                else:  # tek satirlar
                    if sutun == -1:  # satir no yu yazdir.
                        print("  ", end="")
                        print((satir + 1) // 2, end="")
                    else:  # dikey kenari ciz.

                        if dikey_kenar_mat[(satir + 1) // 2][sutun]:
                            str = " " + kare_kimin[(satir + 1) // 2, sutun_list[sutun + 1]] + " "
                            print("|" + str, end="")
                        else:
                            print("    ", end="")  # secilince ciz
                        if sutun == sutun_say - 1:
                            print("|", end="")
            print()



def oyun_oyna():
    #tek bir el oyun oynatir.
    harf_list = list(" ABCDEFGIJKLMNOPQRST")
    oyuncu1 = input(" Birinci oyuncuyu temsil etmek için bir karakter giriniz: ")
    oyuncu2 = input(" İkinci oyuncuyu temsil etmek için bir karakter giriniz: ")
    satir_say = int(input("oyun alaninin satir sayisini giriniz: [3-7]  "))
    sutun_say = int(input("oyun alaninin sütün sayisini giriniz: [3-19]  "))
    while not (3<=satir_say<=7 and 3<=sutun_say<=19):
        print(" HATA......istenen aralıkta değerleri giriniz.")
        satir_say = int(input("oyun alaninin satir sayisini giriniz: [3-7]  "))
        sutun_say = int(input("oyun alaninin sütün sayisini giriniz: [3-19]  "))
    sutun_list = harf_list[:sutun_say + 1]
    # veri yapılari

    yatay_kenar_mat = [False] * (satir_say + 1)# izgaradaki yatay çizgilerin bilgisini boolen olarak tutar.
    for i in range(satir_say + 1):
        yatay_kenar_mat[i] = [False] * (sutun_say+1 )

    for j in range(sutun_say+1 ):
        yatay_kenar_mat[0][j] = True
        yatay_kenar_mat[satir_say][j] = True

    dikey_kenar_mat = [False] * (satir_say +1) # izgaradaki dikey çizgilerin bilgisini boolen olarak tutar.
    for i in range(satir_say+1 ):
        dikey_kenar_mat[i] = [False] * (sutun_say + 1)

    for j in range(satir_say+1 ):
        dikey_kenar_mat[j][0] = True
        dikey_kenar_mat[j][sutun_say] = True
    kare_kimin = dict()  # kare koordinatlarını key olarak kabul der. Value is o kareyi tamamlayan kişidir.
                            # Value " "  ise kare henüz tamamlanmamıştır.
    for sat_ind in range(1, satir_say + 1):
        for sut_ind in sutun_list[1:sutun_say + 1]:
            kare_kimin[(sat_ind, sut_ind)] = " "

    frame_ciz(satir_say, sutun_say, yatay_kenar_mat, dikey_kenar_mat, kare_kimin, sutun_list)
    devam = True
    oyuncu = oyuncu1
    while (devam):
        print(oyuncu, " oynuyor.")

        (sat_ind, harf_sut_ind, yon_ind) = kenar_al(satir_say,sutun_list)

        say_sut_ind = sutun_list.index(harf_sut_ind)
        flag, yatay_kenar_mat, dikey_kenar_mat = kenar_ciz(sat_ind, say_sut_ind, yon_ind,yatay_kenar_mat,dikey_kenar_mat)
        while (not flag): #seçilmemiş bir kenarın seçilmesini sağlar.
            print("bu kenar zaten işaretli tekrar kenar girisi yapiniz.")
            (sat_ind, harf_sut_ind, yon_ind) = kenar_al(satir_say,sutun_list)
            say_sut_ind = sutun_list.index(harf_sut_ind) # sutun index in sayısal karşılığu
            flag, yatay_kenar_mat, dikey_kenar_mat = kenar_ciz(sat_ind, say_sut_ind, yon_ind,yatay_kenar_mat,dikey_kenar_mat)

        komsu_kareler = etrafi_tara(sat_ind, harf_sut_ind, yon_ind, sutun_list)

        dolu_komsu_say = 0
        for komsu in komsu_kareler:
            say_komsu_sutun = sutun_list.index(komsu[1])
            dolu_mu = yatay_kenar_mat[komsu[0]][say_komsu_sutun - 1] and yatay_kenar_mat[komsu[0] - 1][
                say_komsu_sutun - 1] and \
                      dikey_kenar_mat[komsu[0]][say_komsu_sutun - 1] and dikey_kenar_mat[komsu[0]][say_komsu_sutun]
            if dolu_mu:
                kare_kimin[komsu] = oyuncu
                dolu_komsu_say += 1
        frame_ciz(satir_say, sutun_say, yatay_kenar_mat, dikey_kenar_mat, kare_kimin, sutun_list)
        if dolu_komsu_say == 0:
            oyuncu = oyuncu_degistir(oyuncu, oyuncu1, oyuncu2)

        devam = " " in kare_kimin.values()

    print("oyun bitti")
    oyuncu1_puan = list(kare_kimin.values()).count(oyuncu1)
    oyuncu2_puan = satir_say * sutun_say - oyuncu1_puan
    print(oyuncu1, " in puanı ", oyuncu1_puan)
    print(oyuncu2, " in puanı ", oyuncu2_puan)
    if oyuncu1_puan == oyuncu2_puan:
        print("Berabere")
    elif oyuncu1_puan > oyuncu2_puan:
        print("Kazanan ", oyuncu1)
    else:
        print("Kazanan ", oyuncu2)

main()