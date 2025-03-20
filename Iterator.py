class kanallar:
    def __init__(self,kanallar):
        self.kanallar = kanallar
        self.indeks = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.indeks +=1
        if self.indeks < len(self.kanallar):
            return self.kanallar[self.indeks]
        else:
            self.indeks = -1
            raise StopIteration

kanal = kanallar(["atv","kanald","startv"])
iterr = iter(kanal)
print(next(iterr))
print(next(iterr))
print(next(kanal))
