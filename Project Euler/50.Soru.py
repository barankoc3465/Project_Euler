def asal_mi(sayi):
    if sayi >= 2:
        for i in range(2,int(sayi**0.5) + 1):
            if sayi % i == 0:
                return False
        return True
    else:
        return False

def asal_sayi_listesi(limit):
    Asal_Sayilar = list()
    for sayi in range(2, limit):
        if asal_mi(sayi) == True:
            Asal_Sayilar.append(sayi)
    return Asal_Sayilar

def en_uzun_ardisik_asal_listesi(Asal_sayilar, hedef_asal):
    En_uzun_ardisik_asallar = list()
    for i in range(len(Asal_sayilar)):
        Liste = list()
        toplam = 0
        for indis in range(i, len(Asal_sayilar)):
            Liste.append(Asal_sayilar[indis])
            toplam += Asal_sayilar[indis]
            if toplam == hedef_asal:
                if len(Liste) > len(En_uzun_ardisik_asallar):
                    En_uzun_ardisik_asallar = Liste
            elif toplam > hedef_asal:
                break
    return En_uzun_ardisik_asallar

limit = 1000000
Asal_sayilar = asal_sayi_listesi(limit)
Asal_sayilar.reverse()
uzunluk = 0
toplam = 0

for asal in Asal_sayilar:
    ardisik_asal_uzunluğu = en_uzun_ardisik_asal_listesi(Asal_sayilar, asal)
    if len(ardisik_asal_uzunluğu) > uzunluk:
        uzunluk = len(ardisik_asal_uzunluğu)
        toplam = asal

print(toplam)