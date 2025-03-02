sayi = 1
bolen = 0

while bolen < 500: 
    bolen = 0
    sayi += 1
    for i in range(1,sayi+1):
        if sayi % i == 0:
            bolen += 1
            
print(sayi)


