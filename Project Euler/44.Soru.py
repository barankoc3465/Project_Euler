def pentagonal(n):
    return n * (3*n - 1) / 2
def sayi(p):
    return ((24 * p + 1)**0.5 + 1) / 6
    
en_kucuk = 10000000000
for i in range(1,10000):
    print(i)
    for j in range(1,i):
        k = pentagonal(i) - pentagonal(j) 
        l = pentagonal(i) + pentagonal(j) 
        if int(sayi(k)) == sayi(k) and int(sayi(l)) == sayi(l):
            if k < en_kucuk:
                print(en_kucuk)
                en_kucuk = k

print(en_kucuk)