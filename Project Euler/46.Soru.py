def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True
    
def goldbach(sayi):
    for asal_sayi in range(2,sayi):
        if asal_mi(asal_sayi) == True:
            for i in range(1,sayi):
                if sayi == asal_sayi + 2 * i**2:
                    return True
    return False

sayi = 3
while True:
    sayi += 2
    if asal_mi(sayi) == False and goldbach(sayi) == False:
        print(sayi)
        break