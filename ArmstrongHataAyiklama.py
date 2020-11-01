def find_armstrong(num):
    assert type(num) == int, "Veri tipi hatası. Int dışında veri tipi."
    assert num >= 0, "Sayı negatif!"
    num_digit = len(str(num))
    temp = num
    total = 0
    while temp != 0:
        digit = temp % 10
        total += digit ** num_digit
        temp = temp // 10
        if num == total:
            return True
        else:
            return False

print(find_armstrong(152))