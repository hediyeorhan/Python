"""
Örn : Ali baba ve kırk haramiler
Kelime Sayısı : 5
En Kısa Kelime : ve

**Kelimeler boşluk karakteri ile ayrılır. **
"""

"""
mes = input("Metin giriniz : ")
min_length = len(mes)
min_word = ""
count = 0
wcount = 1
word = ""

for s in mes:
    if s == " ":
        wcount += 1
        if count < min_length:
            min_length = count
            min_word = word
        count = 0
        word = ""
    else:
        word = word + s
        count = count + 1
print("Number of word : {} Shortest Word : {} - Length : {}".format(wcount,min_word,min_length))
"""

##### Aynı örneği dizi ve liste ile yapalım.

kelime = input("Metin giriniz : ")
parça = kelime.split() # kelimelere tek tek erişmek için.
min_uzunluk = len(kelime)
min_kelime = ""
for i in parça:
    if len(i) < min_uzunluk:
        min_uzunluk = len(i)
        min_kelime = i
print("En kısa kelime : {} - Uzunluğu : {} ".format(min_kelime,min_uzunluk))