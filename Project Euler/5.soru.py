Liste = list()
Yeni_liste = list()
carpim = 1

for i in range(2, 21):
    Asal_carpanlar = list()
    asal_mi = True
    for j in range(2,i):
        if i % j == 0:
            asal_mi = False
            sayi = i
            bolum = 2
            while sayi != 1:
                if sayi % bolum == 0:
                    sayi //= bolum
                    Asal_carpanlar.append(bolum)
                    continue
                else:
                    bolum += 1
            break
    else:
        if asal_mi == True:
            Asal_carpanlar.append(i)
    Liste.append(Asal_carpanlar)

Asallar = list()

for i in Liste:
    Yeni_liste.extend(i)

Yeni_liste = set(Yeni_liste)

for asal_sayi in Yeni_liste:
    en_buyuk = 0
    for indis in range(len(Liste)):
        if Liste[indis].count(asal_sayi) > en_buyuk:
            en_buyuk = Liste[indis].count(asal_sayi)
    for ekleme in range(en_buyuk):
        Asallar.append(asal_sayi)

for i in Asallar:
    carpim *= i
    
print(carpim)