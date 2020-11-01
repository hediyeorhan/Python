"""

def mükemmel(sayı):
    toplam=0
    for i in range(1,sayı):

            if (sayı % i == 0):
                toplam += i
    return toplam == sayı



x = int(input("0 - x arası mükemmel sayılar için x değeri giriniz : "))
for i in range(1,x):
    if(mükemmel(i)):
        print("Mükemmel Sayı : ",i)

"""

# HÜSEYİN HOCANIN ÖRNEĞİ
import time

def mukemmel_bul(adet, altlimit = 0):
    sayac = 0
    if altlimit <= 0:
        altlimit = 1
    sayilar = list()

    def mukemmelmi(sayi):
        bolen_top = 0
        for i in range(1,sayi//2+1):
            if sayi % i == 0:
                bolen_top += i
        if bolen_top == sayi:
            return True
        else:
            return False
    while sayac < adet:
        if altlimit % 2 == 0:
            if mukemmelmi(altlimit):
                sayilar += [altlimit]
                sayac = sayac + 1
        altlimit += 1

    return sayilar

start = time.time()
sonuc = mukemmel_bul(2,10)
print(sonuc)
end = time.time()
print("\nTime : {:.2f}".format(end-start))
