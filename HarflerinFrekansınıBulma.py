"""
Verilen bir string içindeki harflerin frekansını bulan ve frekansları başka bir string içinde string sırasına göre gösteren Python kodunu yazınız.

Örn : GALATASARAY --> 15151515151 (Tekrar eden harf saysını yazıyor yani bir nevi şifreleme gibi..)
Örn : DENE VE TEST ET --> 151531533513353
"""

Kelime = input("Lütfen kelime ya da cümle giriniz  :")

Frekans = ""
Sayac = 0

for i in range(len(Kelime)):
    Sayac = 0
    for j in Kelime:

        if Kelime[i] == j:
            Sayac += 1
    Frekans += str(Sayac)

print(Frekans)


