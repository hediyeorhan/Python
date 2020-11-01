sayi = int(input("Faktöriyeli alınacak sayıyı giriniz : "))
faktoriyel = 1

if(sayi  < 0):
    print("Negatif Sayıda İşlem Yapılamaz ! ")
    faktoriyel = "---"



for i  in range(1,sayi+1):
    faktoriyel *= i
print("{}! = {}".format(sayi,faktoriyel))