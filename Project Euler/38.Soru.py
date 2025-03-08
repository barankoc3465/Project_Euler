en_buyuk = 0
for i in range(1,10000):
    sayi = ""
    for j in range(1,10):
        sayi += str(i*j)
        if len(sayi) == 9 and "0" not in sayi:
            Kume = set()
            for rakam in sayi:
                Kume.add(rakam) 
            if len(Kume) == 9 and en_buyuk < int(sayi) :
                en_buyuk = int(sayi)
                break
print(en_buyuk)