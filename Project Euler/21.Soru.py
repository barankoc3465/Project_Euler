Sozluk = dict()

for i in range(1,10000):
    bolen_toplami_a = 0
    for j in range(1,i):
        if i % j == 0:
            bolen_toplami_a += j
    Sozluk[i] = bolen_toplami_a

toplam = 0

for anahtar,deger in Sozluk.items():
    if deger in Sozluk and anahtar != deger and Sozluk[Sozluk[anahtar]] == anahtar:
        toplam += anahtar
    
print(f"10 binin altındaki dost sayıların toplamı : {toplam}")