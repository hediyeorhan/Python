"""
Bir şirket personel maaş zamlarının hesaplanmasını istemektedir.

Şirket maaş zammı hesaplaması esnasında mevcut maaş, çocuk sayısı ve önceki
zam miktarını dikkate almaktadır.

Zam oranı;
–
Maaşı 3000’den küçük olanlar için %20,
–
3000 ve 4000 arasında olanlar için %15,
–
4000’ den büyük olanlar için %10
belirlenmektedir.
•
Ayrıca şirket, personele her bir çocuk için 70 TL ekstra zam vermektedir.
•
Şirket, personele yapılan yeni zam miktarı eski zam miktarından daha az olması
durumda eski maaş zammını dikkate almaktadır.
•
Bilgileri verilen personel için maaş zam miktarını ve yeni maaşını hesaplayan
Python kodunu yazınız.
"""

maas = int(input("Mevcut maaşınızı giriniz : "))
cocuk_sayi = int(input("Kaç çocuğunuz var ? "))
eski_zam = int(input("Eski zam miktarınızı giriniz : "))

if(maas < 3000):
    zam_oran = 20/100
elif(maas > 3000) & (maas < 4000):
    zam_oran = 15/100
else:
    zam_oran = 10/100

yeni_zam = (maas * zam_oran) + (cocuk_sayi * 70)


if(eski_zam > yeni_zam):
    maas += eski_zam
else:
    maas += yeni_zam

print("Güncel maaşınız : {} ".format(maas))
