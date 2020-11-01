#Kullanıcının girdiği parola içinde bulunan Türkçe karakterler i tespit
#ederek ekranda gösteren Python kodunu yazınız.

parola = input("Parola giriniz :")

for i in parola:
    if(i == 'ı') | (i == 'ö') | (i == 'İ') | (i == 'ç') | (i == 'ğ') | (i == 'ş'):
        print("Türkçe karakter tespit edildi ! : {} ".format(i))

