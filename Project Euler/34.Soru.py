import math

Liste = list()
for sayi in range(10,100000):
    faktoriyel_toplami = 0
    for harf in str(sayi):
        faktoriyel_toplami += math.factorial(int(harf))
    if faktoriyel_toplami == sayi:
        Liste.append(sayi)

sum = sum(i for i in Liste)
print(sum)