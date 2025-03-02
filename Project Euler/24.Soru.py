import math

n = 999999
Rakamlar = [str(i) for i in range(10)]
Faktoriyel = [math.factorial(i) for i in range(10)]
sayi = ""

for i in range(9,-1,-1):
    indis = n // Faktoriyel[i]
    sayi += Rakamlar.pop(indis)
    n %= Faktoriyel[i]

print(sayi)



import itertools

rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sira = 999999
hedef = "".join(list(itertools.permutations(rakamlar))[sira])

print(hedef)