sayi = 0
yeni_sayi = ""
while len(yeni_sayi) < 1000000:
    print(sayi)
    sayi += 1
    yeni_sayi += str(sayi)

carpim = 1 
for i in range(7):
    carpim *= int(yeni_sayi[(10**i)-1])

print(carpim)