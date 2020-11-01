"""
Ödev1: Kullanıcıdan alınan bir sayının asal bölenlerini tespit edip bu sayıları ve adetini ekrana yazdırınız.
Ödev2: Kullanıcıdan alınan iki sayının EBOB ve EKOK değerlerini bulan programı kodlayınız

"""
sayac = 0
adet = int(input("Sayi giriniz : "))

for sayi in range(2, adet):

    i = 2

    kontrol = 0

    while (i < sayi):

        if (sayi % i == 0):
            kontrol += 1
        i += 1


    if (kontrol == 0):
        if(adet % sayi == 0):
            print(sayi)
            sayac += 1

print("{} sayısının {} tane asal böleni vardır.".format(adet,sayac))



