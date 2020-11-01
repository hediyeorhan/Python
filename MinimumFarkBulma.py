sayi = int(input("Sayı giriniz : "))
fark = 0
MinFark = 100000000000000000000000000000000
temp = sayi

if(sayi < 0):
    print("Negatif Sayı Girdiniz ! ")
    MinFark = "--------"

while(sayi >= 0):
    sayi = int(input("Sayı giriniz : "))
    if(sayi < 0 ):
        print("Negatif Sayı !")
        break
    fark = temp - sayi
    if(fark < 0):
        fark *= (-1)
    if(fark < MinFark):
        MinFark = fark
    print("FARK --> {} - {} : {}".format(temp,sayi,fark))
    temp = sayi
print("Minimum Fark : {}".format(MinFark))


