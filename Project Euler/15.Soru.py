import math

faktoriyal_1 = 1
faktoriyal_2 = 1

for i in range(1,41):
    faktoriyal_1 *= i
for i in range(1,21):
    faktoriyal_2 *= i
    
kombinasyon_1 = math.comb(40,20)
kombinasyon_2 = math.factorial(40) / (math.factorial(20) ** 2)
kombinasyon_3 = faktoriyal_1 / (faktoriyal_2 ** 2)

print(kombinasyon_1)
print(kombinasyon_2)
print(kombinasyon_3)

