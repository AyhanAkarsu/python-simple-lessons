import random
class kumanda():
    def __init__(self):
        self.durum = True
        self.kanal = []
        self.ses = 0
        self.suankiKanal = ""
        self.Televizyondurumu = ""

    def kanalsec(self):
        self.kanalgoster()
        sec = int(input("izlemek istediğiniz kanalı seçiniz..."))
        self.suankiKanal = self.kanal[sec-1]
        print(self.kanal[sec-1])

    def kanalekle(self):
        kanallar = input("Kanalları giriniz")
        kanallar.split(",")
        self.kanal.append(kanallar)

    def sesAyari(self):
        while True:
            sesA = input("ses arttırmak için + \nSes azaltmak için -\nçıkış için herhangi bir tuşa basın..")
            if (sesA == "+") and (self.ses <= 100) and (self.ses >= 0):
                self.ses += 5
                print(self.ses)
            elif (sesA == "-") and (self.ses <= 100) and (self.ses >= 0):
                self.ses -= 5
                print(self.ses)
            else:
                print("Çıkış yapılıyor")
                return False

    def kanalcikar(self):
        self.kanalgoster()
        cikar = int(input("Çıkarmak istediğiniz kanalın numarasını giriniz"))
        self.kanal.pop(cikar-1)
        self.kanalgoster()

    def rastgelekanal(self):
        self.suankiKanal = random.choice(self.kanal)
        print(random.choice(self.kanal))

    def Cikis(self):
        self.durum = False

    def calistir(self):
        self.menu()
        secim = int(input("Seciminizi yapınız: "))
        if secim == 1:
            self.kanalekle()
        if secim == 2:
            self.kanalcikar()
        if secim == 3:
            self.sesAyari()
        if secim == 4:
            self.rastgelekanal()
        if secim == 5:
            self.Cikis()
        if secim == 6:
            self.televiyondurum()
        if secim == 7:
            self.kanalgoster()
        if secim == 8:
            self.kanalsec()
        if secim == 9:
            self.kanalsayisi()
    def televiyondurum(self):
        ackapa = int(input("Televiyonu açmak için 1 kapatmak için 0 giriniz..."))
        if ackapa == 1:
            self.Televizyondurumu = "Televizyon Açık"
            print("Televizyon acılıyor...")
        elif ackapa == 0:
            print("Televizyon kapatılıyor...")
            self.Televizyondurumu = "Televizyon Kapalı"

    def menu(self):
        print("""
              {} : Televiyon durumu
              {} : Şuanki kanal
              {} : Ses
              \n1.Kanal ekle: 
              \n2.Kanal çıkar:
              \n3.Ses ayarı:
              \n4.Rastgele kanal aç:
              \n5.Çıkış:
              \n6.Televizyon aç kapa:
              \n7.Kanalları göster:
              \n8.Kanal seç:
              \n9.Kanal sayısı:
              """.format(self.Televizyondurumu,self.suankiKanal,self.ses))

    def kanalgoster(self):
        for i in range(len(self.kanal)):
            print(i+1,".Kanal...",self.kanal[i])

    def kanalsayisi(self):

        sayi = 0
        for i in range(len(self.kanal)):
            sayi = i
        print("kanal sayısı:",sayi)

Kumanda = kumanda()
while Kumanda.durum:
    Kumanda.calistir()








