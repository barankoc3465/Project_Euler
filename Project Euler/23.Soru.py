Bol_sayilar = list()
sinir = 28124

for i in range(1,sinir):
    bolen_toplami = 1
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            bolen_toplami += j
            if i // j != j:
                bolen_toplami += i // j
    if bolen_toplami > i:
        Bol_sayilar.append(i)

Yazilabilen_sayilar = [(i + j) 
                       for i in Bol_sayilar
                       for j in Bol_sayilar
                        if (i + j) < sinir ]
Yazilabilen_sayilar = set(Yazilabilen_sayilar)
Yazilamayan_sayilar = (i for i in range(1,sinir) 
                       if i not in Yazilabilen_sayilar)

print(sum(Yazilamayan_sayilar))



