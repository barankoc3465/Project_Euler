en_buyuk_n = 0
Liste = list()

for i in range(2,1000):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        Liste.append(i)

for a in range(-1000,1000):
    for b in Liste:
        asal_sayisi = 0
        for n in range(100):
            sayi = n**2 + n*a + b
            if sayi >= 2:
                asal_mi = True
                for i in range(2,int(sayi**0.5)+1):
                    if sayi % i == 0:
                        asal_mi = False
                        break
                if asal_mi == True: 
                    asal_sayisi += 1
                else:
                    if en_buyuk_n < asal_sayisi:
                        en_buyuk_n = asal_sayisi
                        ikinci_sayi = b
                        birinci_sayi = a
                    break

print("n : {}, a : {}, b : {}".format(en_buyuk_n,birinci_sayi,ikinci_sayi))
print("a x b = {}".format(birinci_sayi*ikinci_sayi))
