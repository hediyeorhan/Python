

# EKLEDİĞİM ÖZELLİK 1 --> Parolada alfanümerik olmayan karakter başta veya sonda olmasın ortada bulunsun sadece. - Parolada en az bir tane sayı bulunsun.
# EKLEDİĞİM ÖZELLİK 2 --> Parolada koyulmaması gereken karakterler belirledim. > < { } ^ ~ $ | bu karakterler parolada bulunmamalı.
print("""
1)Parolanız 8 ve 12 karakter arasında olmalıdır.
2)Parolanızda en az 1 tane büyük ve küçük harf bulunmalıdır.
3)Parolanızda en az 1 tane sayı bulunmalıdır.Sayı parolanın başında ve sonunda aynı anda bulunmasın.
4)Parolanızda boşluk karakteri bulunmamalıdır.
5)Parolanızda en az 1 tane alfanümerik karakter bulunmalıdır.Ama bu karakter parolanızın başında ve sonunda olmamalı.
6)Parolanızda > < { ^ ~ $ | karakterleri bulunmamalıdır.
7)Parolanızda bir karakteri sadece bir kez kullanabilirsiniz.Lütfen karakter tekrarı yapmayın.
""")



while(True):
    print("-----------------------------------")
    parola = input("Lütfen parolanızı giriniz : ")
    print("-----------------------------------")

    uzunluk = len(parola)
    BuyukHarf = 0
    KucukHarf = 0

    # UZUNLUK İÇİN
    UzunlukKontrol = None
    if (uzunluk < 8):
        print("Lütfen daha uzun bir parola giriniz !")
        UzunlukKontrol = 1
    elif (uzunluk > 12):
        print("Lütfen daha kısa bir parola giriniz !")
        UzunlukKontrol = 1

    # BÜYÜK KÜÇÜK HARF İÇİN
    for a in parola:
        if (a >= 'A') & (a <= 'Z'):
            BuyukHarf += 1
        elif (a >= 'a') & (a <= 'z'):
            KucukHarf += 1
    if (BuyukHarf == 0) | (KucukHarf == 0):
        print("Parolada hem büyük harf hem küçük harf bulunmak zorunda !")

    # SAYI İLE BAŞLAYIP SONLANMA KONTROLÜ İÇİN
    kontrol = None
    SayıKontrol = None
    BasHarf = None
    SonHarf = None

    for j in ("123456789"):
        for h in parola:
            if (h == j):
                SayıKontrol = 1
                if (parola[0] == j):
                    BasHarf = 1
                elif (parola[-1] == j):
                    SonHarf = 1

    if (BasHarf == 1) & (SonHarf == 1):
        kontrol = 1
        print("Başta ve sonda aynı anda sayı kullanamazsınız !")

    if (SayıKontrol == None):
        print("Lütfen parolanıza en az bir tane sayı ekleyin.")



    # BOŞLUK KONTROLÜ
    BoslukKontrol = None
    for b in parola:
        if (b == ' '):
            print("Parola boşluk karakteri içeremez.Lütfen parolanızdaki boşlukları silin.")
            BoslukKontrol = 1

    # ALFANÜMERİK KONTROL
    AlfaKontrol = None
    BasSonkontrol = None
    AlfaNumerikKarakterler = ("+-*/.,_?#%&=")
    IlkHarf = parola[0]
    SonHarf = parola[-1]
    for i in parola:
        if i in AlfaNumerikKarakterler:
            AlfaKontrol = 1
            for y in AlfaNumerikKarakterler:
                if (IlkHarf == y):
                    print("Parola alfanümerik olmayan karakter ile başlayamaz !")
                    BasSonkontrol = 1
                elif (SonHarf == y):
                    print("Parola alfanümerik olmayan karakter ile bitemez !")
                    BasSonkontrol = 1

    if (AlfaKontrol == None):
        print("Lütfen parolanıza en az bir tane alfanümerik olmayan karakter ekleyin.")

    # OLMAMASI GEREKEN KARAKTERLERİN KONTROLÜ
    KarakterKontrol = None
    YasakKarakterler = ('><^~{}$"|')

    for x in parola:
        if x in YasakKarakterler:
            KarakterKontrol = 1
    if (KarakterKontrol == 1):
        print("İstenmeyen karakter bulundu ! Lütfen istenmeyen karakter kullanmayın.")


    #TEKRAR EDEN KARAKTER KONTROLÜ
    TekrarKontrol = None
    for t in parola:
        if parola.count(t) != 1:
            TekrarKontrol = 1

    if (TekrarKontrol == 1):
        print("Tekrar eden karakter bulundu.Lütfen her karakteri bir defa kullanın.")

    #DÖNGÜDEN ÇIKIŞ ŞARTI
    if (UzunlukKontrol == None) & (KarakterKontrol == None) & (AlfaKontrol == 1) & (BoslukKontrol == None) & (
            SayıKontrol == 1) & (BasSonkontrol == None) & (kontrol == None) & (BuyukHarf != 0) & (KucukHarf != 0) & (TekrarKontrol == None):
        print("Parola işleminiz başarıyla tamamlandı.")
        break
