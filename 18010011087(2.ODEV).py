
# HEDİYE ORHAN
# 18010011087

import random

print("\n**Amiral Battı Oyununa Hoşgeldiniz**\n")

while True:
    secim = int(input("1) Yeni Oyun\n2) Çıkış\n----------------------\nLütfen bir seçim yapınız :"))
    if secim == 1:

        m = int(input("Kaçlık bir kare matris oluşturmak istiyorsunuz ? (Lütfen sadece bir değer giriniz!) : "))

        # BURADA AÇIK MOD VE GİZLİ MOD İÇİN 2 TANE MATRİS OLUŞTURDUM.
        acikalan = []
        for i in range(m):
            acikalan.append([])

        for z in range(m):
            for j in acikalan:
                j.append([])

        for i in range(m):
            for j in range(m):
                acikalan[i][j] = "?"

        gizlialan = []
        for i in range(m):
            gizlialan.append([])

        for z in range(m):
            for j in gizlialan:
                j.append([])

        for i in range(m):
            for j in range(m):
                gizlialan[i][j] = "?"

        # GEMİLERİN ÖZELLİKLERİNİ TUTMASI İÇİN BİR LİSTE TANIMLADIM.
        gemi = [[0, 0, 0, 1], [0, 0, 0, 2], [0, 0, 0, 3], [0, 0, 0, 4]]
        toplamhak = (m*m) // 3
        hak = (m*m) // 3
        kullanilanhak = 0

        # 4 ADET GEMİ OLUŞTURMAK İÇİN FOR DÖNGÜSÜ KULLANDIM.
        # MATRİSTE GEMİLERİ "G" HARFİ İLE GÖSTERDİM  VE RANDOM İLE OLUŞTURDUĞUM İNDİSLERE ATADIM.
        for i in range(4):
            if gemi[i][3] == 1:
                gemi[i][0] = random.randint(0, m-1)
                gemi[i][1] = random.randint(0, m-1)
                gemi[i][2] = random.randint(0, 2)
                x1 = gemi[i][0]
                y1 = gemi[i][1]
                yon1 = gemi[i][2]
                uzunluk = gemi[i][3]


                for k in range(1):
                    acikalan[x1][y1] = "G"
                    if yon1 == 0:
                        y1 += 1  # YATAY
                    else:
                        x1 += 1  # DİKEY

            elif gemi[i][3] == 2:
                gemi[i][0] = random.randint(0, m-2)
                gemi[i][1] = random.randint(0, m-2)
                gemi[i][2] = random.randint(0, 2)
                x2 = gemi[i][0]
                y2 = gemi[i][1]
                yon2 = gemi[i][2]
                uzunluk = gemi[i][3]



                for k in range(2):
                    # EĞER BU İNDİSTE GEMİ BULUNUYORSA TEKRAR BİR İNDİS OLUŞTURMASI İÇİN İF KOŞULU KOYDUM.
                    if acikalan[x2][y2] == "G":
                        x2 = random.randint(0, m-2)
                        y2 = random.randint(0, m-2)
                    else:
                        acikalan[x2][y2] = "G"

                    if yon2 == 0:
                        y2 += 1  # YATAY
                    else:
                        x2 += 1  # DİKEY



            elif gemi[i][3] == 3:
                gemi[i][0] = random.randint(0, m-3)
                gemi[i][1] = random.randint(0, m-3)
                gemi[i][2] = random.randint(0, 2)
                x3 = gemi[i][0]
                y3 = gemi[i][1]
                yon3 = gemi[i][2]
                uzunluk = gemi[i][3]


                for k in range(3):
                    # EĞER BU İNDİSTE GEMİ BULUNUYORSA TEKRAR BİR İNDİS OLUŞTURMASI İÇİN İF KOŞULU KOYDUM.
                    if acikalan[x3][y3] == "G":
                        x3 = random.randint(0, m-3)
                        y3 = random.randint(0, m-3)
                    else:
                        acikalan[x3][y3] = "G"

                    if yon3 == 0:
                        y3 += 1   # YATAY
                    else:
                        x3 += 1   # DİKEY


            elif gemi[i][3] == 4:
                gemi[i][0] = random.randint(0, m-4)
                gemi[i][1] = random.randint(0, m-4)
                gemi[i][2] = random.randint(0, 2)
                x4 = gemi[i][0]
                y4 = gemi[i][1]
                yon4 = gemi[i][2]
                uzunluk = gemi[i][3]


                for k in range(4):
                    # EĞER BU İNDİSTE GEMİ BULUNUYORSA TEKRAR BİR İNDİS OLUŞTURMASI İÇİN İF KOŞULU KOYDUM.
                    if acikalan[x4][y4] == "G":
                        x4 = random.randint(0, m-4)
                        y4 = random.randint(0, m-4)
                    else:
                        acikalan[x4][y4] = "G"

                    if yon4 == 0:
                        y4 += 1  # YATAY
                    else:
                        x4 += 1  # DİKEY




        while True:
            mod = int(input("1) Açık Mod \n2) Gizli Mod\n----------------------\nOynamak istediğiniz modu seçiniz : "))
            if mod == 1:
                break
            elif mod == 2:
                break
            else:
                print("Lütfen 1 ya da 2 giriniz :")


        if mod == 1:
            for i in range(m):
                for j in range(m):
                    print(acikalan[i][j], end="   ")
                print("\n")
        elif mod == 2:
            for i in range(m):
                for j in range(m):
                    print(gizlialan[i][j], end="   ")
                print("\n")

        while (True):
            x_koordinat = int(input("X koordinatı giriniz : "))
            if (x_koordinat < 0) | (x_koordinat > m-1):
                while True:
                    print("Lütfen 0 - {} arası bir koordinat giriniz.".format(m-1))
                    x_koordinat = int(input("X koordinatı giriniz : "))
                    if (x_koordinat >= 0) & (x_koordinat <= m-1):
                        break

            y_koordinat = int(input("Y koordinatı giriniz : "))
            if (y_koordinat < 0) | (y_koordinat > m-1):
                while True:
                    print("Lütfen 0 - {} arası bir koordinat giriniz.".format(m-1))
                    y_koordinat = int(input("Y koordinatı giriniz : "))
                    if (y_koordinat >= 0) & (y_koordinat <= m-1):
                        break

            hak -= 1
            kullanilanhak += 1
            print("Kalan hak : {}".format(hak))

            if (acikalan[x_koordinat][y_koordinat] == "X") | (acikalan[x_koordinat][y_koordinat] == "*") | ( gizlialan[x_koordinat][y_koordinat] == "X") | (gizlialan[x_koordinat][y_koordinat] == "*"):
                while True:
                    print("Daha önce girdiğiniz koordinatları giremezsiniz .")
                    x_koordinat = int(input("X koordinatı giriniz : "))
                    if (x_koordinat < 0) | (x_koordinat > m-1):
                        while True:
                            print("Lütfen 0 - {} arası bir koordinat giriniz.".format(m-1))
                            x_koordinat = int(input("X koordinatı giriniz : "))
                            if (x_koordinat >= 0) & (x_koordinat <= m-1):
                                break

                    y_koordinat = int(input("Y koordinatı giriniz : "))
                    if (y_koordinat < 0) | (y_koordinat > m-1):
                        while True:
                            print("Lütfen 0 - {} arası bir koordinat giriniz.".format(m-1))
                            y_koordinat = int(input("Y koordinatı giriniz : "))
                            if (y_koordinat >= 0) & (y_koordinat <= m-1):
                                break

                    print("Kalan hak : {}".format(hak))
                    if (acikalan[x_koordinat][y_koordinat] != "X") & (acikalan[x_koordinat][y_koordinat] != "*") & (
                            gizlialan[x_koordinat][y_koordinat] != "X") & (gizlialan[x_koordinat][y_koordinat] != "*"):
                        break

            # BAŞARILI HAMLE
            if (acikalan[x_koordinat][y_koordinat] == "G"):

                print("Tebrikler bir gemi vurdunuz.")

                if mod == 1:
                    acikalan[x_koordinat][y_koordinat] = "X"
                    if (yon1 == 0):
                        if (acikalan[x1][y1 - 1] == "X"):
                            print("Tebrikler 1 numaralı gemi battı.")
                    else:
                        if (acikalan[x1 - 1][y1] == "X"):
                            print("Tebrikler 1 numaralı gemi battı.")
                    if (yon2 == 0):
                        if (acikalan[x2][y2 - 1] == "X") & (acikalan[x2][y2 - 2] == "X"):
                            print("Tebrikler 2 numaralı gemi battı.")
                    else:
                        if (acikalan[x2 - 1][y2] == "X") & (acikalan[x2 - 2][y2] == "X"):
                            print("Tebrikler 2 numaralı gemi battı.")
                    if (yon3 == 0):
                        if (acikalan[x3][y3 - 3] == "X") & (acikalan[x3][y3 - 2] == "X") & (acikalan[x3][y3 - 1] == "X"):
                            print("Tebrikler 3 numaralı gemi battı.")
                    else:
                        if (acikalan[x3 - 3][y3] == "X") & (acikalan[x3 - 2][y3] == "X") & (acikalan[x3 - 1][y3] == "X"):
                            print("Tebrikler 3 numaralı gemi battı.")
                    if (yon4 == 0):
                        if (acikalan[x4][y4 - 4] == "X") & (acikalan[x4][y4 - 3] == "X") & (acikalan[x4][y4 - 2] == "X") & (acikalan[x4][y4 - 1] == "X"):
                            print("Tebrikler 4 numaralı gemi battı.")
                    else:
                        if (acikalan[x4 - 4][y4] == "X") & (acikalan[x4 - 3][y4] == "X") & (acikalan[x4 - 2][y4] == "X") & (acikalan[x4 - 1][y4] == "X"):
                            print("Tebrikler 4 numaralı gemi battı.")


                elif mod == 2:
                    gizlialan[x_koordinat][y_koordinat] = "X"
                    if (yon1 == 0):
                        if (gizlialan[x1][y1 - 1] == "X"):
                            print("Tebrikler 1 numaralı gemi battı.")
                    else:
                        if (gizlialan[x1 - 1][y1] == "X"):
                            print("Tebrikler 1 numaralı gemi battı.")
                    if (yon2 == 0):
                        if (gizlialan[x2][y2 - 1] == "X") & (gizlialan[x2][y2 - 2] == "X"):
                            print("Tebrikler 2 numaralı gemi battı.")
                    else:
                        if (gizlialan[x2 - 1][y2] == "X") & (gizlialan[x2 - 2][y2] == "X"):
                            print("Tebrikler 2 numaralı gemi battı.")
                    if (yon3 == 0):
                        if (gizlialan[x3][y3 - 3] == "X") & (gizlialan[x3][y3 - 2] == "X") & (gizlialan[x3][y3 - 1] == "X"):
                            print("Tebrikler 3 numaralı gemi battı.")
                    else:
                        if (gizlialan[x3 - 3][y3] == "X") & (gizlialan[x3 - 2][y3] == "X") & (gizlialan[x3 - 1][y3] == "X"):
                            print("Tebrikler 3 numaralı gemi battı.")
                    if (yon4 == 0):
                        if (gizlialan[x4][y4 - 4] == "X") & (gizlialan[x4][y4 - 3] == "X") & (gizlialan[x4][y4 - 2] == "X") & (gizlialan[x4][y4 - 1] == "X"):
                            print("Tebrikler 4 numaralı gemi battı.")
                    else:
                        if (gizlialan[x4 - 4][y4] == "X") & (gizlialan[x4 - 3][y4] == "X") & (gizlialan[x4 - 2][y4] == "X") & (gizlialan[x4 - 1][y4] == "X"):
                            print("Tebrikler 4 numaralı gemi battı.")


            # BAŞARISIZ HAMLE
            else:
                print("Maalesef isabet edemediniz")
                if mod == 1:
                    acikalan[x_koordinat][y_koordinat] = "*"
                elif mod == 2:
                    gizlialan[x_koordinat][y_koordinat] = "*"
            if mod == 1:
                for i in range(m):
                    for j in range(m):
                        print(acikalan[i][j], end="   ")
                    print("\n")
            elif mod == 2:
                for i in range(m):
                    for j in range(m):
                        print(gizlialan[i][j], end="   ")
                    print("\n")

            # GEMİLERİN HEPSİ BİTTİ Mİ KONTROLÜ.
            if (mod == 1):
                tutucu = list()
                Kontrol = None
                for i in acikalan:
                    for j in i:
                        tutucu += [j]
                    if tutucu.count("G") != 0:
                        Kontrol = False
                        continue
                    else:
                        Kontrol = True
                if (Kontrol == True):
                    skor = toplamhak - kullanilanhak
                    print("Tebrikler {} puan ile oyunu kazandınız.".format(skor))
                    break


            elif (mod == 2):
                tutucu2 = list()
                Kontrol2 = None
                for i in gizlialan:
                    for j in i:
                        tutucu2 += [j]
                    if tutucu2.count("X") != 10:
                        Kontrol2 = False
                        continue
                    else:
                        Kontrol2 = True
                if (Kontrol2 == True):
                    skor = toplamhak - kullanilanhak
                    print("Tebrikler {} puan ile oyunu kazandınız.".format(skor))
                    break

            # HAKKIMIZ BİTTİĞİNDE GEMİLERİN HEPSİNİ VURAMADIYSAK GEMİLERİN YERİNİ AÇIK MOD DURUMUNDA EKRANDA GÖSTERMEK İÇİN .
            if hak == 0:
                print("Hakkınız kalmadı. Maalesef Kaybettiniz.")
                for i in range(m):
                    for j in range(m):
                        print(acikalan[i][j], end="   ")
                    print("\n")

                break

    # OYUNDAN ÇIKIŞ YAPMAK İSTEDİĞİMİZDE ÇIKIŞ YAPILIYOR.
    else:
        print("Çıkış yapılıyor.")
        break
