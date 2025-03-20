import json
class Uyelik():
    def __init__(self):
        self.durum = True
        self.veriler = {}
        self.veriler["kullanicilar"] = []

    def Calistir(self):
        self.Arayuz()
        try:
            secim = int(input("Lütfen seçiminizi yapınız: "))
        except ValueError:
            secim = int(input("Lütten sayı giriniz... :"))
        if secim == 1:
            self.girisyap()
        if secim ==2:
            self.KayitOl()
        if secim == 3:
            self.SifremiUnuttum()
        if secim == 4:
            self.Cikis()
        if secim <0 or secim >4:
            print("Lütfen 1,2,3 ve 4 sayılarından bir sayı giriniz....")

    def Arayuz(self):
        print("""
        Lütffen Yapmak İstediğiniz İşlemi Seçiniz:
        Giris Yap ---> 1
        Kayıt Ol  ---> 2
        Şifremi Unuttum --> 3
        Çıkış  ----> 4
        """)

    def girisyap(self):
        girissayii = 3
        while True:
            with open("veriler.json","r+") as dosya:
                self.veriler = json.load(dosya)
                for kullanici in self.veriler["kullanicilar"]:
                     isimgiris = input("Kullanıcı adınızı giriniz: ")
                     sifregiris = input("Şifrenizi giriniz: ")
                     if kullanici["KullaniciAdi"] == "{}".format(isimgiris) and kullanici["Sifre"] == "{}".format(sifregiris):
                        print("Başarılı bir şekilde giriş yapıldı.")
                        return False
                     elif kullanici["KullaniciAdi"] != "{}".format(isimgiris) or kullanici["Sifre"] != "{}".format(sifregiris):
                         print("Hatalı giriş yaptınız: ")
                         girissayii -= 1
                         print("giriş hakkı...",girissayii)
                     if girissayii == 0:
                         print("Hatalı giriş yaptınız daha sonra deneyiniz...")
                         return False

    def KayitOl(self):
        isim = input("Lütfen isim giriniz: ")
        sifre = input("Lütfen sifrenizi giriniz: ")
        eposta = input("Lütfen epostanizi giriniz: ")
        self.veriler["kullanicilar"].append({"KullaniciAdi" : "{}".format(isim),"Sifre" : "{}".format(sifre),"Mail":"{}".format(eposta)})
        dogrulama = int(input("Epostaya gelen doğrulamayı giriniz: "))
        if dogrulama == 1:
            with open("veriler.json","r+") as dosya:
                json.dump(self.veriler,dosya)
            print("Üyelik başarıyla gerçeklerştirildi.")
        else:
            print("Lütfen size gönderilen numarayı doğru giriniz: ")
            self.KayitOl()

    def SifremiUnuttum(self):
        girishakki = 3
        while True:
            with open("veriler.json", "r+") as dosya:
                self.veriler = json.load(dosya)
                for kullanici in self.veriler["kullanicilar"]:
                    kurtarma = input("Kullanıcı adını giriniz: ")
                    kurtarmam = input("Epostanızı giriniz: ")
                    if kullanici["KullaniciAdi"] == "{}".format(kurtarma) and kullanici["Mail"] == "{}".format(kurtarmam):
                        yeniS = input("Yeni şifrenizi giriniz..:  ")
                        self.veriler["kullanicilar"].append({"Sifre" : "{}".format(yeniS)})
                        print("Başarılı bir şekilde şifre değitirildi...")
                        return False
                    elif kullanici["KullaniciAdi"] != "{}".format(kurtarma) and kullanici["Mail"] == "{}".format(kurtarmam):
                        print("Kullanıcı adi yanlış..")
                        girishakki -= 1
                        print("Giriş hakkı...", girishakki)
                    elif kullanici["KullaniciAdi"] == "{}".format(kurtarma) and kullanici["Mail"] != "{}".format(kurtarmam):
                        print("Şifre yanlış..")
                        girishakki -= 1
                        print("Giriş hakkı...", girishakki)
                    elif kullanici["KullaniciAdi"] != "{}".format(kurtarma) and kullanici["Mail"] != "{}".format(kurtarmam):
                        print("Yanlış giriş yaptınız..")
                        girishakki -= 1
                        print("Giriş hakkı...",girishakki)
                    if girishakki == 0:
                        print("Giriş hakkınız bitti daha sonra deneyin....")
                        return False

    def Cikis(self):
        self.durum = False
uyelik = Uyelik()
while uyelik.durum:
    uyelik.Calistir()




