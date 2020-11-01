import random

fark = 0
MinFark = 1000000000000000000000000

sayi1 = 0
sayi2 = 0
temp = 0

#sayi = random.randint(1, 100)
#print("{}".format(sayi))


#temp = sayi




while(True):

    sayi = random.randint(1, 100)
    print(sayi, end = "\t")

    fark = temp - sayi

    if(fark < 0):
        fark *= (-1)
    if(fark < MinFark):
        MinFark = fark
        sayi1 = temp
        sayi2 = sayi
    #print("FARK --> {} - {} : {}".format(temp,sayi,fark))

    temp = sayi

    if (sayi >= 70) & (sayi <= 75):
        break



print("\nMinimum Fark : {} - Sayılar : {} , {}".format(MinFark,sayi1,sayi2))