import math

carpim= math.prod(2 for i in range(1000))
toplam = math.fsum(int(i) for i in str(carpim))

print(toplam)