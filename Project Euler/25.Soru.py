a = 0
b = 1
dongu_sayisi = 0

while len(str(a)) != 1000:
    dongu_sayisi += 1
    c = a
    a = b
    b += c

print(dongu_sayisi)