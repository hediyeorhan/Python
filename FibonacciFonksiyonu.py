def fibonacci(x):
    a = 1
    b = 1
    fibonacci = [a, b]
    for i in range(100):
        a, b = b, a + b

        fibonacci.append(b)
    print(fibonacci)


    print("\n --> {}. Eleman : {}".format(x,fibonacci[x-1]))


eleman = int(input("Kaçıncı elemanı aramak istersiniz : "))
fibonacci(eleman)