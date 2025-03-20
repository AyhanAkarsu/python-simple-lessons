def sum(s1 = "", s2 = ""):
    rem = ""
    count = 0
    if(len(s1) > len(s2)):
        s2 = "0" + s2
    elif(len(s2) > len(s1)):
        s1 = "0" + s1
    print(f"sayi1: {s1} sayi2: {s2}")
    for i in range(len(s1)-1,-1,-1):
        if(int(s1[i]) + int(s2[i]) + count <= 9):
            rem += str(int(s1[i]) + int(s2[i]) + count)
            count = 0
        else:
            rem += str((int(s1[i]) + int(s2[i]) + count) % 10)
            count = 1

    print(rem[::-1])

sum("123", "395")