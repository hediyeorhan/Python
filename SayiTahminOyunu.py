import random

rastgele = random.randint(1,100)
skor = 0
tahmin = 0
hak = 10

while(tahmin != rastgele):
    tahmin = int(input("Bir tahmin giriniz : "))
    if(tahmin < rastgele):
        print("Daha yüksek bir sayı söyleyin.")
        hak -= 1
        skor += 1

    elif(tahmin > rastgele):
        print("Daha düşük bir sayı söyleyin.")
        hak -= 1
        skor += 1

    else:

        skor +=1
        print("Tebrikler buldunuz ! Skor : {}".format(skor))

    if(hak == 0):
        print("Tahmin Hakkınız Bitti! Sayınız : {}".format(rastgele))
        break

