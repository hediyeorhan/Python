#Ödev2: Kullanıcıdan alınan iki sayının EBOB ve EKOK değerlerini bulan programı kodlayınız

a = int(input("Birinci sayıyı giriniz : "))
b = int(input("İkinci sayıyı giriniz : "))

i=2
ekok=1
m = a * b
while( a != b):
    if(a % i == 0 and b % i == 0):
        ekok *=i
        a //= i
        b //= i
    elif (a % i == 0 and b % i != 0):
        ekok *= i
        a //= i
    elif (a % i != 0 and b % i == 0):
        ekok *= i
        b //= i
    else:
        i += 1
    if (a == 1 and b == 1):
        break

ebob = m // ekok
print("Ekok : {}\nEbob : {}".format(ekok,ebob))






