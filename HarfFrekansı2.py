cumle = input("Cumlenizi giriniz: ")
harf_frekansi = {}
for i in cumle:
    if i in harf_frekansi:
        harf_frekansi[i] += 1
    else:
        harf_frekansi[i] = 1

for i, j in harf_frekansi.items():
    print(f"{i} : {j}")