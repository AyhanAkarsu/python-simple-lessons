import pandas as pd

cumle = input("Cumlenizi giriniz: ")
cumle_listesi = cumle.lower().split()

Kelime_ve_sayisi = {}
for i in cumle_listesi:
    if i in Kelime_ve_sayisi:
        Kelime_ve_sayisi[i] += 1
    else:
        Kelime_ve_sayisi[i] = 1



harf_frekansi_df = pd.DataFrame({"Harf": Kelime_ve_sayisi.keys(),
                                "H_Sayi" : Kelime_ve_sayisi.values()})
print(harf_frekansi_df)
