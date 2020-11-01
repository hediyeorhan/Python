kelime = input("Kelime giriniz : ")

for i in kelime:
#for i in range(len(kelime)):  --------  İki şekilde de yazılabilir.
    TersKelime = kelime[::-1]
    if(TersKelime == kelime):
        print("Kelime Polindrom ! -- {} - {}".format(kelime,TersKelime))
        break
    else:
        print("Kelime Polindrom değil!")
        break