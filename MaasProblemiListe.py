"""
(Nested List) --> iç içe
Bir şirkette çalışanların çocuk sayısına göre maaşlarına zam yapılacaktır. Bu şirkette çalışanların adını , çocuk sayısını ve maaşını kullanıcıdan alarak listede tutunuz.
Çocuk sayısı :
1 = 50 Tl
2 = 75 Tl
Daha fazla = Çocuk başına 80 TL zam yapılacaktır.
Tüm çalışanların bilgilerini ve güncel maaşlarını ekrana yazdıran Python kodunu yazınız.

"""
calisanlar = []

sayac = int(input("Kaç adet çalışan bilgisi gireceksiniz ? "))

for i in range(sayac):
    calisanlar.append(list()) # iç içe liste yapısı yaptık..
    ad = input("{}.Çalışan ad : ".format(i+1))
    calisanlar[i].append(ad)
    cs = int(input("Çocuk sayısı : "))
    calisanlar[i].append(cs)
    maas = int(input("{}.Çalışanın maaşı : ".format(i+1)))
    calisanlar[i].append(maas)

for i in range(sayac):
    if calisanlar[i][1] == 1:
        calisanlar[i][2] += 50
    elif calisanlar[i][1] == 2:
        calisanlar[i][2] += 75
    elif calisanlar[i][2] > 2:
        calisanlar[i][2] += (calisanlar[i][1] * 80)
    else:
        pass

print("-------------------------------------------------\nGüncel Çalışan Bilgileri\n-------------------------------------------------")
for i in range(sayac):
    print("{}.Çalışan adı : {} - Çocuk Sayısı : {} - Yeni Maaşı : {}".format(i+1,calisanlar[i][0],calisanlar[i][1],calisanlar[i][2]))
