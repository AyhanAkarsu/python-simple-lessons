def ekle(fonk):
    def mukemmel():
        mukemmelsayi = []
        for i in range(1,101):
            t = 0
            for j in range(1,i):
                if i%j == 0:
                    t += j
            if t == i:

               mukemmelsayi.append(i)
        print("Mükemmel sayilar: ",mukemmelsayi)
        fonk()
    return mukemmel

@ekle
def asal():
    asal = []
    for i in range(2,101):
        t = 0
        for j in range(2,i):
            if i%j == 0:
                t = 1
        if t == 0:
            asal.append(i)
    print("Asal sayilar: ",asal)

asal()









