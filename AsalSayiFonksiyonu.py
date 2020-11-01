def asal(x,y):

    for i in range(x,y+1):
        kontrol = False
        if i == 1 | i == 0:
            kontrol == True
        elif i == 2:
            kontrol = False
        else:
            for j in range(2, i):
                if i % j == 0:
                    kontrol = True

            if kontrol == False:
                print(i)


asal(2,100)
