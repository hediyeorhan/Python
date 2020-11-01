personel = dict()


def bilgial():
    per_say = int(input("Kaç adet personel bilgisi gireceksiniz ? "))
    id = 100
    global personel
    for i in range(1, per_say + 1):
        bilgi = dict()
        adsoyad = input("{}. Personel Ad-Soyad : ".format(i))
        bilgi["AdSoyad"] = adsoyad
        maas = int(input("{}. Personel Maaş : ".format(i)))
        bilgi["Maas"] = maas
        cs = int(input("{}. Personel Çocuk Sayısı : ".format(i)))
        bilgi["CS"] = cs
        ezam = int(input("{}. Personel Eski Zam : ".format(i)))
        bilgi["Ezam"] = ezam
        personel[id + i] = bilgi
        print("--------------------------------------")
    print(personel)
    print("--------------------------------------")


# PERSONEL LİSTELE
def listele():
    for per_id in personel.keys():
        print(" PER ID : {}\n".format(per_id), end=" ")
        for per_bilgi in personel[per_id].keys():
            print("{} : {}\n".format(per_bilgi, personel[per_id][per_bilgi]), end=" ")
        print()


# ESKİ ZAM ORANLARI BUL
def ZamHesapla(personel):
    for per_id in personel.keys():
        maas = personel[per_id]["Maas"]
        if maas < 2000:
            zam_oran = 0.20
        elif maas < 3000:
            zam_oran = 0.15
        else:
            zam_oran = 0.10
        yeni_zam = maas * zam_oran + personel[per_id]["CS"] * 70
        if yeni_zam < personel[per_id]["Ezam"]:
            yeni_zam = personel[per_id]["Ezam"]
        personel[per_id]["YeniZam"] = yeni_zam
        personel[per_id]["YeniMaas"] = maas + yeni_zam


# ARA
def ara(personel):
    ara_per_id = int(input("Aranacak Personel ID giriniz : "))
    bilgi = personel.get(ara_per_id, "Böyle bir personel bulunmamaktadır.")
    print(bilgi)

bilgial()
listele()
ZamHesapla(personel)
listele()