kelime = input("Kelime giriniz : ")
sesli = " "
sessiz = " "
for i in kelime:
    if(i == 'a') | (i == 'e')  | (i == 'i') | (i == 'ı') | (i == 'o') | (i == 'ö') | (i == 'u') | (i == 'ü'):
        sesli += i
    else:
        sessiz += i
print("Sesli Harfler : {}".format(sesli))
print("Sessiz Harfler : {}".format(sessiz))
