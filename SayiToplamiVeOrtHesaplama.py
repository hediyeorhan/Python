adet = int(input("Kaç adet sayi gireceksiniz ? "))
toplam = 0
ort = 0

for i in range(adet):
    sayi = int(input("{} . sayıyı giriniz : ".format(i+1)))
    toplam += sayi
ort = toplam / adet
print("Sayıların toplamı : {} , Sayıların ortalaması : {}".format(toplam,ort))
