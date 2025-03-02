sayi = 1
Asal_sayilar = list() 

while len(Asal_sayilar) != 10001:
    sayi += 1
    for j in range(2,int(sayi**0.5)+1):
        if sayi % j == 0:
            break
    else:
        Asal_sayilar.append(sayi)

print(Asal_sayilar[-1])