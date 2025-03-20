import sqlite3
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT, yazar TEXT, yayinevi TEXT, sayfasayisi INT)")
    con.commit()
def veriekleme():
    cursor.execute("Insert into kitaplik Values('İnstanbul Hatırası','Ahmet ümit','Everst','561')")
    con.commit()
def veriekle2():
    isim = input("İsim: ")
    yazar = input("Yazar: ")
    yayinevi = input("Yayinevi: ")
    sayfa_sayisi = int(input("Sayfa sayisi: "))
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verilerial():
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print("kitaplık bilgileri..")
    for i in liste:
        print(i)
def verilerial2():
    cursor.execute("Select isim,sayfasayisi From kitaplik")
    liste = cursor.fetchall()
    print("kitaplık bilgileri(isim,sayfa sayisi)..")
    for i in liste:
        print(i)
def verilerial3():
    yayinevi = input("Everest: ")
    cursor.execute("Select * From kitaplik where yayinevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("kitaplık bilgileri(Everest yayin olanlar.)..")
    for i in liste:
        print(i)
def veriguncelle():
    eskiveri = input("Eski veriyi giriniz: ")
    yeniveri = input("Yeni veriyi giriniz: ")
    cursor.execute("Update kitaplik set yayinevi = ? where yayinevi = ?",(yeniveri,eskiveri))
    con.commit()
def verisil():
    isim = input("Çıkarmak istediğiniz kitap ismini giriniz: ")
    cursor.execute("Delete From kitaplik where isim = ?",(isim,))
    con.commit()

tablo_olustur()
veriekle2()
con.close()
