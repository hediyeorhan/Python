trans_table = {
    "Ö" : "O",
    "Ü" : "U",
    "İ" : "I",
    "Ç" : "C",
    "Ş" : "S",
    "Ğ" : "G",
    "ö" : "o",
    "ü" : "u",
    "ı" : "i",
    "ç" : "c",
    "ş" : "s",
    "ğ" : "g",

}
turkcekarakter = "ÖÜİÇŞĞöüıçşğ"
metin = input("Lütfen bir metin giriniz : ")
newMetin = " "

for i in metin:
    if i in turkcekarakter:
        newMetin += trans_table[i]
    else:
        newMetin += i
print(newMetin)