import time
def zamanH(fonk):
    def zaman(sayilar):
        baslama = time.time()
        sonuc = fonk(sayilar)
        bitis = time.time()
        print(fonk.__name__+" "+str(bitis-baslama)+"saniye sürdü")
        return sonuc
    return zaman
@zamanH
def kare(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc
@zamanH
def kup(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**3)
    return sonuc

kup(range(100000))
kare(range(100000))
