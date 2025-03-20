cumle = input("Cumlenizi giriniz: ")
cumledizi = []
sayi = []
for i in cumle:
    if not(i in cumledizi) and i != " ":
        cumledizi.append(i)
for i in cumledizi:
    c = 0
    for j in cumle:
        if i == j:
            c +=1
    sayi.append(c)
for i in range(len(cumle)):
    print("Harf: {} cümle içindeki sayisi {}".format(cumledizi[i],sayi[i]))