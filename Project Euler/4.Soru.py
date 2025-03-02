en_buyuk = 0

for i in range(999,1,-1):
    for j in range(i,1,-1):
        carpim = i * j 
        if str(carpim) == str(carpim)[::-1] and en_buyuk< carpim:
            en_buyuk = carpim

print(en_buyuk)