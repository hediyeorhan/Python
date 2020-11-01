"""
Kullanıcıdan alınan stringi sırayla her seferinde
tek karakter ekleyerek ekranda gösteren Python
kodunu yazınız.

"""

kelime = input("Kelime : ")
j = 0

for i in range(len(kelime)):

    print(kelime[0:j:1])
    j -= 1


