sayi = 2
toplam = 2

while sayi != 2000000: 
    sayi += 1
    if sayi % 2 != 0:
        for i in range(2,int(sayi**0.5)+1):
            if sayi % i == 0:
                break
        else:
            toplam += sayi

print(toplam)