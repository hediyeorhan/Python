nisan = haziran = eylul = kasim = 30

subat = 28

ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31

birimFiyat = 0.79

AylikTuketim = input("Aylık ne kadar elektrik tüketiyorsunuz ?")

dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz ?
(Lütfen ay adının tamamını küçük harf ile giriniz.)\n""")

ay = eval(dönem)

gunlukTuketim = int(AylikTuketim) / ay

fatura = birimFiyat * int(AylikTuketim)

print("Günlük Tüketim Miktarınız : {} TL\n Fatura : {} TL\n".format(gunlukTuketim,fatura,'.2f'))