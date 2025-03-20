class XOX:
    def __init__(self):
        self.durum = True
        self.tahta = [["{ }","{ }","{ }"],["{ }","{ }","{ }"],["{ }","{ }","{ }"]]
        self.sira = 0
    def oyna(self):
        if self.sira%2==0:
            self.oyuncu1()
        else:
            self.oyuncu2()
        self.durum = self.oyunkontrol()
        self.sira += 1
    def oyuncu1(self):
        self.oyunalani()
        print("1.oyuncu")
        satir = int(input("0,1 veya 2 girerek satırı belirleyiniz: "))
        while satir<0 or satir>2:
            satir = int(input("Lütfen 0,1 veya 2 girerek satırı belirleyiniz: "))
        sutun = int(input("0,1 veya 2 girerek sütunu belirleyiniz:"))
        while sutun<0 or sutun>2:
            sutun = int(input("Lütfen 0,1 veya 2 girerek sütunu belirleyiniz:"))
        if self.bosmu(satir,sutun):
            self.oyuncu1()
        else:
            self.tahta[satir][sutun] = "X"
    def oyuncu2(self):
        self.oyunalani()
        print("2.oyuncu")
        satir = int(input("0,1 veya 2 girerek satırı belirleyiniz: "))
        while satir < 0 or satir > 2:
            satir = int(input("Lütfen 0,1 veya 2 girerek satırı belirleyiniz: "))
        sutun = int(input("0,1 veya 2 girerek sütunu belirleyiniz:"))
        while sutun < 0 or sutun > 2:
            sutun = int(input("Lütfen 0,1 veya 2 girerek sütunu belirleyiniz:"))
        if self.bosmu(satir,sutun):
            self.oyuncu2()
        else:
            self.tahta[satir][sutun] = "O"
    def oyunalani(self):
        for i in self.tahta:
            for j in i:
                print(j,end=" ")
            print("\n")
    def oyuncusirasi(self):
        if self.sira/2 == 0:
            return self.oyuncu1()
        if self.sira/2 == 1:
            return self.oyuncu2()
    def oyunkontrol(self):
        if [self.tahta[0][0],self.tahta[0][1],self.tahta[0],[2]] == [["X"],["X"],["X"]] or [self.tahta[0][0],self.tahta[0][1],self.tahta[0],[2]] == [["O"],["O"],["O"]]:
            return False
        if [self.tahta[1][0],self.tahta[1][1],self.tahta[1],[2]] == [["X"],["X"],["X"]] or [self.tahta[1][0],self.tahta[1][1],self.tahta[1],[2]] == [["O"],["O"],["O"]]:
            return False
        if [self.tahta[2][0], self.tahta[2][1], self.tahta[2],[2]] == [["X"], ["X"], ["X"]] or [self.tahta[2][0],self.tahta[2][1],self.tahta[2],[2]] == [["O"], ["O"],["O"]]:
            return False

        if [self.tahta[0][0],self.tahta[1][0],self.tahta[2],[0]] == [["X"],["X"],["X"]] or [self.tahta[0][0],self.tahta[1][0],self.tahta[2],[0]] == [["O"],["O"],["O"]]:
            return False
        if [self.tahta[0][1],self.tahta[1][1],self.tahta[2],[1]] == [["X"],["X"],["X"]] or [self.tahta[1][0],self.tahta[1][1],self.tahta[2],[1]] == [["O"],["O"],["O"]]:
            return False
        if [self.tahta[0][2], self.tahta[1][2], self.tahta[2],[2]] == [["X"], ["X"], ["X"]] or [self.tahta[0][2],self.tahta[1][2],self.tahta[2],[2]] == [["O"], ["O"],["O"]]:
            return False

        if [self.tahta[0][0],self.tahta[1][1],self.tahta[2],[2]] == [["X"],["X"],["X"]] or [self.tahta[0][0],self.tahta[1][1],self.tahta[2],[2]] == [["O"],["O"],["O"]]:
            return False
        if [self.tahta[0][2], self.tahta[1][1], self.tahta[2],[0]] == [["X"], ["X"], ["X"]] or [self.tahta[0][2],self.tahta[1][1],self.tahta[2],[0]] == [["O"], ["O"],["O"]]:
            return False

        return True
    def bosmu(self,satir,sutun):
        if self.tahta[satir][sutun] != "{ }":
            return True
        else:
            return False
xox =XOX()
while xox.durum:
 xox.oyna()

