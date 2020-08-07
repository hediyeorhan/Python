# GİRİLEN MİKTARI TÜRK LİRASI BANKNOTLARINA AYIRARAK EKRANA YAZDIRAN FONKSİYON.
def TR(amountT):
    # TR
    amount1 = amountT
    amount2 = amountT
    amount3 = amountT
    # 50'LİK, 100'LÜK, 200'LÜK BANKNOTLAR
    YunusEmre = amount1 // 200
    amount1 = amount1 - (YunusEmre * 200)
    MustafaItri = amount1 // 100
    amount1 = amount1 - (MustafaItri * 100)
    FatmaAliye = amount1 // 50
    amount1 = amount1 - (FatmaAliye * 50)
    AhmedKemaleddin = amount1 // 20
    amount1 = amount1 - (AhmedKemaleddin * 20)
    AzizSancar1 = amount1 // 1

    print("-In TR\n{} Yunus Emre , {} Mustafa Itri , {} Fatma Aliye Hanım , {} Ahmed Kemalleddin and {} Aziz Sancar".format(YunusEmre, MustafaItri, FatmaAliye, AhmedKemaleddin, AzizSancar1))
    # 50'LİK, 100'LÜK BANKNOTLAR
    MustafaItri2 = amount2 // 100
    amount2 = amount2 - (MustafaItri2 * 100)
    FatmaAliye2 = amount2 // 50
    amount2 = amount2 - (FatmaAliye2 * 50)
    AzizSancar2 = amount2 // 1
    print("{} Mustafa Itri, {} Fatma Aliye and {} Aziz Sancar".format(MustafaItri2, FatmaAliye2, AzizSancar2))
    # 5'LİK, 10'LUK BANKNOTLAR
    CahitArf = amount3 // 10
    amount3 = amount3 - (CahitArf * 10)
    AydinSayili = amount3 // 5
    amount3 = amount3 - (AydinSayili * 5)
    AzizSancar3 = amount3 // 1
    print("{} Cahit Arf, {} Aydın Sayılı and {} Aziz Sancar".format(CahitArf, AydinSayili, AzizSancar3))

# GİRİLEN MİKTARI FRANSIZ FRANGI BANKNOTLARINA AYIRARAK EKRANA YAZDIRAN FONKSİYON.
def EUR(amountE):
    # EUR
    amount1 = amountE
    amount2 = amountE
    amount3 = amountE
    # 20'LİK, 500'LÜK, 200'LÜK BANKNOTLAR
    Modern = amount1 // 500
    amount1 = amount1 - (Modern * 500)
    IronAndPine = amount1 // 200
    amount1 = amount1 - (IronAndPine * 200)
    Gothic = amount1 // 20
    amount1 = amount1 - (Gothic * 20)
    Portre = amount1 // 1
    print("\n-In EURO\n{} Modern, {} Iron ,{} Gothic and  Pine and {}Portre".format(Modern, IronAndPine, Gothic, Portre))
    # 100'LÜK, 50'LİK BANKNOTLAR
    BarokAndRococo = amount2 // 100
    amount2 = amount2 - (BarokAndRococo * 100)
    Renaissance = amount2 // 50
    amount2 = amount2 - (Renaissance * 50)
    Portre2 = amount2 // 1
    print("{} Barok and Rococo, {} Renaissance and {} Portre".format(BarokAndRococo, Renaissance, Portre2))
    # 10'LUK, 5'LİK BANKNOTLAR
    Romanesque = amount3 // 10
    amount3 = amount3 - (Romanesque * 10)
    Classic = amount3 // 5
    amount3 = amount3 - (Classic * 5)
    Portre3 = amount3 // 1
    print("{} Romanesque, {} Classic and {} Portre".format(Romanesque, Classic, Portre3))

# GİRİLEN MİKTARI ALMAN BANKNOTLARINA AYIRARAK EKRANA YAZDIRAN FONKSİYON.
def USD(amountD):
    # USD
    amount1 = amountD
    amount2 = amountD
    amount3 = amountD
    # 50'LİK, 100'LÜK BANKNOTLAR
    BenjaminFranklin = amount1 // 100
    amount1 = amount1 - (BenjaminFranklin * 100)
    HarrietTubman = amount1 // 20
    amount1 = amount1 - (HarrietTubman * 20)
    GeorgeWashington1 = amount1 // 1

    print("\n-In USD\n{} Benjamin Franklin, {} Harriet Tubman and {} George Washington".format(BenjaminFranklin, HarrietTubman, GeorgeWashington1))
    # 50'LİK, 10'LUK BANKNOTLAR
    UlyssesGrant = amount2 // 50
    amount2 = amount2 - (UlyssesGrant * 50)
    AlexanderHamilton = amount2 // 10
    amount2 = amount2 - (AlexanderHamilton * 10)
    GeorgeWashington2 = amount2 // 1
    print("{} Ulysses Grant, {} Alexander Hamilton and {} George Washington".format(UlyssesGrant, AlexanderHamilton, GeorgeWashington2))
    # 5'LİK, 2'LİK VE 1'LİK BANKNOTLAR
    AbrahamLincoln = amount3 // 5
    amount3 = amount3 - (AbrahamLincoln * 5)
    ThomasJefferson = amount3 // 2
    amount3 = amount3 - (ThomasJefferson * 2)
    GeorgeWashington3 = amount3 // 1
    print("{} Abraham Lincoln, {} Thomas Jefferson and {} George Washington".format(AbrahamLincoln, ThomasJefferson, GeorgeWashington3))

# GİRİLEN MİKTARIN PARA BİRİMİNE GÖRE DÖNÜŞÜM YAPAN VE EKRANA YAZDIRAN FONKSİYON
def calculation(currency, amount):
    # EĞER TÜRK LİRASI GİRİLDİYSE TÜRK LİRASINI EURO VE USD'YE ÇEVİRİYORUZ.
    if currency == 'TR':
        amountT = amount
        amountE = amount / 7.73
        amountD = amount / 6.84
    # EĞER EUR GİRİLDİYSE EURO'YU TL VE USD'YE ÇEVİRİYORUZ.
    elif currency == 'EUR':
        amountE = amount
        amountT = amount / (1/7.73)
        amountD = amount * 1.1302
    # EĞER USD GİRİLDİYSE EUR VE TL'YE ÇEVİRİYORUZ.
    elif currency == 'USD':
        amountD = amount
        amountT = amount / (1/6.84)
        amountE = amount * (1/1.1302)

    else:
        print("Invalid")

    print("\nYour Anahtar result of {} {} is\n ".format(amount, currency.upper()))
    # GİRİLEN PARA MİKTARI DÖNÜŞÜMÜ PARA BİRİMLERİNE GÖRE YAPILDIKTAN SONRA BANKNOTLARA BÖLÜNEREK EKRANA YAZDIRILMASI İÇİN TR, USD, EUR FONKSİYONLARINA GÖNDERİYORUZ.
    TR(amountT)
    EUR(amountE)
    USD(amountD)

# BELİRLEDİĞİMİZ OBJELERİN FİYATLARININ BANKNOTLAR HALİNDE EKRANA YAZDIRILMASINI SAĞLAYAN FONKSİYON.
def calculation2 (amount, object):

    print("\nThe value of a {} is {}\n ".format(object.upper(), amount))
    print("Your Anahtar result of a {} is \n".format(object))
    TR(amount)
    EUR(amount)
    USD(amount)


while True:

    option = input("\n1 for Currency\n2 for Goods\nPlease select your option: ")
    # FİYATLARINI BELİRDEĞİMİZ 5 ADET OBJEMİZ
    car = 35000
    window = 1000
    flower = 90
    computer = 650
    pencil = 980
    if option == '1':
        while True:
            try:
                # GİRİLEN PARA BİRİMİ TR, EUR VEYA USD DEĞİLSE KULLANICIDAN TEKRAR PARA BİRİMİ İSTENİYOR.
                currency = input("Please enter currency: ")
                if currency.upper() == "TR":
                    currency = currency.upper()
                    break
                elif currency.upper() == "EUR":
                    currency = currency.upper()
                    break
                elif currency.upper() == "USD":
                    currency = currency.upper()
                    break
                else:
                    raise BaseException("Please enter TR, EUR or USD !")

            except BaseException:
                print("Please enter TR, EUR or USD !")
        while True:
            try:
                amount = int(input("Please enter the amount: "))
                break
            except ValueError:
                print("Please enter an integer value !")

        calculation(currency.upper(), amount)
        break
    elif option == '2':
        while True:
            # EĞER KULLANICI BİZİM BELİRDİĞİMİZ OBJE İSİMLERİNDEN GİRMEDİYSE, KULLANICIDAN TEKRAR OBJE İSMİ GİRMESİ İSTENİR.
            try:
                object = input("Please Enter Object: ")
                object.lower()
                amount = 0
                if object == 'car':
                    amount = car
                    break
                elif object == 'window':
                    amount = window
                    break
                elif object == 'flower':
                    amount = flower
                    break
                elif object == 'computer':
                    amount = computer
                    break
                elif object == 'pencil':
                    amount = pencil
                    break
                else:
                    raise BaseException("Please enter the objects we have determined!")
            except BaseException:
                print("Please enter the objects we have determined!")
        calculation2(amount, object)
        break


    else:
        print("Please choose 1 or 2 !!")
