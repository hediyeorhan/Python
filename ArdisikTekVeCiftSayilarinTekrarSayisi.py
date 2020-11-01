""" 1-100 arasında, üretilen sayı 50-55 arasında olana kadar random sayılar üretiniz.
Bu üretilen sayılar arasında ardışık olarak en çok tekrar eden çift sayı adetini ve en çok tekrar eden tek sayı adetini bulup, ekrana yazdırınız.
Dizi ve liste kullanmayınız."""

import random

CiftSayac = 0
TekSayac = 0
MaxCiftSayac = 0
MaxTekSayac = 0

while True:
    number = random.randint(1, 100)
    print(number, end = "\t")
    if number % 2 == 0:
        CiftSayac += 1
        if CiftSayac > MaxCiftSayac:
            MaxCiftSayac = CiftSayac
        TekSayac = 0
    else:
        TekSayac += 1
        if TekSayac > MaxTekSayac:
            MaxTekSayac = TekSayac
        CiftSayac = 0
    if 50 <= number <= 55:
        break
print("\nArdışık olarak en çok tekrar eden çift sayı adedi : {}\nArdışık olarak en çok tekrar eden tek sayı adedi : {}".format(MaxCiftSayac,MaxTekSayac))
