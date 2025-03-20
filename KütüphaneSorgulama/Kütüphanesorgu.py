import sqlite3
class Kutuphane:
    def __init__(self,isim,yazar,tur,yayinevi,baski):
        self.isim = isim
        self.yazar = yazar
        self.tur = tur
        self.yayinevi = yayinevi
        self.baski = baski
    def __str__(self):
        return "isim: {} yazar: {} tur: {} yayinevi: {} baski: {}".format(self.isim,self.yazar,self.tur,self.yayinevi,self.baski)
class islemler:
    def __init__(self):
        self.durum = True
        self.baglantiolustur()

    def baglantiolustur(self):
        self.baglanti = sqlite3.connect("kütüphane.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE NEW TABLE IF EXISTS kitaplik(isim TEXT,yazar TEXT,tur TEXT,yayinevi TEXT,baski INT")
        self.baglanti.commit()
    def baglantikapat(self):
        self.baglanti.close()
        print("Proğram sonlandırılıyor.")
        self.durum = False
    def kutuphanegoster(self):
        self.cursor.execute("Select * From kitaplik")
        kitaplar = self.cursor.fetchall()
        for i in kitaplar:
            if len(kitaplar) == 0:
                print("Kütüphane boş")
            else:
                kutuphane = Kutuphane(i[0],i[1],[2],i[3],i[4])
                print(kutuphane)
    def kitapara(self):
        isim = input("Aradığınız kitap ismini giriniz: ")
        self.cursor.execute("Select * From kitaplik where isim = ?",(isim,))
        kitaplar = self.cursor.fetchall()
        for i in kitaplar:
            if len(kitaplar) == 0:
                print("Aradığınız kitap bulunamadı...")
            else:
                kutuphane = Kutuphane(i[0][0],i[0][1],i[0][2],i[0][3],i[0][4])
                print(kutuphane)
    def kitapekle(self):
        isim = input("Kitap ismi giriniz: ")
        yazar = input("Yazar ismini giriniz: ")
        tur = input("Kitabın türünü giriniz: ")
        yayinevi = input("kitabın yayın evini giriniz: ")
        baski = input("kitap baskısını giriniz: ")
        self.cursor.execute("Insert into kitaplik Values(?,?,?,?,?",(isim,yazar,tur,yayinevi,baski))
        self.baglanti.commit()
    def kitapsil(self):
        isim = input("Silmek istediğiniz kitabın ismini giriniz: ")
        self.cursor.execute("Delete From kitaplik where isim = ?",(isim,))
        sil = self.cursor.fetchall()
        if len(sil) == 0:
            print("Böyle bir kitap bulunmamaktadır...")
        else:
            karar = input("Eminmisiniz(E/H): ")
            if karar == "E":
                self.baglanti.commit()
                print("Başarı bir şekilde silindi")
            else:
                self.calistir()
                pass
    def baskiyukselt(self):
        isim = input("Baskı yükseltmek isteddiğiniz kitab ismini giriniz")
        self.cursor.execute("Select isim From kitaplik")
        kitap = self.cursor.fetchall()
        for i in kitap:
            if len(kitap) == 0:
                print("Böyle bir kitap bulunamadı..")
            else:
                baski = kitap[0][4]
                baski +=1
                self.cursor.execute("Update kitaplik set baski = ? where isim = ?",(baski,isim))
                self.baglanti.commit()
    def arayuz(self):
        print("""
        **********************
        1. Kütüphaneyi göster
        2. Kitap ara
        3. Kitap ekle
        4. Kitap sil
        5. Baskı sayısını yükselt
        6.Çıkış
        *************************
        """)
    def calistir(self):
        secim = int(input("Yapmak istediğiniz işlemi seçiniz: "))
        if secim == 1:
            self.kutuphanegoster()
        if secim == 2:
            self.kitapara()
        if secim == 3:
            self.kitapekle()
        if secim == 4:
            self.kitapsil()
        if secim == 5:
            self.baskiyukselt()
        if secim == 6:
            self.baglantikapat()


islemlerr = islemler()
islemlerr.calistir()














