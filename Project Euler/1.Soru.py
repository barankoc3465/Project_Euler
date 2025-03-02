sayi = 0
toplam = 0
adet = 0

while True:
    sayi += 1
    if sayi == 1000:
        break
    else:
        if sayi % 3 == 0 or sayi % 5 == 0:
            toplam += sayi

print(toplam)
