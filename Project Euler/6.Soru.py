toplam = sum(i for i in range(1,101))
toplam_karesi = toplam ** 2
kare_toplam = sum(i**2 for i in range(1,101))
sonuc = toplam_karesi - kare_toplam

print(sonuc)