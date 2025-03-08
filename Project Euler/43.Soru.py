import itertools

Liste = list(itertools.permutations('0123456789'))
Asal_sayilar = list()
sayi = 1
while len(Asal_sayilar) != 7:
    sayi += 1
    for i in range(2,int(sayi**0.5)+1):
        if sayi % i == 0:
            break
    else:
        Asal_sayilar.append(sayi)

toplam = 0
for sayi in Liste:
    ozel_mi = True
    sayi = "".join(sayi)
    if sayi[0] != "0":
        for indis in range(len(Asal_sayilar)):
            if int(sayi[indis+1:indis+4]) % Asal_sayilar[indis] != 0:
                ozel_mi = False
                break
        if ozel_mi == True:
            toplam += int(sayi)

print(toplam)