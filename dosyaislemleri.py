class dosya():
    def __init__(self):
        with open("MehemetAkifErsoy.txt","r",encoding="utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimelre = []
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip(" ")
                self.sade_kelimelre.append(i)
            
    def kume(self):
       kkume = set()
       for i in self.sade_kelimelre:
           kkume.add(i)
       for i in kkume:
           print(i)
           print("***********************")
    def sozluk(self):
        keleime_sozluk = dict()
        for i in self.sade_kelimelre:
            if (i in keleime_sozluk):
                keleime_sozluk[i] += 1
            else:
                keleime_sozluk[i] = 1
        for kelime,sayi in keleime_sozluk.items():
            print("{} kelimesi {} defa var".format(kelime,sayi))





Dosya = dosya()
Dosya.sozluk()

