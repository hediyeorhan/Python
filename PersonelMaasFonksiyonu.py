def maas_zam(mevcutmaas,cocuksayisi,eskizam):
    if mevcutmaas < 2000:
        yenizam = (mevcutmaas * 0.2) + (cocuksayisi * 30)
    elif 2000 < mevcutmaas < 3000:
        yenizam = (mevcutmaas * 0.15) + (cocuksayisi * 30)
    elif mevcutmaas > 3000:
        yenizam = (mevcutmaas * 0.1) + (cocuksayisi * 30)
    if yenizam < eskizam:
        yenimaas = mevcutmaas + eskizam
    else:
        yenimaas = mevcutmaas + yenizam

    return yenimaas,yenizam


mevcutmaas = float(input("Mevcut maas : "))
cocuksayisi = int(input("Çocuk sayısı : "))
eskizam = float(input("Eski Zam : "))
yenimaas,yenizam = maas_zam(mevcutmaas,cocuksayisi,eskizam)
print("\n------------------------------------------\n")
print("Mevcut maaş : {}\nÇocuk Sayısı : {}\nEski Zam : {}\nYeni Maaş : {}\nYeni Zam : {}".format(mevcutmaas,cocuksayisi,eskizam,yenimaas,yenizam))

