import math

sayi = math.factorial(100)
rakamlar_toplami = math.fsum(int(rakam) for rakam in str(sayi))

print(rakamlar_toplami)