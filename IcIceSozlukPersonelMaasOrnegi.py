personel = dict()
per_say = int(input("Kaç adet personel bilgisi gireceksiniz ? "))
id = 100

for i in range(1,per_say+1):
    bilgi = dict()
    adsoyad = input("{}. Personel Ad-Soyad : ".format(i))
    bilgi["AdSoyad"] = adsoyad
    maas = int(input("{}. Personel Maaş : ".format(i)))
    bilgi["Maaş"] = maas
    cs = int(input("{}. Personel Çocuk Sayısı : ".format(i)))
    bilgi["CS"] = cs
    ezam = int(input("{}. Personel Eski Zam : ".format(i)))
    bilgi["Ezam"] = ezam
    personel[id+i] = bilgi
    print("--------------------------------------")
print(personel)
print("--------------------------------------")

# PERSONEL LİSTELE
for per_id in personel.keys():
    print(" PER ID : {}\n".format(per_id),end = " ")
    for per_bilgi in personel[per_id].keys():
        print("{} : {}\n".format(per_bilgi,personel[per_id][per_bilgi]),end = " ")
    print()

# ESKİ ZAM ORANLARI BUL

for per_id in personel.keys():
    assert personel[per_id]["Maaş"] >= 0, "Maaş negatif bir değer olamaz"
    ezam_oran = personel[per_id]["Ezam"] / personel[per_id]["Maaş"]
    print("Per_ID : {} , Per_EzamOran : {:.2f}".format(per_id,ezam_oran))

# ARA
ara_per_id = int(input("Aranacak Personel ID giriniz : "))
bilgi = personel.get(ara_per_id,"Böyle bir personel bulunmamaktadır.")
print(bilgi)