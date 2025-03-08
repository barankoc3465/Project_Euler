en_buyuk = 0

for p in range(1,1000):
    print(p)
    Kume = set()
    for a in range(1,p):
        for b in range(1,a):
            c = ( a**2 + b**2 )**0.5
            if a + b + c == p:
                Kume.add((a,b,c))
    if en_buyuk < len(Kume):
        en_buyuk = len(Kume)
        en_buyuk_p = p

print(en_buyuk_p)