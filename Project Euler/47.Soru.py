def asal_mi(sayi):
    for i in range(2,int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

sayi = 1
while True:
    sayi += 1
    kontrol_sayisi = sayi
    ardısık = 0
    while ardısık != 4:
        adet = 0
        for asal in range(2,kontrol_sayisi):
            if kontrol_sayisi % asal == 0:
                if asal_mi(asal):
                    adet += 1
            if adet == 4:
                kontrol_sayisi += 1
                ardısık += 1
                break
        else:
            break
    if ardısık == 4:
        print(sayi)
        break
    