class kuvvet:
    def __init__(self,maks):
        self.kuvvet = -1
        self.maks = maks
    def __iter__(self):
        return self
    def __next__(self):
        if self.kuvvet < self.maks:
            self.kuvvet += 1
            return 3**self.kuvvet
        else:
            self.kuvvet = -1
            return StopIteration
uckuvvet = kuvvet(5)
ii = iter(uckuvvet)
print(next(ii))
print(next(ii))
print(next(ii))
print(next(ii))
print(next(ii))

print(next(ii))

print(next(ii))

print("for kuvvet...")


print("Fibonacci sayilarin generator ile kullanimi.....")

def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

for i in fibonacci():
    if i > 1000:
        break
    print(i)