vize = int(input("Vize notu : "))
finalNotu = int(input("Final notu : "))

gecme_notu = vize * 0.4 + finalNotu * 0.6

if(gecme_notu >= 90):
    print("Geçme Notu : {} - Harf Notu : AA".format(gecme_notu))
elif(gecme_notu < 90) & (gecme_notu > 80):
    print("Geçme Notu : {} - Harf Notu : BA".format(gecme_notu))
elif(gecme_notu < 80) & (gecme_notu > 75):
    print("Geçme Notu : {} - Harf Notu : BB".format(gecme_notu))
elif(gecme_notu < 75) & (gecme_notu > 70):
    print("Geçme Notu : {} - Harf Notu : CB".format(gecme_notu))
elif(gecme_notu < 70) & (gecme_notu > 65):
    print("Geçme Notu : {} - Harf Notu : CC".format(gecme_notu))
elif(gecme_notu < 65) & (gecme_notu > 60):
    print("Geçme Notu : {} - Harf Notu : DC".format(gecme_notu))
elif(gecme_notu < 60) & (gecme_notu > 55):
    print("Kaldınız - Harf Notu : DD".format(gecme_notu))
elif(gecme_notu < 55) & (gecme_notu > 50):
    print("Kaldınız - Harf Notu : FD".format(gecme_notu))
else:
    print("Kaldınız - Harf Notu : FF".format(gecme_notu))
