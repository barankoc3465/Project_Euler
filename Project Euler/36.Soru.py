hedef = 1000000
toplam = 0
for sayi in range(1,hedef):
    if str(sayi)[-1] != 0 and sayi == int(str(sayi)[::-1]):
            print(sayi)
            if str(bin(sayi))[-1] != 0 and str(bin(sayi))[2:] == str(bin(sayi))[:1:-1]:
                toplam += sayi

print(toplam)