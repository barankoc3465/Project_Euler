hedef = 10**7

for sayi in range(1,hedef):
    if "0" not in str(sayi):
        Kume = set()
        for harf in str(sayi):
            Kume.add(harf)
            if int(harf) > len(str(sayi)):
                break
        else:
            if len(Kume) == len(str(sayi)):
                for i in range(2,int(sayi**0.5)+1):
                    if sayi % i == 0:
                        break
                else:
                    sonuc = sayi

print(sonuc)