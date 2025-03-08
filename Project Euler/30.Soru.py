baslangic = 2
bitis = sum(9**5 for i in range(9)) + 1
sayilar_toplami = 0

for sayi in range(baslangic,bitis):
    rakamlar_toplami = sum(int(rakam)**5 for rakam in str(sayi))
    if rakamlar_toplami == sayi:
        sayilar_toplami += rakamlar_toplami

print(sayilar_toplami)