def asal_mi(sayi):
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def permutasyon_mu(sayi_1,sayi_2):
    if sorted(str(sayi_1)) == sorted(str(sayi_2)):
        return True
    return False

def aritmatik_dizi_mi(sayi_1,sayi_2,sayi_3):
    if sayi_2 - sayi_1 == sayi_3 - sayi_2:
        return True
    return False

sinir = 10000
for sayi_1 in range(1000, sinir):
    for sayi_2 in range(sayi_1 + 1, sinir):
        sayi_3 =  sayi_2 + sayi_2 - sayi_1 
        if aritmatik_dizi_mi(sayi_1, sayi_2, sayi_3):
            if permutasyon_mu(sayi_1, sayi_2) and permutasyon_mu(sayi_1, sayi_3):
                if asal_mi(sayi_1) and asal_mi(sayi_2) and (asal_mi(sayi_3)):
                    if sayi_1 != 1487:
                        cevap = "{}{}{}".format(sayi_1,sayi_2,sayi_3)
                        print(cevap)
                        exit()
                        

