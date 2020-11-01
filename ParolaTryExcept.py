tr_karakter = "şçğüöıİ"
parola = input("Parolanız : ")
try:
    for  i in parola:
        if i in tr_karakter:
            raise TypeError("Parolada Türkçe karakter kullanılamaz!")
except TypeError:
    print("Parolada Türkçe karakter kullanılamaz!")
else:
    print("Parola kabul edildi!")