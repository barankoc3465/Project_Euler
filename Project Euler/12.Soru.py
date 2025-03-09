def ucgen_sayisi(sayi):
    return sayi * (sayi + 1) / 2

sinir = 1000000
for n in range(1,sinir):
    sayi = ucgen_sayisi(n)
    adet = 0
    for bolen in range(1,int(sayi**0.5)):
        if sayi % bolen == 0:
            adet += 1
    adet *= 2
    if adet > 500:
        print(int(sayi))
        break