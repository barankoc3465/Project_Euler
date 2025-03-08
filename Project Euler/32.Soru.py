Pandijital_sayilar = set()
Liste = [str(i) for i in range(1, 10)]

for i in range(10000, 1, -1):
    adet = 0
    for j in range(1, 100):
        sayi = str(i)+str(j)+str(i*j)
        if len(sayi) == 9:
            Kontrol = set()
            for indis in range(len(Liste)):
                if Liste[indis] in sayi:
                    Kontrol.add(Liste[indis])                        
                else:
                    break
            if len(Kontrol) == 9:
                Pandijital_sayilar.add(i*j)

toplam = sum(i for i in Pandijital_sayilar)
print(toplam)
