import random
class MP3Calar():
    def __init__(self,):
        self.suancalansarki= " "
        self.sarkilar = []
        self.durum = True
        self.ses = 100
    def sarkiSec(self):
        secilensarki=int(input("Seçmek istediğiniz şarkı numarasını giriniz:"))
        sayac=1
        for sarki in self.sarkilar:
            print("{}. {}.".format(sayac,sarki))
            sayac +=1
            self.suancalansarki=self.sarkilar[secilensarki-1]
    def sesArttir(self):
        self.ses += 10
    def sesAzalt(self):
      self.ses-=10
    def rastgeleSarkisec(self):
        random.choice(self.sarkilar)
    def sarkiEkle(self):
        sadigrup=input("sanatcı veya gurup ismi giriniz")
        sarkiadi=input("Şarkı adı giriniz")
        self.sarkilar.append(sarkiadi+" "+sadigrup)
    def sarkiSil(self):
        secilensarki = int(input("Silmek istediğiniz şarkı numarasını giriniz:"))
        sayac = 1
        for sarki in self.sarkilar:
            print("{}. {}.".format(sayac, sarki))
            sayac += 1
            self.sarkilar.pop(secilensarki-1)
    def kapat(self):
        self.durum = False
    def menuGoster(self):
        print("""MP3 ÇALAR
        Şarkı listesi: {}
        Şuan çalan şarkı: {}
        Ses seviyesi {}
        1.Sarkı seç
        2.Ses arttır
        3.Ses azalt
        4.Rastgele şarkı seç
        5.Sarkı ekle
        6.Sarkı sil
        7.Kapat
        """.format(self.sarkilar,self.suancalansarki,self.ses))

    def calistir(self):
        self.menuGoster()
        secim = int(input("Seciminizi yapınız.."))
        if secim == 1:
            self.sarkiSec()
        elif secim == 2:
            self.sesArttir()
        elif secim == 3:
            self.sesAzalt()
        elif secim == 4:
            self.rastgeleSarkisec()
        elif secim == 5:
            self.sarkiEkle()
        elif secim == 6:
            self.sarkiSil()
        elif secim == 7:
            self.kapat()
mp3calar = MP3Calar()
while mp3calar.durum:
    mp3calar.calistir()
print("program sonlandı")


