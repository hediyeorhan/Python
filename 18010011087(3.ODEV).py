# 18010011087
# HEDİYE ORHAN
"""
KODU TAMAMEN ÇALIŞTIRDIĞIMIZDA SATIŞ YAP FONKSİYONUNDA, SATIŞ BİLGİLERİ VE MÜŞTERİ BİLGİLERİ TUTULAN 2 ADET DOSYA DAHA OLUŞTURULUYOR.
PROJEMDE 3 TANE TXT DOSYASI KULLANDIM. GÖNDERDİĞİM TXT DOSYASI İSE ÜRÜNLER BİLGİSİ TUTAN TXT DOSYASI.
YANİ YENİ ÜRÜN KAYIT FONKSİYONUNDA EKLEDİĞİMİZ ÜRÜNLERİ TUTAN DOSYA.
"""

import random

# DOSYADAKİ STRİNGLERİ VE KULLANICININ GİRDİĞİ STRİNGLERİ KARŞILAŞTIRMAK İÇİN TÜRKÇE KARAKTERLERİ DE KÜÇÜK HARF YAPAN FONKSİYONU YAZDIM.
# BÖYLECE AŞAĞIDAKİ FONKSİYONLARDA TÜM KELİMELERİ KÜÇÜK HARF YAPIP O ŞEKİLDE KARŞILAŞTIRMA YAPILIYOR.
def trlower(metin):
    metin2 = " "
    for harf in metin:
        if harf == 'I':
            sonuc = 'ı'
        elif harf == 'İ':
            sonuc = 'i'
        else:
            sonuc = harf.lower()
        metin2 += sonuc

    return metin2

# BURADA MÜŞTERİ BİLGİLERİ VE SATIŞ YAPILAN ÜRÜN BİLGİLERİ ALINIYOR. SATIŞ VE MÜŞTERİLER DOSYASINA VERİLER KAYDEDİLİYOR.
def SatisYap():
    Musteriler = dict()

    while True:
        try:
            satissayisi = int(input("Kaç adet satış yapacaksınız : "))
            break
        except ValueError:
            print("Lütfen integer bir değer giriniz !!")

    print("\n")

    for i in range(1, satissayisi + 1):
        bilgi = dict()
        # SATIŞ BİLGİLERİ İÇİ AYRI MÜŞTERİ BİLGİLERİ İÇİN AYRI DOSYA AÇTIM.
        dosya = open("18010011087(2).txt", "a", encoding="utf-8")
        dosya2 = open("18010011087(3).txt", "a", encoding="utf-8")

        MusteriAdSoyad = input("{}. Müşterinin adı ve soyadını giriniz : ".format(i))
        bilgi["AD SOYAD"] = MusteriAdSoyad.title()
        dosya.write("MÜŞTERİ AD-SOYAD : " + MusteriAdSoyad.title() + " -- ")
        dosya2.write("MÜŞTERİ AD-SOYAD : " + MusteriAdSoyad.title() + " -- ")

        MusteriNumara = input("{}. Müşterinin telefon numarasını giriniz : ".format(i))
        bilgi["TELEFON NUMARASI"] = MusteriNumara
        dosya2.write("MÜŞTERİ TELEFON NUMARASI : " + MusteriNumara + " -- ")
        uruntur = input("Ürünün türünü giriniz.(Örneğin : Pantolon,Gömlek..) : ")
        bilgi["ÜRÜN TÜRÜ"] = uruntur.title()
        dosya.write("ÜRÜN TÜR : " + uruntur.title() + " -- ")

        urunrenk = input("Ürünün rengini giriniz : ")
        bilgi["ÜRÜN RENK"] = urunrenk.title()
        dosya.write("ÜRÜN RENK : " + urunrenk.title() + " -- ")

        urunbeden = input("Ürünün bedenini giriniz.(Örneğin : S,M,XL,L.. ya da 36,38..) : ")
        bilgi["ÜRÜN BEDEN"] = urunbeden
        dosya.write("ÜRÜN BEDEN: " + urunbeden + " -- ")

        urunmarka = input("Ürünün markasını giriniz : ")
        bilgi["ÜRÜN MARKA"] = urunmarka.title()
        dosya.write("ÜRÜN MARKA : " + urunmarka.title() + " -- ")
        while True:
            try:
                urunfiyat = float(input("Ürünün fiyatını giriniz : "))
                break
            except ValueError:
                print("Lütfen integer ya da float bir değer giriniz !!")

        bilgi["ÜRÜN FİYAT"] = urunfiyat
        dosya.write("ÜRÜN FİYAT : " + str(urunfiyat) + " -- ")

        # MÜŞTERİNİN ALDIĞI ÜRÜNÜN FİYATINA GÖRE İNDİRİM UYGULAMALARI VARSA ONLARI UYGULAMASI İÇİN ÜRÜNÜN FİYATINI BU FONKSİYONA GÖNDERİYORUZ.
        # BURADA ÖDENECEK FİYATI HEMEN HESAPLAYIP BİZE GERİ DÖNDÜRMESİ İÇİN İÇ İÇE FONKSİYON KULLANDIM.
        def fiyathesapla(urunfiyat):
            sonfiyat = 0

            while True:
                try:
                    indirim = input("Ürünlerin etiketlerinde indirim var mı ?(E : EVET / H : HAYIR) : ")
                    if indirim == 'H' or indirim == 'h':
                        sonfiyat = urunfiyat
                        break
                    elif indirim == 'E' or indirim == 'e':
                        while True:
                            try:
                                indirim_orani = float(input("Üründeki indirim oranını yazınız.(Örneğin 0.5 ya da 0.20 şeklinde) : "))
                                sonfiyat = urunfiyat - (urunfiyat * indirim_orani)
                                break
                            except ValueError:
                                print("Lütfen float bir değer giriniz !!")
                        break
                    else:
                        raise BaseException("Lütfen H/h ya da E/e giriniz !!")
                except BaseException:
                    print("Lütfen H/h ya da E/e giriniz !!")


            while True:
                try:
                    odemesekli = input("Ödeme şekli giriniz.(KART : K / TAKSİT : T / NAKİT : N) : ")
                    if odemesekli == 'K' or odemesekli == 'k':
                        sonfiyat += (sonfiyat * 0.03)
                        break

                    elif odemesekli == 'T' or odemesekli == 't':
                        # YAPILAN TAKSİT MİKTARINA GÖRE HER AY İÇİN 10 TL ÖDENECEK ŞEKİLDE AYARLADIM.
                        while True:
                            try:
                                adet = int(input("Kaç aylık taksit yaptırmak istiyorsunuz ? (2 - 12 arası yapılabilir.) : "))
                                sonfiyat += (adet * 5)
                                break
                            except ValueError:
                                print("Lütfen integer bir değer giriniz !!")
                        break


                    elif odemesekli == 'N' or odemesekli == 'n':
                        sonfiyat = sonfiyat
                        break
                    else:
                        raise BaseException("Lütfen K/k, N/n ya da T/t giriniz !!")
                except BaseException:
                    print("Lütfen K/k, N/n ya da T/t giriniz !!")


            # 300 TL VE ÜZERİ ÜRÜNLERDE 15 TL İNDİRİM.
            if urunfiyat >= 300:
                sonfiyat -= 15
            while True:
                try:
                    kart = input("Müşterinin mağaza kartı var mı ? (E : EVET / H : HAYIR) : ")
                    # MÜŞTERİMİZDE MAĞAZAMIZIN ÖZEL KARTINDAN BULUNUYORSA VE BELLİ BİR PUAN ÜZERİNDE TOPLADIYSA İNDİRİM UYGULANIYOR.
                    # HER ALIŞVERİŞTE MAĞAZA KART PUANI ARTAR VE MÜŞTERİ PUAN TOPLAR.
                    if kart == 'E' or kart == 'e':
                        while True:
                            try:
                                magaza_kart = int(input("Müşterinin toplam mağaza kart puanını giriniz : "))
                                magaza_kart += 10
                                if magaza_kart >= 100:
                                    indirim_fiyat = (magaza_kart // 300) * 5
                                    sonfiyat = sonfiyat - indirim_fiyat
                                    break

                            except ValueError:
                                print("Lütfen integer bir sayı giriniz !!")
                        break


                    elif kart == 'H' or kart == 'h':
                        magaza_kart = 0
                        sonfiyat = sonfiyat
                        break
                    else:
                        raise BaseException("Lütfen E/e ya da H/h giriniz !!")
                except BaseException:
                    print("Lütfen E/e ya da H/h giriniz !!")



            return sonfiyat, magaza_kart

        toplamfiyat, magaza_kart = fiyathesapla(urunfiyat)
        bilgi["MAĞAZA KART PUANI"] = magaza_kart
        dosya2.write("MAĞAZA KART PUANI : " + str(magaza_kart) + "\n")

        bilgi["ÖDENEN FİYAT"] = toplamfiyat
        dosya.write("ÖDENEN FİYAT : " + str(toplamfiyat) + "\n")

        Musteriler[i] = bilgi
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    dosya.close()
    dosya2.close()
    print("\nYENİ SATIŞLAR\n")
    print(Musteriler)

# DEPOYA YENİ GELEN ÜRÜNLERİ EKLEME FONKSİYONU
def YeniUrunKayit():
    YeniUrun = dict()
    while True:
        try:
            urunsayisi = int(input("Kaç adet yeni ürün bilgisi gireceksiniz ? "))
            break
        except ValueError:
            print("Lütfen integer bir değer giriniz !!")

    print("\n")

    for i in range(1,urunsayisi+1):

        bilgi = dict()
        # DEPODAKİ ÜRÜN BİLGİLERİNİ TUTMASI İÇİN ÜRÜNLER.TXT DOSYASI OLUŞTURDUM.
        dosya = open("18010011087.txt", "a", encoding="utf-8")

        # DEPOYA EKLEDİĞİMİZ ÜRÜNLERE RASTGELE KOD ATAMASI YAPIYOR BÖYLECE DİĞER FONKSİYONLARDA BU KOD İLE ÜRÜNLERE ERİŞECEĞİZ.
        kod = random.randint(10000,99999)
        bilgi["ÜRÜN KODU"] = kod
        dosya.write("ÜRÜN KODU : " + str(kod) + " -- ")

        tur = input("{}. Ürünün türünü giriniz.(Örneğin : Pantolon,Gömlek..) : ".format(i))
        bilgi["Tür"] = tur.title()
        dosya.write("TÜR : " + tur.title() + " -- ")

        renk = input("{}. Ürünün rengini giriniz : ".format(i))
        bilgi["Renk"] = renk.title()
        dosya.write("RENK : " + renk.title() + " -- ")

        beden = input("{}. Ürünün bedenini giriniz.(Örneğin : S,M,XL,L.. ya da 36,38..) : ".format(i))
        bilgi["Beden"] = beden
        dosya.write("BEDEN : " + beden + " -- ")

        marka = input("{}. Ürünün markasını giriniz : ".format(i))
        bilgi["MARKA"] = marka.title()
        dosya.write("MARKA : " + marka.title() + " -- ")

        while True:
            try:
                fiyat = float(input("{}. Ürünün fiyatını giriniz : ".format(i)))
                break
            except ValueError:
                print("Lütfen integer ya da float bir değer giriniz !!")

        bilgi["Fiyat"] = fiyat
        dosya.write("FİYAT : " + str(fiyat) + "\n")

        YeniUrun[i] = bilgi
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    dosya.close()
    print("\nÜRÜNLER EKLENDİ\n")
    print(YeniUrun)

# DEPODAKİ ÜRÜNLER İÇİNDEN ARAMA YAPMA FONKSİYONU
def UrunArama(urun):
    dosya = open("18010011087.txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()
    # TXT DOSYASINI OKUMA MODUNDA AÇTIM VE READLİNES() İLE HER SATIRI TEK TEK OKUDUM.
    # OKUNAN SATIRLAR BİR LİSTEDE TUTULUYOR.
    for i in satir:    # HER SATIRI TEK TEK DOLANARAK İÇİNDE ÜRÜN KODUMUZ BULUNAN SATIRI YAZDIRDIM.
        if trlower(urun) in trlower(i):
            print("\nÜRÜN BULUNDU\n")
            print(i)





# İSTEDİĞİMİZ MÜŞTERİNİN BİLGİLERİNİ ARAMA FONKSİYONU
def MusteriArama(musteriad):
    dosya = open("18010011087(3).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()

    for i in satir:
        if trlower(musteriad) in trlower(i):
            #  HER SATIRI TEK TEK DOLANARAK İÇİNDE MÜŞTERİMİZİN ADI BULUNAN SATIRI YAZDIRDIM.
            print("\nMÜŞTERİ BİLGİLERİ\n")
            print(i)

# YAPILAN SATIŞLAR İÇİNDEN ARAMA YAPMAMIZI SAĞLAYAN FONKSİYON.
def SatisBilgisiArama(musteriad,uruntur):
    dosya = open("18010011087(2).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()
    for i in satir:
        if trlower(musteriad) in trlower(i):
            if trlower(uruntur) in trlower(i):
                print("\nSATIŞ BİLGİSİ BULUNDU\n")
                print(i)

# DEPOYA EKLEDİĞİMİZ ÜRÜNLERDEN İSTEDİĞİMİZİ SİLME FONKSİYONU
def UrunSilme(kod):
    dosya = open("18010011087.txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()

    dosya = open("18010011087.txt", "w", encoding="utf-8")
    # SİLME İŞLEMİ DOSYADA DEĞİŞİKLİK YAPACAĞI İÇİN DOSYAYI YAZMA MODUNDA AÇTIM.

    for i in satir:

        if trlower(kod) in trlower(i):
            #  HER SATIRI TEK TEK DOLANARAK İÇİNDE ÜRÜN KODUMUZ BULUNAN SATIRIN İNDEKSİNİ ALDIM VE O SATIRI SİLDİM.
            indeks = satir.index(i)
            del satir[indeks]
            print("\nÜRÜN BAŞARIYLA SİLİNDİ.\n")

        else:
            pass
    dosya.writelines(satir)  # KALAN SATIRLARI TEKRAR DOSYAMIZA YAZDIRDIM.
    dosya.close()
    print("\n-- KALAN ÜRÜNLER --\n")
    for i in satir:
        print(i)


# YAPTIĞIMIZ SATIŞLARIN BİLGİLERİNDEN İSTEDİĞİMİZİ SİLME FONKSİYONU
def SatisBilgisiSilme(musteriad):
    dosya = open("18010011087(2).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()


    dosya = open("18010011087(2).txt", "w", encoding="utf-8")
    # SİLME İŞLEMİ DOSYADA DEĞİŞİKLİK YAPACAĞI İÇİN DOSYAYI YAZMA MODUNDA AÇTIM.

    for i in satir:

        if trlower(musteriad) in trlower(i):
            # HER SATIRI TEK TEK DOLANARAK İÇİNDE MÜŞTERİMİZİN ADI BULUNAN SATIRIN İNDEKSİNİ ALDIM VE O SATIRI SİLDİM.
            indeks = satir.index(i)
            del satir[indeks]
            print("\nKAYIT BAŞARIYLA SİLİNDİ.\n")

        else:
            pass
    dosya.writelines(satir)  # KALAN SATIRLARI TEKRAR DOSYAMIZA YAZDIRDIM.
    dosya.close()
    print("\n-- KAYITLI SATIŞ BİLGİLERİ --\n")
    for i in satir:
        print(i)




# İSTEDİĞİMİZ MÜŞTERİNİN KAYDINI SİLME FONKSİYONU
def MusteriKayitSilme(isim):
    dosya = open("18010011087(3).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()

    dosya = open("18010011087(3).txt", "w", encoding="utf-8")
    # SİLME İŞLEMİ DOSYADA DEĞİŞİKLİK YAPACAĞI İÇİN DOSYAYI YAZMA MODUNDA AÇTIM.

    for i in satir:

        if trlower(isim) in trlower(i):
            # HER SATIRI TEK TEK DOLANARAK İÇİNDE MÜŞTERİMİZİN ADI BULUNAN SATIRIN İNDEKSİNİ ALDIM VE O SATIRI SİLDİM.
            indeks = satir.index(i)
            del satir[indeks]
            print("\nMÜŞTERİ BAŞARIYLA SİLİNDİ.\n")

        else:
            pass
    dosya.writelines(satir)   # KALAN SATIRLARI TEKRAR DOSYAMIZA YAZDIRDIM.
    dosya.close()
    print("\n-- KAYITLI MÜŞTERİ BİLGİLERİ --\n")
    for i in satir:
        print(i)

# ÜRÜNLER.TXT DOSYASINDAKİ BİLGİLERİ BU FONKSİYON İLE ALDIM (HER SATIRDAKİ BİLGİLERİ TEK TEK ALDIM).
# BU FONKSİYONDAN DÖNEN DEĞERLERİ DİĞER FONKSİYONLARDA KULLANMAK İÇİN BU FONKSİYONU YAZDIM.
def UrunBilgisi(kod):
    with open("18010011087.txt", "r", encoding="utf-8") as dosya:
        for bilgi in dosya:
            bilgi = bilgi[:-1]
            bilgiler = bilgi.split(" -- ")    # BİLGİLER ARASINDA '--' İŞARETİ OLDUĞU İÇİN '--' İŞARETİNDEN AYIRARAK İNDEKSLEME YAPTIM.
            if kod in bilgiler[0]:
                tur = bilgiler[1]
                renk = bilgiler[2]
                beden = bilgiler[3]
                marka = bilgiler[4]
                fiyat = bilgiler[5]

    return tur,renk,beden,marka,fiyat


# DEPODAKİ ÜRÜNLERİN İSTEDİĞİMİZ ÖZELLİKLERİNİ GÜNCELLEME FONKSİYONU

def UrunGuncelleme(kod):

    dosya = open("18010011087.txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()

    for i in satir:

        if trlower(kod) in trlower(i):
            tur, renk, beden, marka, fiyat = UrunBilgisi(kod)  # YUKARIDA YAZDIĞIM FONKSİYON İLE ÜRÜNLER.TXT(18010011087.txt) DOSYASI İÇİNDEKİ DEĞERLERİ ALDIM.
            indeks = satir.index(i)
            print("\n", i, "\n")
            dosya = open("18010011087.txt", "w", encoding="utf-8")
            # GÜNCELLEME İŞLEMİ DOSYADA DEĞİŞİKLİK YAPACAĞI İÇİN DOSYAYI YAZMA MODUNDA AÇTIM.
            while True:
                try:
                    secim = input("1 : Tür / 2 : Renk / 3 : Beden / 4 : Marka / 5 : Fiyat\nLütfen güncellemek istediğiniz özelliği seçiniz : ")

                    # SEÇİLEN ÖZELLİĞE GÖRE ÜRÜNÜ GÜNCELLEYİP TEKRAR DOSYAYA YAZDIRDIM.
                    if secim == "1":
                        tur2 = input("Tür giriniz : ")
                        tur = tur2
                        eklenecekler = "ÜRÜN KODU : " + kod + " -- TÜR : " + tur.title() + " -- " + renk.title() + " -- " + beden + " -- " + marka.title() + " -- " + str(
                            fiyat) + "\n"
                        break

                    elif secim == "2":
                        renk2 = input("Renk giriniz : ")
                        renk = renk2
                        eklenecekler = "ÜRÜN KODU : " + kod + " -- " + tur.title() + " -- RENK : " + renk.title() + " -- " + beden + " -- " + marka.title() + " -- " + str(
                            fiyat) + "\n"
                        break

                    elif secim == "3":
                        beden2 = input("Beden giriniz : ")
                        beden = beden2
                        eklenecekler = "ÜRÜN KODU : " + kod + " -- " + tur.title() + " -- " + renk.title() + " -- BEDEN : " + beden + " -- " + marka.title() + " -- " + str(
                            fiyat) + "\n"
                        break

                    elif secim == "4":
                        marka2 = input("Marka giriniz : ")
                        marka = marka2
                        eklenecekler = "ÜRÜN KODU : " + kod + " -- " + tur.title() + " -- " + renk.title() + " -- " + beden + " -- MARKA : " + marka.title() + " -- " + str(
                            fiyat) + "\n"
                        break

                    elif secim == "5":
                        while True:
                            try:
                                fiyat2 = float(input("Fiyat giriniz : "))
                                break
                            except ValueError:
                                print("Lütfen integer ya da float değer giriniz !!")
                        fiyat = fiyat2
                        eklenecekler = "ÜRÜN KODU : " + kod + " -- " + tur.title() + " -- " + renk.title() + " -- " + beden + " -- " + marka.title() + " -- FİYAT : " + str(fiyat) + "\n"
                        break
                    else:
                        raise BaseException("Lütfen 1-2-3-4-5 seçeneklerinden seçiniz !!")
                except BaseException:
                    print("Lütfen 1-2-3-4-5 seçeneklerinden seçiniz !!")


            del satir[indeks]
            # HER KOŞULA GÖRE AYRI STRİNGLER OLUŞTURDUM VE EN SONDA BU STRİNGİ DOSYAYA EKLEDİM.
            eklenecekler = str(eklenecekler)
            satir.insert(indeks, eklenecekler)
            dosya.writelines(satir)
            dosya.close()
            print("\nGÜNCELLEME BAŞARILIYLA TAMAMLANDI.\n")
            break

        else:
            pass

    print("\n-- GÜNCEL ÜRÜNLER --\n")
    for i in satir:
        print(i)

# SATİSVEMUSTERİLER.TXT DOSYASINDAKİ BİLGİLERİ BU FONKSİYON İLE ALDIM (HER SATIRDAKİ BİLGİLERİ TEK TEK ALDIM).
# BU FONKSİYONDAN DÖNEN DEĞERLERİ DİĞER FONKSİYONLARDA KULLANMAK İÇİN BU FONKSİYONU YAZDIM.
def BilgiCekme(musteriad):
    with open("18010011087(2).txt", "r", encoding="utf-8") as dosya:
        for bilgi in dosya:
            bilgi = bilgi[:-1]
            bilgiler = bilgi.split(" -- ")    # BİLGİLER ARASINDA '--' İŞARETİ OLDUĞU İÇİN '--' İŞARETİNDEN AYIRARAK İNDEKSLEME YAPTIM.
            if trlower(musteriad) in trlower(bilgiler[0]):
                ad = bilgiler[0]
                tur = bilgiler[1]
                renk = bilgiler[2]
                beden = bilgiler[3]
                marka = bilgiler[4]
                fiyat = bilgiler[5]
                odenen = bilgiler[6]

    return ad, tur, marka, fiyat, odenen, renk, beden


# MUSTERİLER.TXT DOSYASINDAKİ BİLGİLERİ BU FONKSİYON İLE ALDIM (HER SATIRDAKİ BİLGİLERİ TEK TEK ALDIM).
# BU FONKSİYONDAN DÖNEN DEĞERLERİ DİĞER FONKSİYONLARDA KULLANMAK İÇİN BU FONKSİYONU YAZDIM.
def MusteriBilgi(ad):
    with open("18010011087(3).txt", "r", encoding="utf-8") as dosya:
        for bilgi in dosya:
            bilgi = bilgi[:-1]
            bilgiler = bilgi.split(" -- ")   # BİLGİLER ARASINDA '--' İŞARETİ OLDUĞU İÇİN '--' İŞARETİNDEN AYIRARAK İNDEKSLEME YAPTIM.
            if trlower(ad) in trlower(bilgiler[0]):
                ad = bilgiler[0]
                numara = bilgiler[1]
                kart = bilgiler[2]

    return ad, numara, kart

# MÜŞTERİ BİLGİSİ GÜNCELLEME FONKSİYONU
def MusteriBilgisiGuncelleme(guncelad):
    dosya = open("18010011087(3).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()


    for i in satir:

        if trlower(guncelad) in trlower(i):
            ad, numara, kart = MusteriBilgi(guncelad)  # YUKARIDA YAZDIĞIM FONKSİYON İLE MUSTERİLER.TXT(18010011087(3).txt) DOSYASINDAKİ BİLGİLERİ ALDIM.
            indeks = satir.index(i)
            print("\n", i, "\n")
            dosya = open("18010011087(3).txt", "w", encoding="utf-8")
            # GÜNCELLEME İŞLEMİ DOSYADA DEĞİŞİKLİK YAPTIĞI İÇİN YAZMA MODUNDA AÇTIM.
            while True:
                try:
                    secim = input( "1 : Ad Soyad / 2 : Telefon Numarası / 3: Mağaza Kart Puanı\nLütfen güncellemek istediğiniz durumu seçiniz : ")
                    # YAPILAN SEÇİME GÖRE MÜŞTERİ BİLGİSİNİ GÜNCELLEDİ VE DOSYAYA YAZDI.
                    if secim == "1":
                        ad2 = input("Müşteri adı ve soyadı giriniz : ")
                        ad = ad2
                        eklenecekler = "MÜŞTERİ AD-SOYAD : " + ad.title() + " -- " + numara + " -- " + kart + "\n"
                        break
                    elif secim == "2":
                        numara2 = input("Müşteri telefon numarası giriniz : ")
                        numara = numara2
                        eklenecekler = ad.title() + " -- MÜŞTERİ TELEFON NUMARASI : " + numara + " -- " + kart + "\n"
                        break
                    elif secim == "3":
                        while True:
                            try:
                                kart2 = int(input("Müşterinin mağaza kart puanını giriniz : "))
                                break
                            except ValueError:
                                print("Lütfen integer bir değer giriniz !!")

                        kart = kart2
                        eklenecekler = ad.title() + " -- " + numara + " -- MAĞAZA KART PUANI : " + str(kart) + "\n"
                        break
                    else:
                        raise BaseException("Lütfen 1-2-3 seçeneklerinden seçiniz !!")
                except BaseException:
                    print("Lütfen 1-2-3 seçeneklerinden birini seçiniz !!")


            del satir[indeks]
            # HER KOŞULA GÖRE AYRI STRİNGLER OLUŞTURDUM VE EN SONDA BU STRİNGİ DOSYAYA EKLEDİM.
            eklenecekler = str(eklenecekler)
            satir.insert(indeks, eklenecekler)
            dosya.writelines(satir)
            dosya.close()
            print("\nGÜNCELLEME BAŞARILIYLA TAMAMLANDI.\n")
            break

        else:
            pass

    print("\n-- GÜNCEL MÜŞTERİ BİLGİLERİ --\n")
    for i in satir:
        print(i)


# YAPTIĞIMIZ SATIŞLARDA İSTEYEN MÜŞTERİLERİMİZİN ÜRÜN DEĞİŞİMİNİ YAPAN FONKSİYON
def UrunDegisim(musteri,urun):
    dosya = open("18010011087(2).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()

    # TXT DOSYASINI OKUMA MODUNDA AÇTIM VE READLİNES() İLE HER SATIRI TEK TEK OKUDUM.
    # OKUNAN SATIRLAR BİR LİSTEDE TUTULUYOR.

    for i in satir:

        if trlower(musteri) in trlower(i):
            if trlower(urun) in trlower(i):
                ad, tur, marka, fiyat, odeme, mevcutrenk, mevcutbeden = BilgiCekme(musteri)
                # YUKARIDA YAZDIĞIM FONKSİYON İLE SATIŞ BİLGİLERİNİ ALDIM.
                indeks = satir.index(i)
                print("\n", i, "\n")
                print("\nSadece beden ve renk değişimi yapabilirsiniz.\n")
                dosya = open("18010011087(2).txt", "w", encoding="utf-8")
                while True:
                    try:

                        secim = input("Renk değişimi : R / Beden değişimi : B\n Seçim : ")

                        # DEĞİŞİM YAPAN MÜŞTERİNİN SATIŞ BİLGİSİNDE DEĞİŞİM YAPILDIĞI NOT OLARAK GÖRÜNÜYOR.
                        # SEÇİME GÖRE MÜŞTERİNİN 2 ÖZELLİKTEN BİRİNİ DEĞİŞTİRME HAKKI VAR.
                        # DOSYA BUNA GÖRE YENİDEN YAZILIYOR.

                        if secim == "R" or secim == "r":
                            renk = input("Renk giriniz : ")
                            beden = mevcutbeden
                            eklenecekler = ad.title() + " -- " + tur.title() + " (DEĞİŞİM YAPILDI) -- ÜRÜN RENK : " + renk.title() + " -- " + beden + " -- " + marka + " -- " + fiyat + " -- " + odeme + "\n"
                            break
                        elif secim == "B" or secim == "b":
                            beden = input("Beden giriniz : ")
                            renk = mevcutrenk
                            eklenecekler = ad.title() + " -- " + tur.title() + " (DEĞİŞİM YAPILDI) -- " + renk.title() + " -- ÜRÜN BEDEN : " + beden + " -- " + marka + " -- " + fiyat + " -- " + odeme + "\n"
                            break
                        else:
                            raise BaseException("Lütfen R/r ya da B/b giriniz !!")
                    except BaseException:
                        print("Lütfen R/r ya da B/b giriniz !!")
                # HER KOŞULA GÖRE AYRI STRİNGLER OLUŞTURDUM VE EN SONDA BU STRİNGİ DOSYAYA EKLEDİM.
                del satir[indeks]
                eklenecekler = str(eklenecekler)
                satir.insert(indeks, eklenecekler)
                dosya.writelines(satir)
                dosya.close()
                print("\nDEĞİŞİM YAPILDI.\n")
                break
            else:
                pass
        else:
            pass


    print("\n-- GÜNCEL SATIŞLAR DURUMU --\n")
    for i in satir:
        print(i)

# YAPTIĞIMIZ SATIŞLARDA İSTEYEN MÜŞTERİLERİMİZİN ÜRÜN İADESİNİ YAPAN FONKSİYON
def UrunIade(musteri,urun):
    dosya = open("18010011087(2).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()

    for i in satir:

        if trlower(musteri) in trlower(i):
            if trlower(urun) in trlower(i):
                ad, tur, marka, fiyat, odeme, renk, beden = BilgiCekme(musteri)
                # YUKARIDA YAZDIĞIM FONKSİYON İLE SATIŞ BİLGİLERİNİ ALDIM.
                indeks = satir.index(i)
                print("\n", i, "\n")
                dosya = open("18010011087(2).txt", "w", encoding="utf-8")

                # İADE YAPAN MÜŞTERİNİN SATIŞ BİLGİSİNDE İADE EDİLDİĞİ NOT OLARAK GÖRÜNÜYOR.
                # DOSYA BUNA GÖRE YENİDEN YAZILIYOR.

                del satir[indeks]
                eklenecekler = ad.title() + " -- ÜRÜN TÜR : "+  urun.title() + " (ÜRÜN MÜŞTERİ TARAFINDAN İADE EDİLDİ) -- " + renk + " -- " + beden + " -- " + marka + " -- " + fiyat + " -- " + odeme + "\n"
                eklenecekler = str(eklenecekler)
                satir.insert(indeks, eklenecekler)
                dosya.writelines(satir)
                dosya.close()
                print("\nİADE İŞLEMİ YAPILDI.\n")
                break
            else:
                pass
        else:
            pass


    print("\n-- GÜNCEL SATIŞ DURUMU --\n")
    for i in satir:
        print(i)


# BELİRLİ BİR FİYAT VE ÜZERİNDE KAÇ ALIŞVERİŞ YAPILDIĞINI KULLANICIYA SÖYLEYEN FONKSİYON
def FiyataGoreListeleme(arananfiyat):

    with open("18010011087(2).txt", "r", encoding="utf-8") as dosya:
        sayac = 0
        for fiyat in dosya:
            fiyat = fiyat[:-1]
            # DOSYADAKİ SATIRLARI "ÖDENEN FİYAT : " STRİNGİNE GÖRE AYIRDIM VE SON İNDİSE FİYAT KISMI KALDI.
            fiyatlar = fiyat.split("ÖDENEN FİYAT : ")

            aranan = fiyatlar[-1]
            aranan = float(aranan)  # STRİNGİ FLOATA ÇEVİRDİM VE KOŞULU SAĞLAYIP SAĞLAMADIĞINA BAKTIM.

            if aranan >= arananfiyat :
                sayac += 1
                print(fiyatlar[0] +"ÖDENEN FİYAT : " +fiyatlar[1])
            else:
               pass
    print("\n{} tane {} TL ve üzeri satış yapılmıştır.".format(sayac,arananfiyat))




# EN ÇOK ALIŞVERİŞ YAPAN MÜŞTERİLERİ LİSTELEYEN FONKSİYON
def EnCokAlisverisYapanMusteriler():
    with open("18010011087(3).txt", "r", encoding="utf-8") as dosya:
        print("\nEN ÇOK ALIŞVERİŞ YAPAN MÜŞTERİLER\n")
        print("\nMağaza kart puanı 300 ve üzeri olan daimi müşterilerimiz : \n")
        for fiyat in dosya:
            fiyat = fiyat[:-1]
            # DOSYADAKİ SATIRLARI "MAĞAZA KART PUANI : " STRİNGİNE GÖRE AYIRDIM VE SON İNDİSE KART PUANI KISMI KALDI.
            fiyatlar = fiyat.split("MAĞAZA KART PUANI : ")

            aranan = fiyatlar[-1]
            aranan = int(aranan)

            if aranan >= 300:  # MAĞAZA KART PUANI 300 ÜZERİNDE OLAN MÜŞTERİLERİ LİSTELE BU MÜŞTERİLER EN ÇOK ALIŞVERİŞ YAPANLAR GRUBUNA GİRİYOR.
                print(fiyat)
            else:
               pass


# DEPODAKİ ÜRÜNLERİ LİSTELEYEN FONKSİYON
def UrunListele():
    dosya = open("18010011087.txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()
    print("\nDEPODAKİ ÜRÜNLER\n")
    for i in satir:
        print(i)

# SİSTEMDE KAYITLI MÜŞTERİLERİMİZİN TAMAMINI KULLANICIYA LİSTELEYEN FONKSİYON
def MusteriListele():
    dosya = open("18010011087(3).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()
    print("\nKAYITLI MÜŞTERİ BİLGİLERİ\n")
    for i in satir:
        print(i)

# YAPILAN BÜTÜN SATIŞLARIN BİLGİSİNİ KULLANICIYA LİSTELEYEN FONKSİYON
def SatisBilgisiListele():
    dosya = open("18010011087(2).txt", "r", encoding="utf-8")
    satir = dosya.readlines()
    dosya.close()
    print("\nYAPILAN BÜTÜN SATIŞLARIN BİLGİLERİ\n")
    for i in satir:
        print(i)


def menu():
    print("\n---- MAĞAZA OTOMASYONUNA HOŞGELDİNİZ ----")
    print("\nNOT : GÖNDERDİĞİM DOSYA ÜRÜN BİLGİLERİNİ TUTTUĞU İÇİN ÜRÜN ARAMA, ÜRÜN GÜNCELLEME, ÜRÜN LİSTELEME, ÜRÜN SİLME İŞLEMLERİNİ DİREKT ÇALIŞTIRABİLİRSİNİZ.\nDİĞER İŞLEMLERİ YAPMAK İÇİN ÖNCELİKLE SATIŞ YAP İŞLEMİNİ YAPMANIZ GEREKLİ ÇÜNKÜ MÜŞTERİ BİLGİLERİ VE SATIŞ BİLGİLERİ DOSYALARI O FONKSİYONDA OLUŞUYOR.\nBENİM GÖNDERDİĞİM SADECE ÜRÜN BİLGİLERİNİ İÇEREN TXT DOSYASI.PROJEMDE 3 TANE DOSYA KULLANDIM.\n")
    while True:
        # MENÜDE BAZI İŞLEMLER 2 VEYA 3 DOSYA ÜZERİNDE DE GERÇEKLEŞEBİLECEĞİ İÇİN ALT KISIMLARA AYIRDIM.
        print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        menu = input(
            "1) SATIŞ YAP\n2) YENİ ÜRÜN EKLE\n3) ARAMA İŞLEMLERİ\n\t-Ürün Arama\n\t-Müşteri Arama\n\t-Satış Bilgisi Arama\n4) SİLME İŞLEMLERİ\n\t-Ürün Silme\n\t-Satış Bilgisi Silme\n\t-Müşteri Kaydı Silme\n5) ÜRÜN DEĞİŞİMİ\n6) ÜRÜN İADE\n7) GÜNCELLEME İŞLEMLERİ\n\t-Ürün Güncelleme\n\t-Müşteri Kayıt Bilgisi Güncelleme\n8) LİSTELEME İŞLEMLERİ\n\t-Depodaki Ürünleri Listele\n\t-Kayıtlı Müşteri Bilgilerini Listele\n\t-Mevcut Satış Bilgilerini Listele\n\t-En Çok ALışveriş Yapan Müşterileri Listele\n9) ... TL ve Üzeri Yapılan Satışlar\n10) Çıkış\nLütfen menü seçiniz : ")
        print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        if menu == "1":
            SatisYap()
        elif menu == "2":
            YeniUrunKayit()
        elif menu == "3":
            while True:
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                secim = input("1) Ürün Arama\n2) Müşteri Arama\n3) Satış Bilgisi Arama\n4) Ana Menü\nLütfen menü seçiniz : ")
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                if secim == "1":
                    urun = input("Aramak istediğiniz ürünün kodunu giriniz.(Kodu bilmiyorsanız ürünün türünü giriniz.) : ")
                    UrunArama(urun)
                elif secim == "2":
                    musteriad = input("Aramak  istediğiniz müşterinin adını ve soyadını giriniz : ")
                    MusteriArama(musteriad)
                elif secim == "3":
                    musteriad = input("Satış bilgisini aradığınız müşterinin adını giriniz : ")
                    uruntur = input("Müşterinin aldığı ürünün türünü giriniz : ")
                    SatisBilgisiArama(musteriad, uruntur)
                elif secim == "4":
                    break
                else:
                    print("Geçersiz menü seçimi!")

        elif menu == "4":
            while True:
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                secim = input(
                    "1) Ürün Silme\n2) Satış Bilgisi Silme\n3) Müşteri Kaydı Silme\n4) Ana Menü\nLütfen menü seçiniz : ")
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                # SİLME İŞLEMİNDEN ÖNCE BİLGİLERİ EKRANA YAZDIRDIM KULLANICININ GÖRMESİ İÇİN.
                if secim == "1":
                    dosya = open("18010011087.txt", "r", encoding="utf-8")
                    satir = dosya.readlines()
                    for i in satir:
                        print(i)
                    dosya.close()
                    kod = input("Silmek  istediğiniz ürünün kodunu giriniz : ")
                    UrunSilme(kod)

                elif secim == "2":
                    dosya = open("18010011087(2).txt", "r", encoding="utf-8")
                    satir = dosya.readlines()
                    for i in satir:
                        print(i)
                    dosya.close()
                    ad = input("Satış bilgilerini silmek istediğiniz müşterinin adını ve soyadınız giriniz : ")
                    SatisBilgisiSilme(ad)
                elif secim == "3":
                    dosya = open("18010011087(3).txt", "r", encoding="utf-8")
                    satir = dosya.readlines()
                    for i in satir:
                        print(i)
                    dosya.close()
                    isim = input("Sistemden kaydını silmek istediğiniz müşterinin adını ve soyadını giriniz : ")
                    MusteriKayitSilme(isim)
                elif secim == "4":
                    break
                else:
                    print("Geçersiz menü seçimi!")

        elif menu == "5":
            musteri = input("Değişim işlemi yapacak müşterinin adını ve soyadını giriniz : ")
            urun = input("Değişimi yapılacak ürünün türünü giriniz : ")
            UrunDegisim(musteri, urun)
        elif menu == "6":
            musteri = input("İade işlemi yapacak müşterinin adını ve soyadını giriniz : ")
            urun = input("İadesi yapılacak ürünün türünü giriniz : ")
            UrunIade(musteri, urun)

        elif menu == "7":
            while True:
                # GÜNCELLEME İŞLEMİNDEN ÖNCE BİLGİLERİ EKRANA YAZDIRDIM KULLANICININ GÖRMESİ İÇİN.
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                secim = input(
                    "1) Ürün Güncelleme\n2) Müşteri Kayıt Bilgisi Güncelleme\n3) Ana Menü\nLütfen menü seçiniz : ")
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                if secim == "1":
                    dosya = open("18010011087.txt", "r", encoding="utf-8")
                    satir = dosya.readlines()
                    for i in satir:
                        print(i)
                    dosya.close()

                    kod = input("Güncellemek istediğiniz ürünün kodunu giriniz : ")
                    UrunGuncelleme(kod)

                elif secim == "2":
                    dosya = open("18010011087(3).txt", "r", encoding="utf-8")
                    satir = dosya.readlines()
                    for i in satir:
                        print(i)
                    dosya.close()

                    guncelad = input("Güncellemek istediğiniz müşterinin adını ve soyadını giriniz : ")
                    MusteriBilgisiGuncelleme(guncelad)
                elif secim == "3":
                    break

                else:
                    print("Geçersiz menü seçimi!")
        elif menu == "8":
            while True:
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                secim = input(
                    "1) Depodaki Ürünleri Listele\n2) Kayıtlı Müşteri Bilgilerini Listele\n3) Mevcut Satış Bilgilerini Listele\n4) En Çok Alışveriş Yapan Müşterileri Listele\n5) Ana Menü\nLütfen menü seçiniz : ")
                print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                if secim == "1":
                    UrunListele()
                elif secim == "2":
                    MusteriListele()
                elif secim == "3":
                    SatisBilgisiListele()
                elif secim == "4":
                    EnCokAlisverisYapanMusteriler()
                elif secim == "5":
                    break
                else:
                    print("Geçersiz menü seçimi!")
        elif menu == "9":
            while True:
                try:
                    aranacakfiyat = float(input("Aramak istediğiniz fiyatı giriniz : "))
                    break
                except ValueError:
                    print("Lütfen float ya da integer değer giriniz !!")
            FiyataGoreListeleme(aranacakfiyat)

        elif menu == "10":
            print("ÇIKIŞ YAPILIYOR..")
            exit()
        else:
            print("Geçersiz menü seçimi!")

menu()

