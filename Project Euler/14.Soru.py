Sozluk = dict()
sayi = 1
bitis = 1000000

while sayi != bitis:
    adim_sayisi = 0
    sayi += 1
    kontrol = sayi
    is_true = True
    while kontrol != 1:
        if kontrol in Sozluk.keys():
            Sozluk[sayi] = Sozluk[kontrol] + adim_sayisi
            is_true = False
            break
        elif kontrol % 2 == 0:
            kontrol //= 2
            adim_sayisi += 1

        else:
            kontrol = kontrol*3+1
            adim_sayisi += 1
    if is_true == True:
        Sozluk[sayi] = adim_sayisi

deger = max(Sozluk.values())

for key,value in Sozluk.items():
    if value == deger:
        anahtar = key
        break

print(f"Sayı : {key}, Zincir Uzunluğu : {deger}")